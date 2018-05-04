

print(console.args.length);
print(console.args);

var i;
for (i = 0; i < console.args.length; ++i) {
    print ("argv[" + i + "] = " + console.args[i]);
}



// Memory leak to to argument alias.
function foo() {
  var args = arguments;
  for (i=0; i<args.length; i++)
    print(args[i]);
}
foo(1,2,3,4);


/*
=!ARGSTART!=
g 2 3
=!ARGEND!=

=!EXPECTSTART!=
3
[ "g", "2", "3" ]
argv[0] = g
argv[1] = 2
argv[2] = 3
1
2
3
4
=!EXPECTEND!=
*/
