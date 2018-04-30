assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// references with functions

var a = 42;
var b = [];
b[0] = 43;

function foo(myarray) {
  myarray[0]++;
}

function bar(myvalue) {
  myvalue++;
}

foo(b);
bar(a);

result = a==42 && b[0]==44;
assert(result);
