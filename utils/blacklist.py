# TODO: keep updating...

INVALID_STRINGS = [
    "file with feature not implemented yet",
    "is not a function",
    "is not defined",
    "undefined",
    "find variable",
    "support this action",
    "support property",
    "test is not a function",
    "Invalid or unexpected token",
    "unexpected token",
    "Unexpected token",
    "illegal character",
    "Invalid character",
    "Object expected",
    "TIMEOUT",
    "Invalid string length",
    "be less than infinity",
    "Out of stack space",
    "Out of memory",
    "too much recursion",
    "stack size exceeded",
    "requires more than",
    "is not an Object",
    "should be an Object",
    "must be an object",
    "non-object as target",
    "called on incompatible",
    "can only be called",
    "called on non-object",
    "requires the first argument",
    "invalid regular expression",
    "Invalid regular expression",
    "error in regular expression",
    "Cannot read property",
    "Cannot use",
    "is null",
    "is not a constructor",
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
    "is not iterable",
    "hand side",
    "must be a string literal",
    "expected double-quoted",
    "Declaration outside",
    "classes can't appear",
    "Unterminated string",
    "literal not terminated",
    "is not a valid",
    "Cannot convert",
    "can't convert",
    "Error: true",
    "cannot be a RegExp",
    "be a Regular Expression",
    "be a regular expression",
    "cannot be a RegExp"
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