import re
import sys

import multiprocessing
import concurrent.futures

from itertools import chain
from typing import Any

from generic_fn import GenericFn
from task import Task
from env import Env

import regex

word_sizes: list[str] = ["u8", "u16", "u32", "u64", "u128", "u256"]

cast_replacement_dict: dict[str, str] = {
    "!(u8)": "(8u)",
    "!(u16)": "(16u)",
    "!(u32)": "(32u)",
    "!(u64)": "(64u)",
    "!(u128)": "(128u)",
    "!(u256)": "(256u)",
}


def get_params(code: str) -> dict[str, int]:
    """
    Extracts and evaluates parameter declarations from Jasmin source code.
    The code assumes that all parameter declarations follow the format
    'param int <parameter_name> = <expression>;'
    """
    pattern = r"param\s+int\s+(\w+)\s*=\s*(.+);"
    matches = re.findall(pattern, code, re.MULTILINE)
    param_dict = dict(matches)
    res: dict[str, int] = {}
    visited: set[str] = set()

    def evaluate_expression(param_name: str):
        if param_name in visited:
            raise ValueError("Circular dependency.")

        visited.add(param_name)
        param_value = param_dict[param_name]
        res[param_name] = eval(param_value, None, res)
        visited.remove(param_name)

    for key in param_dict:
        evaluate_expression(key)

    return res


def get_generic_fn_dict(input_text: str) -> dict[str, GenericFn]:
    """
    Extracts generic function declarations from the input text and returns a dictionary
    containing information about each generic function.
    """
    res: dict[str, GenericFn] = {}

    pattern = regex.GENERIC_FUNCTION_REGEX

    if matches := re.finditer(pattern, input_text, flags=re.MULTILINE):
        for match in matches:
            annotation, fn_name, params, args, fn_body = match.groups()

            # print(f"Annotation: {annotation}")
            # print(f"Fn name: {fn_name}")
            # print(f"Params: {params}")
            # print(f"Args: {args}")
            # print(f"Fn Body: {fn_body}")
            # print("---------------", end="\n\n")

            annotation = annotation.strip() if annotation is not None else annotation
            if annotation is not None and "#" in annotation:
                annotation += "\n"

            generic_fn = GenericFn(annotation, fn_name, params, args, fn_body)
            res[fn_name] = generic_fn

    return res


def get_functions_from_source(code: str) -> list[str]:
    pattern = regex.FUNCTION_REGEX
    matches = re.findall(pattern, code, re.MULTILINE)
    return [match[1] for match in matches if not match[0].strip().startswith("export")]


def get_global_vars(code: str) -> dict[str, int]:
    """
    Same as get_params but for global variables.
    """
    # TODO: Should global arrays be supported ?
    res: dict[str, int] = {}
    return res


def parse_tasks(text: list[str], env: Env) -> list[Task]:
    if text is None:
        return []

    pattern = r"fn:[^ ]+\s+(\s*p:[^ ]+:\d+)+"

    res: list[Task] = []
    for s in text:
        if not re.match(pattern, s):
            sys.stderr.write("Invalid format for task\n")
            sys.stderr.write("Format should be fn:<function name> p:<parameter name>:parameter value\n")
            sys.stderr.write("Example: fn:shake256  p:OUTLEN:64 p:INLEN:64")
            sys.exit(-1)

        fields: list[str] = s.split()
        params: dict[str, int] = {}
        fn_name: str = fields[0].split(":")[-1]
        for field in fields:
            if field.startswith("p:"):
                # Split the field by ':'
                _, key, value = field.split(":")
                params[key] = int(value)

        task: Task = Task(fn_name, list(params.values()), env)
        res.append(task)

    return res


