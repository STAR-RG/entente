assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
/* Javascript eval */

myfoo = eval("{ foo: 42 }");

result = eval("4*10+2")==42 && myfoo.foo==42;
assert(result);
