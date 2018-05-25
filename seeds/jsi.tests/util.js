

var x = 0;
function foo(n) { return n+1; }
function bar() { x += foo(0); }
var tim = Util.times(bar,100000);
print(x);

/*
=!EXPECTSTART!=
100000
=!EXPECTEND!=
*/