def get_tasks(text: str, env: Env) -> list[Task]:
    """
    This function also replaces generic function calls with calls to the concrete functions
    """
    tasks = set()
    generic_fn_call_pattern = r"(\w+)<(.+)>\(([^)]+)\);"

    def replace_fn(match) -> str:
        fn_name, generic_params, generic_args = match.groups()
        generic_params: list[str] = [p.strip() for p in generic_params.split(",")]
        concrete_params = {}

        for param in generic_params:
            try:
                # Evaluate the expression using the param_dict to get the
                # concrete value
                concrete_params[param] = eval(param.replace("/", "//"), None, env.global_params)
            except (NameError, TypeError, ValueError, SyntaxError):
                # If evaluation fails, use the original param as a string
                concrete_params[param] = param

        concrete_args = [str(concrete_params.get(p, p)) for p in generic_params]
        # Store the task with all parameters
        tasks.add((fn_name, tuple(concrete_args)))
        return f"{fn_name}_" + "_".join(concrete_args) + f"({generic_args})"

    text = re.sub(generic_fn_call_pattern, replace_fn, text)
    return [  # We only return the tasks that can be solved right away. We look for subtasks later
        Task(fn_name, list(params), env)
        for fn_name, params in tasks
        if all(param.isdigit() or param in word_sizes for param in params)
    ]


def remove_generic_fn_text(input_text: str) -> str:
    """
    Returns the updated input text with the generic function declarations removed
    """
    pattern = r"^([#\[\]\"=\w\s]*)\s+?fn\s+(\w+)<([^>]+)>\s*\(([^\)]+)\)([\s\S]*?)}//<>"

    matches = re.finditer(pattern, input_text, flags=re.MULTILINE)

    replacements = []

    for match in matches:
        _, fn_name, _, _, _ = match.groups()
        replacement_text = f"\n\n// Place concrete instances of the {fn_name} function here"
        replacements.append((match.start(), match.end(), replacement_text))

    # Sort the replacements in reverse order to ensure that replacing text doesn't affect other replacements
    replacements.sort(reverse=True)

    for start, end, replacement_text in replacements:
        input_text = input_text[:start] + replacement_text + input_text[end:]

    return input_text


def replace_generic_calls_with_concrete(text: str, env: Env) -> str:
    """
    Replaces generic function calls with concrete function calls based on the provided parameters.

    This function takes an input 'text' that may contain generic function calls with generic
    type parameters, e.g., 'my_function<T, U>(x, y)'. It also takes a dictionary 'global_params'
    containing concrete values for the generic type parameters. The function then replaces
    the calls to generic functions with the corresponding calls to concrete functions.

    For example, f = foo<2>(...) { ... } becomes f = foo_2(...) { ... } and
                 x = bar<2, 3>(...) { ... } becomes x = bar_2_3(...) { ... }
    """

    def replace_fn(match):
        fn_name, generic_params = match.groups()
        generic_params = [p.strip() for p in generic_params.split(",")]
        concrete_params: dict[str, int] = {}

        for param in generic_params:
            try:
                # Evaluate the expression using the global_params dict to get
                # the concrete value
                concrete_params[param] = eval(param.replace("/", "//"), None, env.global_params)
            except (NameError, TypeError, ValueError, SyntaxError):
                # If evaluation fails, use the original param as a string
                concrete_params[param] = param

        concrete_args = [str(concrete_params.get(p, p)) for p in generic_params]
        concrete_call = f"{fn_name}_" + "_".join(concrete_args)

        return concrete_call

    pattern = r"(\w+)<(.+)>"
    return re.sub(pattern, replace_fn, text)


def replace_parameters_in_string(text: str, replacement_dict: dict[str, int]) -> str:
    """_
    Auxiliary function to replace the parameters with their value
    """
    for key, value in replacement_dict.items():
        text = text.replace(f"{key}", str(value))
    return text


def build_concrete_fn(
    generic_fn: GenericFn,
    replacement_dict: dict[str, int],
) -> str:
    """
    Build the concrete function from the generic one.

    Args:
        generic_fn (GenericFn): Information about the generic function.
        replacement_dict (dict[str, int]): Map containing the value of each parameter to replace in the function.

    Returns:
        str: The concrete function as a string.
    """
    tmp = replace_parameters_in_string("_".join(generic_fn.params), replacement_dict)

    if generic_fn.annotation == "":
        res = f"fn {generic_fn.fn_name}_{tmp}({replace_parameters_in_string(generic_fn.args, replacement_dict)})"
    elif "#" in generic_fn.annotation:  # #[returnaddress="stack"] annotation
        res = f"{generic_fn.annotation}fn {generic_fn.fn_name}_{tmp}({replace_parameters_in_string(generic_fn.args, replacement_dict)})"
    else:
        res = f"{generic_fn.annotation} fn {generic_fn.fn_name}_{tmp}({replace_parameters_in_string(generic_fn.args, replacement_dict)})"
    res += replace_parameters_in_string(generic_fn.fn_body, replacement_dict)
    res += "}"

    return res


