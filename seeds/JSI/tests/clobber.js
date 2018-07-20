

// Run with "jsish -ImemDebug 2 clobber" to see mem leak.
function foo() {
  var noOp = noOp();
}
try { foo(); } catch(e) {}
try { foo(); } catch(e) {}

/*
=!EXPECTSTART!=
=!EXPECTEND!=
*/
