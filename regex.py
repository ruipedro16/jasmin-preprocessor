# Regex for a "standard Jasmin" function
# Group 0: Annotation
# Group 1: Function name
# Group 2: Arguments => Even if a functions does not have <> it can still not be "standard jasmin" because it may take a function as argument
FUNCTION_REGEX = r"([#\[\]\"=\w]+)?\s+?fn\s+(\w+)\s*\(([^\)]+\))"

GENERIC_FUNCTION_REGEX = r"([#\[\]\"=\w]+)?\s+?fn\s+(\w+)<([^>]+)>\s*\(([^\)]+)\)([\s\S]*?)}//<>"

"""
This regex mathces a function that takes another function as argument

Eg:

inline fn f<A, B>(fn foo(reg u8) -> reg u8, reg ptr u8[5] a)
                  -> reg ptr u8[5] {
    ...
}//<>

groups[0] : inline
groups[1] : f
groups[2] : <A, B> (This group will never be used. It is here because it is optional)
groups[3] : A, B
groups[4] : fn foo(reg u8) -> reg u8, reg ptr u8[5] a
groups[5] : function body

FIXME: TODO: This requires that there is a \n between the closing ) of the arguments and the return type

The problem is that ([^\)]+) fins the shortest match instead of the longest. This means that the 4th group
would be fn foo(reg u8 instead of fn foo(reg u8) -> reg u8, reg ptr u8[INLEN] a
"""
FUNCTION_AS_ARG_REGEX = r"([#\[\]\"=\w]+)\s+?fn\s+(\w+)(<([^>]+)>)?\s*\((.+)\)([\s\S]*?)}//<>"
