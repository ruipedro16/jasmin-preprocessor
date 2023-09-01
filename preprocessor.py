#!/bin/env python3

import sys
import os
import re
import sys
import pprint

import argparse

import utils
from generic_fn import GenericFn
from task import Task

"""
Example: python3 preprocessor.py --parameters param1.txt param2.txt --source source1.txt source2.txt --output_file stdout
"""

DEBUG: bool = False


def parse_args():
    parser = argparse.ArgumentParser(description="Jasmin source code preprocessor")

    parser.add_argument(
        "--source",
        nargs="+",
        required=True,
        help="List of source files",
        type=str,
    )

    parser.add_argument(
        "--parameters",
        nargs="+",
        required=False,
        help="List of parameter files",
        type=str,
    )

    parser.add_argument(
        "--output_file",
        required=True,
        help="Output file path",
        type=str,
    )

    return parser.parse_args()


def resolve_templates(
    text: str, global_params: dict[str, int], generic_fn_dict: dict[str, GenericFn]
) -> str:
    """
    Resolves templates in the source code.
    The code assumes that all template declarations follow the format
    '[inline] fn <function_name><template_params>(<parameters>) -> <return_type> { <function_body> } // <>'
    """
    # 1st step: Update global params dict. The source file may define new `param int` variables or override previously
    #           defined ones
    tmp: dict[str, int] = utils.get_params(text)
    global_params.update(tmp)

    # 2nd step: Update generic functions dict from Jasmin source code
    tmp: dict[str, GenericFn] = utils.get_generic_fn_dict(text)
    generic_fn_dict.update(tmp)

    # 3rd step: Remove the code of the generic functions from the source code
    text = utils.remove_generic_fn_text(text)

    # 4th step: Replace calls to generic functions with calls to concrete functions
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
        lambda match: f"{match.group(1)}_{'_'.join(str(global_params.get(p.strip(), p.strip())) for p in match.group(2).split(','))}",
        text,
    )

    # Last step: Remove extra blank space & remove auxiliary comments

    pattern = r"// Place concrete instances of the (\w+) function here"
    text = re.sub(pattern, "", text)

    pattern = r"\n{3,}"
    while re.search(pattern, text):
        text = re.sub(pattern, "\n\n", text)

    text = text.strip()

    return text


if __name__ == "__main__":
    args = parse_args()

    all_files = []
    if args.parameters:
        all_files.extend(args.parameters)
    if args.source:
        all_files.extend(args.source)

    # Check if all files exist
    for file in all_files:
        if not os.path.exists(file):
            sys.stderr.write(f"Error: The file '{file}' does not exist.\n")
            sys.exit(-1)

    global_params: dict[str, int] = {}
    generic_fn_dict: dict[str, GenericFn] = {}

    # 1st step: Load global parameters from param files
    if args.parameters:
        for file in args.parameters:
            with open(file, "r") as f:
                text: str = f.read()
            tmp: dict[str, int] = utils.get_params(text)
            global_params.update(tmp)

    if DEBUG:
        print("DEBUG: Global Param Dictionary")
        pprint.pprint(global_params)

    if args.source:
        for file in args.source:
            with open(file, "r") as f:
                text: str = f.read()
            tmp: dict[str, GenericFn] = utils.get_generic_fn_dict(text)
            generic_fn_dict.update(tmp)

    if DEBUG:
        print("DEBUG: Generic Fn Dictionary:")
        pprint.pprint(generic_fn_dict.keys())
        
    # exit(0)

    input_file: str = args.source[0]

    with open(input_file, "r") as f:
        input_text: str = f.read()

    output_text: str = resolve_templates(input_text, global_params, generic_fn_dict)
    output_text += "\n"

    if DEBUG:
        print("\n--------------------------------------------------------------\n")

    with open(args.output_file, "w") as f:
        f.write(output_text)
