

// Simple test script for the debugger.
function foo2() {
  debugger;
}

function foo1() {
  var x = 99;
  foo2();
}

function foo() {
  var x = 88;
  foo1();
}

foo();

/*
=!EXPECTSTART!=
=!EXPECTEND!=
*/
