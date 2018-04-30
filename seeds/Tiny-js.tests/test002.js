assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// comparison
var a = 42;
result = a==42;
assert(result);
