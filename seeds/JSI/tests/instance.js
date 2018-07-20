

function f() {};
function j() {};
var x = new f();
print(x instanceof f);
print(x instanceof j);
print(x instanceof Object);

/*
=!EXPECTSTART!=
true
false
true
=!EXPECTEND!=
*/
