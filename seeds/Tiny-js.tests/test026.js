assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// check for undefined-ness
a = undefined;
b = "foo";
result = a==undefined && b!=undefined;
assert(result);
