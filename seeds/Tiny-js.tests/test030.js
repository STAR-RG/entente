assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// test for array join
var a = [1,2,4,5,7];

result = a.join(",")=="1,2,4,5,7";
assert(result);
