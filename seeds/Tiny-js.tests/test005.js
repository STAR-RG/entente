assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// simple for loop containing initialisation, using +=
var a = 0;
for (var i=1;i<10;i++) a += i;
result = a==45;
assert(result);
