var o = { f: "string-f" };
with (o) {
  var desc = Object.getOwnPropertyDescriptor(this, "f");
  assertEq(desc.value, undefined);
  function f() {
    return "fun-f";
  }
}
