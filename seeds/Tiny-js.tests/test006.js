assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// simple function
function add(x,y) { return x+y; }
result = add(3,6)==9;
assert(result);
