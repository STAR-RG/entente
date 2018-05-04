

var a = { "x":[4,5,6], "y":{a:1, b:2}};
var b = { n:a, m:a.y };
print (b.n);
print (b.m);

function a() { return {x:1, y:{a:1,b:[]}}; };
print(a().y.a);

/*
=!EXPECTSTART!=
{ x:[ 4, 5, 6 ], y:{ a:1, b:2 } }
{ a:1, b:2 }
1
=!EXPECTEND!=
*/
