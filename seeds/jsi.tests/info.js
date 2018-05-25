

var x = 1;
var xx = 2;
var y = 2;

print(Info.vars('x'));
print(Info.vars(/x/));
print(Info.vars());

function X(a) {var jj=1, kk; return jj++;}
function XX(a) {}
function Y(a) {}

print(Info.funcs('X').argList);
print(Info.funcs(/X/));
print(Info.funcs());

var K = {};
K.f = function(z) { print("F"); };
K.g = function(z) { print("G"); };
K.f();
print(Info.funcs(K.f).argList);
print(Info.funcs(K));

print(File.tail(Info.script()));
print(File.tail(Info.script(XX)));
print(File.tail(Info.script(/.*/)[0]));

print(Info.cmds(/^loa./));
print(Info.cmds('String.concat'));

X.prototype.P = function(M) { return M; };
X.prototype.Q = function(M) { return M; };
print(Info.funcs(X.prototype));

/*
=!EXPECTSTART!=
{ type:"number" }
[ "xx", "x" ]
[ "xx", "x", "y" ]
[ "a" ]
[ "XX", "X" ]
[ "XX", "X", "Y" ]
F
[ "z" ]
[ "f", "g" ]
info.js
info.js
info.js
[ "load" ]
{ args:"str:string, ...", flags:0, help:"Append one or more strings", maxArgs:-1, minArgs:0, name:"String.concat", retType:"string", type:"command" }
[ "P", "Q" ]
=!EXPECTEND!=
*/
