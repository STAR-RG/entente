assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// test for string split
var b = "1,4,7";
var a = b.split(",");

result = a.length==3 && a[0]==1 && a[1]==4 && a[2]==7;
assert(result);
