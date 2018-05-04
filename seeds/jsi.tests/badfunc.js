

var x = {a:1, b:2};
x.big = function() {};
x.bad = function() {};
x.ugly = function() {};
try {
  x.xx();
} catch(e) {
  print(e);
}
print(Info.funcs(x));
print(Info.data(x));
print(Info.data());

/*
=!EXPECTSTART!=
'xx', functions are: bad big ugly.
[ "bad", "big", "ugly" ]
[ "a", "b" ]
[ "x" ]
=!EXPECTEND!=
*/
