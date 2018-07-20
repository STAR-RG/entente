

var a = eval("{ test:1}");
print(a);

var b = eval("print({a:1,b:2,c:3,d:4});");
print(b);
b = eval("print({a:1,b:2,c:3,d:4})", x, n, g, k);
print(b);

/*
=!EXPECTSTART!=
{ test:1 }
{ a:1, b:2, c:3, d:4 }
undefined
{ a:1, b:2, c:3, d:4 }
undefined
=!EXPECTEND!=
*/
