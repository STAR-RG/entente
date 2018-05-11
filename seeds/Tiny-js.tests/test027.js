assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// test for postincrement working as expected
var foo = 5;
result = (foo++)==5;
assert(result);
