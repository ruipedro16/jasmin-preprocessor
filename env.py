import re
import pprint

import utils
from generic_fn import GenericFn


class Env:
    def __init__(self, text: str) -> None:
        self.global_params: dict[str, int] = utils.get_params(text)
        self.global_vars: dict[str, int] = utils.get_global_vars(text)
        self.functions: list[str] = utils.get_functions(text)
        self.generic_functions: dict[str, GenericFn] = utils.get_generic_fn_dict(text)

    def __repr__(self) -> str:
        # TODO:
        pass
