

var a = {};
eval("a.a = 1;");
print(a);


var y = eval("{ a:1, b:2, c:'abc', d:[1,2,3], e: {}}");
print(y);


var n = 'abc';
eval("(y = n)");

print(y);

/*
=!EXPECTSTART!=
{ a:1 }
{ a:1, b:2, c:"abc", d:[ 1, 2, 3 ], e:{} }
abc
=!EXPECTEND!=
*/
