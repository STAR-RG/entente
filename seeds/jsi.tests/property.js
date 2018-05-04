

var x = {x:1};
print(x.propertyIsEnumerable('x'));
var x = {a:1, b:2};
print(x.hasOwnProperty('a'));
print(x.hasOwnProperty('c'));

function f() {}
f.a = 9;
function g() {}
g.prototype.x = new f();
var h = new g();
print(f.a);
print(g.a);
print(h.a);

var s = new String("Sample");
print(s.hasOwnProperty("split"));
print(String.prototype.hasOwnProperty("split"));

/*
=!EXPECTSTART!=
true
true
false
9
undefined
undefined
false
true
=!EXPECTEND!=
*/