def flatten(input_list: list[list[Any]]) -> list[Any]:
    return list(chain(*input_list))


def find_subtasks(task: Task, env: Env) -> list[Task]:
    return task.get_sub_tasks(env)


def find_sub_taks_concurrenly(tasks: list[Task], env: Env) -> list[Task]:
    try:
        workers: int = multiprocessing.cpu_count()
    except NotImplementedError:
        workers: int = 1

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        # Submit tasks to the executor concurrently
        futures = [executor.submit(find_subtasks, task, env) for task in tasks]

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

        # Get results from the completed tasks
        subtasks: list[list[Task]] = [future.result() for future in futures]

    # new_tasks: list[Task] = [subtask for sublist in subtasks for subtask in sublist]
    new_tasks: list[Task] = flatten(subtasks)

    tasks.extend(new_tasks)
    return tasks


def find_sub_tasks_sequentially(tasks: list[Task], env: Env) -> list[Task]:
    new_tasks: list[Task] = []
    for task in tasks:
        new_tasks.extend(task.get_sub_tasks(env))
    tasks.extend(new_tasks)
    return tasks


def remove_duplicates(input_list: list[Any]) -> list[Any]:
    """
    Removes duplicates from a list and returns a new list with unique elements.

    Args:
        input_list (list[T]): The input list with potential duplicates.

    Returns:
        list[T]: A new list with duplicates removed.
    """
    if len(input_list) == 0:
        return input_list

    if not hasattr(input_list[0].__class__, "__eq__"):
        raise TypeError("Elements in the input list must implement the __eq__ method.")

    res = []

    for item in input_list:
        if item not in res:
            res.append(item)

    return res


def validate_tasks(tasks: list[Task]):
    for task in tasks:
        if not task.is_valid():
            sys.stderr.write(f"Invalid task: {task}\n")
            sys.exit(1)


def replace_eval_global_params(text: str, params: dict[str, int]) -> str:
    def eval_expression(match):
        name, expression = match.groups()
        try:
            value = eval(expression.replace("/", "//"), params)
            return f"param int {name} = {value};"
        except Exception as e:
            print(f"Error evaluating expression for {name}: {e}")
            return match.group(0)

    pattern = r"param\s+int\s+(\w+)\s*=\s*(.+);"
    updated_text = re.sub(pattern, eval_expression, text)
    return updated_text


def resolve_generic_fn_calls(text: str, env: Env) -> str:
    if text is None:
        return ""

    # Typed first
    typed_generic_fn_call_pattern = r"(\w+)<([^>]+)>\s*\[([^\]]+)]\(([^)]+)\);"
    for match in re.finditer(typed_generic_fn_call_pattern, text):
        fn_name, generic_params, type_info, args = match.groups()
        fn_names = [type_info.split(";")[0].strip()]
        fn_names = [name for name in fn_names if name != ""]

        fn_types = [type_info.split(";")[-1].strip()]
        fn_types = [type for type in fn_types if type != ""]

        names_types = list(zip(fn_names, fn_types))
        replacement = (
            fn_name
            + "_"
            + "_".join([x + "_" + y for x, y in names_types] + [generic_params])
            + "("
            + ", ".join(args)
            + ");"
        )
        text = re.sub(re.escape(match.group(0)), replacement, text)

    # Regular generic fn
    text = re.sub(
        r"(\w+)<(.+)>",
        lambda match: f"{match.group(1)}_{'_'.join(str(env.global_params.get(p.strip(), eval(p.strip().replace('/', '//'), {}, env.global_params))) for p in match.group(2).split(','))}",
        text,
    )

    return text


def replace_casts(text: str) -> str:
    for key, value in cast_replacement_dict.items():
        text = text.replace(f"{key}", value)
    return text
