

function Load() {
  print("LOAD");
  //delete Foo;
  Foo = function (a) { print("FOO: "+arguments.toString()); };
  print("DONE");
}

function Foo() {
  print("ORIG FOO: "+arguments.toString());
  Load();
  return Foo.apply(this,arguments);
}

var j = new Foo(99);

/*
=!EXPECTSTART!=
ORIG FOO: [ 99 ]
LOAD
DONE
FOO: [ 99 ]
=!EXPECTEND!=
*/
