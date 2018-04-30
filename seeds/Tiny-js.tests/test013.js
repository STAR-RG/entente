assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// if .. else with blocks
var a = 42;
if (a != 42) {
   result = 0;
} else {
  result = 1;
}
assert(result);
