import re
import pprint

import utils
from generic_fn import GenericFn

from io import StringIO


class Env:
    def __init__(self, text: str) -> None:
        self.global_params: dict[str, int] = utils.get_params(text)
        self.global_vars: dict[str, int] = utils.get_global_vars(text)  # TODO: Not implemented yet
        self.functions: list[str] = utils.get_functions_from_source(text)
        self.generic_functions: dict[str, GenericFn] = utils.get_generic_fn_dict(text)

    def __repr__(self) -> str:
        global_params_buf: StringIO = StringIO()
        pprint.pprint(self.global_params, stream=global_params_buf)
        global_params_str: str = global_params_buf.getvalue()

        functions_buf: StringIO = StringIO()
        pprint.pprint(self.functions, stream=functions_buf)
        functions_str: str = functions_buf.getvalue()

        generic_functions_buf: StringIO = StringIO()
        pprint.pprint(list(self.generic_functions.keys()), stream=generic_functions_buf)
        generic_functions_str: str = generic_functions_buf.getvalue()

        return (
            f"Global Parameters: {global_params_str}"
            f'Functions ["standard" jasmin] (not including export): {functions_str}'
            f"Generic functions (including high order functions): {generic_functions_str}"
        )
