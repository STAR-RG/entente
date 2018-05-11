

var b = new Boolean(true);
print(b.valueOf());

var s = new String('aa');
print(s.valueOf());

var x = { a:1, b:3 };
print(x.valueOf());

print(b.constructor);
print(Boolean);
print(Boolean == b.constructor);

/*
=!EXPECTSTART!=
true
aa
{ a:1, b:3 }
"function Boolean(bool:boolean=false) { [native code] }"
"function Boolean(bool:boolean=false) { [native code] }"
true
=!EXPECTEND!=
*/
