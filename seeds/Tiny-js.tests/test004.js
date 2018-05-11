assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// simple if
var a = 42;
if (a < 43)
  result = 1;
assert(result);
