eval("if (false) function _f() {} else function f() { return \"second declaration\"; }");
{
   function f() {
      return "first declaration";
   }
}
assert.sameValue(typeof f
                ,"function");
assert.sameValue(f()
                ,"second declaration");