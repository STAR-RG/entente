/* Javascript eval */

myfoo = eval("{ foo: 42 }");

assert(eval("4*10+2")==42 && myfoo.foo==42);
