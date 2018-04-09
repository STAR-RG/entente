# TODO: keep updating...

INVALID_STRINGS = [
    "file with feature not implemented yet",
    "is not a function",
    "is not defined",
    "undefined",
    "support this action",
    "support property",
    "test is not a function",
    "Invalid or unexpected token",
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
]

# these lists contains invalid code in JS file

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
]

# features not implemented on v8
V8_KEYWORDS = [
    "Array.prototype.values"
]

# features not implemented on jscore
JSCORE_KEYWORDS = []

# features not implemented on spidermonkey
SPIDERMONKEY_KEYWORDS = [
    "dotAll"
]


ENGINES_KEYWORDS = {
    "chakra": CHAKRA_KEYWORDS,
    "jscore": JSCORE_KEYWORDS,
    "spidermonkey": SPIDERMONKEY_KEYWORDS,
    "v8": V8_KEYWORDS
}