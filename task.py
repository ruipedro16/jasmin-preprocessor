import re

import utils
from generic_fn import GenericFn

import pprint

from typing import List


class Task:
    """
    Represents a task that needs to be resolved by inserting the concrete definition
    for the function in the Jasmin source code.

    Attributes:
        fn_name (str): The name of the function to be resolved in the Jasmin code.
        template_params (dict[str, int]): A dictionary of integer parameters to be used in the function.
        global_params (dict[str, int]): The dictionary of the global parameters
    """

    def __init__(
        self,
        fn_name: str,
        template_params: list[int],
        global_params: dict[str, int],
    ):
        self.fn_name = fn_name
        self.template_params = template_params
        self.global_params = global_params

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return (
            self.fn_name == other.fn_name
            and self.template_params == other.template_params
        )

    def __hash__(self):
        # Convert the list to a tuple for hashing (TypeError: unhashable type: 'list')
        return hash((self.fn_name, tuple(self.template_params)))

    def __repr__(self) -> str:
        params_str = ", ".join(str(param) for param in self.template_params)
        return f"Task(fn_name='{self.fn_name}', params=[{params_str}])"

    def resolve(
        self,
        text: str,
        global_params: dict[str, int],
        generic_fn_dict: dict[str, GenericFn],
    ) -> str:
        """
        Resolve the function and return the concrete definition
        """
        pattern = rf"// Place concrete instances of the {self.fn_name} function here"
        generic_fn: GenericFn = generic_fn_dict[self.fn_name]
        replacement_dict: dict[str, int] = dict(
            zip(generic_fn.params, self.template_params)
        )

        return re.sub(
            pattern,
            lambda match: match.group()
            + "\n"
            + utils.build_concrete_fn(generic_fn, replacement_dict)
            + "\n",
            text,
        )


import re

import utils
from generic_fn import GenericFn

import pprint
import ast

from typing import List


class Task:
    """
    Represents a task that needs to be resolved by inserting the concrete definition
    for the function in the Jasmin source code.

    Attributes:
        fn_name (str): The name of the function to be resolved in the Jasmin code.
        template_params (dict[str, int]): A dictionary of integer parameters to be used in the function.
        global_params (dict[str, int]): The dictionary of the global parameters
    """

    def __init__(
        self,
        fn_name: str,
        template_params: dict[str, int],
        global_params: dict[str, int],
    ):
        self.fn_name = fn_name
        self.template_params = template_params
        self.global_params = global_params

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return (
            self.fn_name == other.fn_name
            and self.template_params == other.template_params
        )

    def __hash__(self):
        # Convert the list to a tuple for hashing (TypeError: unhashable type: 'list')
        return hash((self.fn_name, tuple(self.template_params)))

    def __repr__(self) -> str:
        params_str = ", ".join(str(param) for param in self.template_params)
        return f"Task(fn_name='{self.fn_name}', params=[{params_str}])"

    def resolve(
        self,
        text: str,
        global_params: dict[str, int],
        generic_fn_dict: dict[str, GenericFn],
    ) -> str:
        """
        Resolve the function and return the concrete definition
        """
        pattern = rf"// Place concrete instances of the {self.fn_name} function here"
        generic_fn: GenericFn = generic_fn_dict[self.fn_name]
        replacement_dict: dict[str, int] = dict(
            zip(generic_fn.params, self.template_params)
        )

        return re.sub(
            pattern,
            lambda match: match.group()
            + "\n"
            + utils.build_concrete_fn(generic_fn, replacement_dict)
            + "\n",
            text,
        )

    def get_sub_tasks(
        self,
        generic_fn_dict: dict[str, GenericFn],
        context_params: dict[str, int] = None,
    ) -> List["Task"]:
        """
        Get the sub-tasks for the current task by resolving nested generic function calls.
        """
        # print(f"Getting subtasks of {self.fn_name}")

        subtasks = []
        generic_fn: GenericFn = generic_fn_dict[self.fn_name]
        resolved_fn_body = self.resolve(
            generic_fn.fn_body, self.global_params, generic_fn_dict
        )

        replacement_dict: dict[str, int] = dict(
            zip(generic_fn.params, self.template_params)
        )
        # print(f"Replacement dict of {self.fn_name}")
        # pprint.pprint(replacement_dict)

        # The 1st function call does not have
        if context_params is None:
            context_params = replacement_dict

        generic_fn_call_pattern = r"(\w+)<([^>]+)>\(([^)]+)\);"
        for match in re.finditer(generic_fn_call_pattern, resolved_fn_body):
            fn_name, generic_params, _ = match.groups()
            generic_params: list[str] = [p.strip() for p in generic_params.split(",")]
            # print(f"Generic params {generic_params}")
            concrete_params = {}

            for param in generic_params:
                try:
                    concrete_params[param] = context_params[
                        param
                    ]  # Context params may override global params
                except Exception:
                    concrete_params[param] = self.global_params[param]
            # print(f"Concrete params of {self.fn_name}")
            # pprint.pprint(concrete_params)

            concrete_args = [int(concrete_params.get(p, p)) for p in generic_params]
            # print("concrete args are")
            # print(concrete_args)
            subtask = Task(fn_name, concrete_args, self.global_params)
            subtasks.append(subtask)

        # Recursive step: Find and collect sub-tasks from the resolved function body
        for subtask in subtasks:
            sub_subtasks = subtask.get_sub_tasks(
                generic_fn_dict,
                concrete_params,  # Pass concrete_params in the recursion
            )
            subtasks.extend(sub_subtasks)

        # print("\n\n")

        return subtasks
