import pprint
import sys
import re

from typing import Optional

import utils
from env import Env
from generic_fn import GenericFn

from io import StringIO


class Task:
    """
    Represents a task that needs to be resolved by inserting the concrete definition
    for the function in the Jasmin source code.

    Attributes:
        fn_name (str): The name of the function to be resolved in the Jasmin code.
        template_params (list[str]): A list of the value of the parameters to be used in the function. At this point, the
                                     value is already evaluated. E.g. 42 instead of INLEN
        env (Env): The environment
    """

    def __init__(self, fn_name: str, template_params: list[int], env: Env, functions_as_args: list[str] = None):
        self.fn_name: str = fn_name  # Name of the generic function. Not the name of the resolved function I think (?)
        self.template_params: list[int] = template_params
        self.env: Env = env
        self.functions_as_args: list[str] = functions_as_args if functions_as_args is not None else []

    def __repr__(self) -> str:
        template_params_buf: StringIO = StringIO()
        pprint.pprint(self.template_params, stream=template_params_buf)
        template_params_str: str = template_params_buf.getvalue()

        high_order_functions_buf: StringIO = StringIO()
        pprint.pprint(self.functions_as_args, stream=high_order_functions_buf)
        high_order_functions_str: str = high_order_functions_buf.getvalue()

        return (
            "Task:\n"
            f"Function name: {self.fn_name}\n"
            f"Template parameters: {template_params_str}"
            f"High Order Functions: {high_order_functions_str}"
        )

    def get_resolved_fn_name(self) -> str:
        template_params_str: list[str] = [str(param) for param in self.template_params]
        return f"{self.fn_name}_" + "_".join(template_params_str)

    def __eq__(self, other: object):
        if not isinstance(other, Task):
            return False

        template_params_int_self: list[int] = [int(val) for val in self.template_params]
        template_params_int_other: list[int] = [
            int(val) for val in other.template_params  # TODO: This cast to int shouldnt be necessary
        ]

        return self.fn_name == other.fn_name and template_params_int_self == template_params_int_other

    def __hash__(self):
        # Convert the list to a tuple for hashing (TypeError: unhashable type: 'list')
        return hash((self.fn_name, tuple(self.template_params)))

    def is_valid(self) -> bool:
        return self.fn_name != ""

    def resolve(self, text: str, env: Env) -> str:
        """
        Resolve the function and return the concrete definition
        """
        pattern = rf"// Place concrete instances of the {self.fn_name} function here"

        generic_fn: Optional[GenericFn] = None
        try:
            generic_fn = env.generic_functions[self.fn_name]
        except KeyError:
            sys.stderr.write(f"Could not find {self.fn_name} in env.generic_functions in Task.resolve [1]\n")
            sys.exit(-1)

        replacement_dict: dict[str, int] = dict(zip(generic_fn.params, self.template_params))

        if generic_fn.functions_as_args is not None:
            functions_as_args_dict: dict[str, int] = dict(zip(generic_fn.functions_as_args, self.functions_as_args))
            replacement_dict.update(functions_as_args_dict)

        # print(f"DEBUG: Printing replacement DICT of task {self.fn_name}")
        # pprint.pprint(replacement_dict)

        return re.sub(
            pattern,
            lambda match: match.group() + "\n" + utils.build_concrete_fn(generic_fn, replacement_dict) + "\n",
            text,
        )

    def get_sub_tasks(
        self,
        env: Env,
        context_params: Optional[dict[str, int]] = None,  # None in the first iteration
    ) -> list["Task"]:
        """
        Get the sub-tasks for the current task by resolving nested generic function calls.
        """
        subtasks: list["Task"] = []

        generic_fn: Optional[GenericFn] = None

        # TODO: FIXME: PEercebi 0 deste if
        function_name = self.fn_name
        if context_params is not None:  # If we are not in the first iteration
            try:
                function_name = eval(self.fn_name, {}, context_params)
                print(f"Name: {function_name}")
            except NameError:
                pass

        try:
            generic_fn = env.generic_functions[function_name]
        except KeyError:
            sys.stderr.write(f"Could not find {self.fn_name} in generic_fn_dict in Task.get_sub_tasks [2]\n")
            sys.exit(-1)

        resolved_fn_body: str = self.resolve(generic_fn.fn_body, env)

        # The 1st function call does not have
        if context_params is None:
            context_params = dict(zip(generic_fn.params, self.template_params))

            # FIXME: I think these next 2 lines are not needed
            tmp = dict(zip(generic_fn.params, self.template_params))
            context_params.update(tmp)

        # Find nested generic function calls
        generic_fn_call_pattern = r"(\w+)<([^>]+)>\(([^)]+)\);"
        for match in re.finditer(generic_fn_call_pattern, resolved_fn_body):
            fn_name, generic_params, _ = match.groups()

            # If the function already exists, we don't generate it
            # This is to support recursive functions. The base case is written in "standard jasmin"
            # and the inductive case is written in "high level jasmin"
            # if fn_name in env.functions:
            #    continue  # Skip to the next iteration
            """
            if fn_name == self.target_fn_name:
                sys.stderr.write(f"Recursive functions not supported: {self.fn_name}\n")
                sys.exit(-1)
            """

            generic_params: list[str] = [p.strip() for p in generic_params.split(",")]

            for param in generic_params:
                # If the parameter exists, we recompute it regardless.
                # This is stupid but we need it to support recursive functions
                try:
                    _ = context_params.pop(param)
                except KeyError:
                    pass

                try:
                    # Context params may override global params
                    context_params[param] = int(context_params[param])  # Nao percebi
                except KeyError:
                    try:
                        # get param from context_params else the default value is env.global_params[param]
                        context_params[param] = context_params.get(param, env.global_params[param])
                    except KeyError:
                        template_params_int: list[int] = [int(val) for val in self.template_params]

                        template_dict: dict[str, int] = dict(
                            zip(
                                env.generic_functions[self.fn_name].params,
                                template_params_int,
                            )
                        )  # TODO: handle key error

                        context_params[param] = eval(
                            param.replace("/", "//"),
                            {},
                            {
                                **env.global_params,
                                **context_params,
                                **template_dict,
                            },
                        )

                    except Exception:
                        sys.stderr.write(f"Could not evaluate parameter: {param}\n")

            concrete_args: list[int] = [int(context_params.get(p, p)) for p in generic_params]

            subtask = Task(fn_name, concrete_args, env)
            subtasks.append(subtask)

        # Recursive step: Find and collect sub-tasks from the resolved function body
        replacement_dict: dict[str, int] = dict(zip(generic_fn.params, self.template_params))

        # Recursive functions: Check if any subtask corresponds to a base case already defined in "standard" jasmin.
        # If so, we remove that task
        subtasks = [subtask for subtask in subtasks if subtask.get_resolved_fn_name() not in env.functions]

        for subtask in subtasks:
            sub_subtasks = subtask.get_sub_tasks(
                env,
                {
                    **env.global_params,
                    **context_params,
                    **replacement_dict,
                },  # Pass resolved_params_local in the recursion
            )
            subtasks.extend(sub_subtasks)

        return subtasks
