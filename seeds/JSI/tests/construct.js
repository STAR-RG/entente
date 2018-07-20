

var b = new Boolean(false);
print(b.constructor == Boolean );
print(Boolean == b.constructor );

function f() {};
function g() {};
g.prototype = new f();
var h = new g();

/*
=!EXPECTSTART!=
true
true
=!EXPECTEND!=
*/
