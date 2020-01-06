{
   function f() {
      return "first declaration";
   }
}
switch (1)
{
  case /0.0/gi:
    function f() {
       return "second declaration";
    }
}
assert.sameValue(typeof f
                ,"function");
assert.sameValue(f()
                ,"second declaration");