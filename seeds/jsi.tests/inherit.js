

var a = { x:1, y:0};
a.z = function() { print('CALLED Z'); };
var b = { y:2 };
Object.setPrototypeOf(b, a);
a.x++;
for (var i in b) { print(i+'='+b[i]); }
b.z();

/*
=!EXPECTSTART!=
y=2
x=2
z=function () {...}
CALLED Z
=!EXPECTEND!=
*/
