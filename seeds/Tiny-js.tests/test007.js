assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// simple function scoping test
var a = 7;
function add(x,y) { var a=x+y; return a; }
result = add(3,6)==9 && a==7;
assert(result);
