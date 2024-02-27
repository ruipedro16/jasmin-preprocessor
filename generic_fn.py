class GenericFn:
    """
    Represents a generic function with its respective relevant attributes.

    Attributes:
        annotation (str): The inline annotation (optional; may be the empty string).
        fn_name (str): The name of the function.
        params (list[str]): A string representing the generic parameters enclosed in angle brackets.
        args (str): A string representing the generic arguments provided when calling the function.
        fn_body (str): The body of the generic function. May contain calls to other generic ~
                       functions. Also contains the return type
    """

    def __init__(
        self, annotation: str, fn_name: str, params: str, args: str, fn_body: str, functions_as_args: list[str] = None
    ):
        self.annotation: str = annotation
        self.fn_name: str = fn_name
        self.params: list[str] = [] if params is None else [p.strip() for p in params.split(",")]
        self.args: str = args
        self.fn_body: str = fn_body
        self.functions_as_args: list[str] = functions_as_args

    def __repr__(self) -> str:
        return (
            f"Annotation: {self.annotation}\n"
            f"Function Name: {self.fn_name}\n"
            f"Parameters: {self.params}\n"
            f"Arguments: {self.args}\n"
            f"Function Body:\n{self.fn_body}\n\n"
            f"Functions as Arguments: {self.functions_as_args}\n\n"
        )
