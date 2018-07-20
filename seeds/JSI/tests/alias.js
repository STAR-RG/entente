

var i = new Interp({subthread:false});
//var i = new Interp();
function myAlias(interp,name,arg1,arg2) {
   //print('myAlias: '+interp+' '+name+' '+arg1+' '+arg2);
   print('myAlias:',interp,name,arg1,arg2);
}

function myAlias2(arg1,arg2) {
   print('myAlias2: '+arg1+' '+arg2);
}

i.alias('foo', myAlias, [i, 'foo']);
i.alias('bar', myAlias2,null);

print(i.alias());
print(i.alias('foo'));
print(i.alias('foo', null));

i.eval('bar(1,2);');

print('A');
i.eval('var bb = {x:1};');
print('B');
i.alias('bb.fig', myAlias, [i, 'bb.fig']);
i.eval('bb.fig(1)');

/*i.alias('bb.fig', myAlias, [i, 'bb.FIG']);
i.eval('bb.fig(1)');*/

print(i.alias());
//i.alias('bb.fig', null, null); //Leaks memory.
i.alias('foo', null, null);
print(i.alias());


// Set alias on Interp
function foo(a,b) {
  print('A='+a+' B='+b);
}
foo(1,2);

Interp.alias('bar', foo, [3]);
bar(4);

//try { i.eval('bb.fig(1)'); } catch(e) { print("CAUGHT ERROR: "+e); };
print("OK");

/*
=!EXPECTSTART!=
[ "foo", "bar" ]
"function myAlias(interp, name, arg1, arg2) {...}"
[ "#Interp_1", "foo" ]
myAlias2: 1 2
A
B
myAlias: "#Interp_1" bb.fig 1 undefined
[ "bb.fig", "foo", "bar" ]
[ "bb.fig", "bar" ]
A=1 B=2
A=3 B=4
OK
=!EXPECTEND!=
*/
