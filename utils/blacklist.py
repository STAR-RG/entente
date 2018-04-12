# TODO: keep updating...

# this list contains invalid message output
INVALID_STRINGS = [
    "file with feature not implemented yet",
    "is not a function",
    "is not defined",
    "is not an Object",
    "is not a constructor",
    "is not iterable",
    "is not a valid",
    "is not valid",
    "undefined",
    "find variable",
    "support this action",
    "support property",
    "Invalid or unexpected token",
    "unexpected token",
    "illegal character",
    "Invalid character",
    "Invalid operand",
    "Object expected",
    # "TIMEOUT",
    "Invalid string length",
    "be less than infinity",
    # "Out of stack space",
    # "Out of memory",
    "too much recursion",
    "stack size exceeded",
    "requires more than",
    "should be an Object",
    "must be a",
    "must be an",
    # "must be an object",
    # "must be a function",
    # "must be an ArrayBuffer",
    "non-object as target",
    "called on incompatible",
    "can only be called",
    "called on non-object",
    "requires the first argument",
    "invalid regular expression",
    "error in regular expression",
    "Cannot read property",
    "Cannot use",
    "is null",
    "without new is invalid",
    "without new is forbidden",
    "requires 'new'",
    "|new|",
    "without 'new'",
    "access lexical declaration",
    "before declaration",
    "uninitialized variable",
    "undeclared variable",
    "keyword",
    "reserved identifier",
    "missing formal parameter",
    "hand side",
    "cannot be destructured",
    "must be a string literal",
    "expected double-quoted",
    "Declaration outside",
    "classes can't appear",
    "Unterminated string",
    "literal not terminated",
    "Cannot convert",
    "can't convert",
    "Error: true",
    "cannot be a RegExp",
    "be a Regular Expression",
    "cannot be a RegExp",
    "super() is only valid",
    "got '...'",
    "... operator",
    "setter functions must have one argument",
    "JSON Parse error: Expected ':'",
    "JSON.parse Error: Expected ':'",
    "JSON.parse: expected ':'",
    "Invalid flags supplied",
    "Arg string terminates",
    "after formal parameters",
    "Expected ')'",
    "Invalid unicode escape",
    "Function expected",
]

# these lists contains invalid code in JS file

OPERATORS = [
    "-=="
]

# features not implemented on chakra
CHAKRA_KEYWORDS = [
    "Symbol.split",
    "Symbol.search",
    "Symbol.replace",
    "Symbol.match",
    "(RegExp.prototype, 'flags')",
    ".flags",
    "Array.prototype.values",
    "RegExp.prototype.test",
    "RegExp.prototype.toString.call",
    "(E.prototype) === '[object Object]'"
] + OPERATORS

# features not implemented on v8
V8_KEYWORDS = [
    "Array.prototype.values"
] + OPERATORS

# features not implemented on jscore
JSCORE_KEYWORDS = [] + OPERATORS

# features not implemented on spidermonkey
SPIDERMONKEY_KEYWORDS = [
    "dotAll"
] + OPERATORS


ENGINES_KEYWORDS = {
    "chakra": CHAKRA_KEYWORDS,
    "jscore": JSCORE_KEYWORDS,
    "spidermonkey": SPIDERMONKEY_KEYWORDS,
    "v8": V8_KEYWORDS
}