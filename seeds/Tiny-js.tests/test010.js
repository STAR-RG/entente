assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// double function calls
function a(x) { return x+2; }
function b(x) { return a(x)+1; }
result = a(3)==5 && b(3)==6;
assert(result);
