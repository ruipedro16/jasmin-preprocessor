#!/bin/env python3

import sys
import os
import re
import sys
import pprint

from collections import OrderedDict

import utils
from generic_fn import GenericFn
from task import Task

DEBUG: bool = False


def resolve_templates(text: str) -> str:
    """
    Resolves templates in the source code.
    The code assumes that all template declarations follow the format
    '[inline] fn <function_name><template_params>(<parameters>) -> <return_type> { <function_body> } // <>'
    """

    # 1st Step: Evaluate the global parameters
    global_params: dict[str, int] = utils.get_params(text)

    if DEBUG:
        print("DEBUG: Global Param Dictionary")
        pprint.pprint(global_params)

    # 2nd step: Identify generic functions from Jasmin source code
    generic_fn_dict: dict[str, GenericFn] = utils.get_generic_fn_dict(text)

    if DEBUG:
        print("LOG: Generic Fn Dictionary:")
        pprint.pprint(generic_fn_dict)

    # 3rd step: Remove the code of the generic functions from the source code
    text = utils.remove_generic_fn_text(text)

    # 4th step: Replace calls to generic functions with calls to concrete functions
    # NOTE: TODO: Doesnt work with nested function calls
    text = utils.replace_generic_calls_with_concrete(text, global_params)

    # 5th step: Get a list of all the tasks that need to be done
    # First, we gather the tasks without handling nested calls, and then, after all
    # the tasks are collected, resolve the nested calls in the Task class.
    # This needs to be done on the input_text instead of the already processed text
    tasks: list[Task] = utils.get_tasks(input_text, global_params)
    if DEBUG:
        print("Tasks [1st pass]:")
        pprint.pprint(tasks)

    if DEBUG:
        print("Searching for subtasks")

    for task in tasks:
        subtasks = task.get_sub_tasks(generic_fn_dict)
        tasks.extend(subtasks)

    if DEBUG:
        print("Tasks [2nd pass (includes subtasks)]:")
        pprint.pprint(tasks)

    # Remove duplicate tasks
    tasks = list(set(tasks))

    if DEBUG:
        print("Tasks [3rd pass (removes duplicate tasks)]:")
        pprint.pprint(tasks)

    # 6th step: Resolve each task
    for task in tasks:
        text = task.resolve(text, global_params, generic_fn_dict)

    # 7th step: Resolve generic function calls that were not resolved before
    text = re.sub(
        r"(\w+)<([^>]+)>",
        lambda match: f"{match.group(1)}_{'_'.join(match.group(2).split(','))}",
        text,
    )

    # Last step: Remove extra blank space & remove auxiliary comments
    pattern = r"\n{3,}"
    text = re.sub(pattern, "\n\n", text)

    pattern = r"// Place concrete instances of the (\w+) function here"
    text = re.sub(pattern, "", text)

    text = text.strip()

    return text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <input_file>\n")
        sys.exit(-1)

    input_file: str = sys.argv[1]

    if not os.path.exists(input_file):
        sys.stderr.write(f"Error: The file '{input_file}' does not exist.\n")
        sys.exit(-1)

    with open(input_file, "r") as f:
        input_text: str = f.read()

    output_text: str = resolve_templates(input_text)

    if DEBUG:
        print("\n--------------------------------------------------------------\n")
    print(output_text)
