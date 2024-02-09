# Regex for a "standard Jasmin" function
# Group 0: Annotation
# Group 1: Function name
FUNCTION_REGEX = r"([#\[\]\"=\w]+)?\s+?fn\s+(\w+)\s*\([^\)]+\)"

GENERIC_FUNCTION_REGEX = r"([#\[\]\"=\w]+)?\s+?fn\s+(\w+)<([^>]+)>\s*\(([^\)]+)\)([\s\S]*?)}//<>"
