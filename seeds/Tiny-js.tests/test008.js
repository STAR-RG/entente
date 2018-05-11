assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// functions in variables
var bob = {};
bob.add = function(x,y) { return x+y; };

result = bob.add(3,6)==9;
assert(result);
