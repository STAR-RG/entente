assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// simple for loop
var a = 0;
var i;
for (i=1;i<10;i++) a = a + i;
result = a==45;
assert(result);
