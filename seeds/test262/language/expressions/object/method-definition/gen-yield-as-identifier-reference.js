// This file was procedurally generated from the following sources:
// - src/generators/yield-as-identifier-reference.case
// - src/generators/syntax/obj-method.template
/*---
description: yield is a reserved keyword within generator function bodies and may not be used as an identifier reference. (Generator method)
esid: prod-GeneratorMethod
features: [generators]
flags: [generated]
negative:
  phase: parse
  type: SyntaxError
info: |
    14.4 Generator Function Definitions

    GeneratorMethod[Yield, Await]:
      * PropertyName[?Yield, ?Await] ( UniqueFormalParameters[+Yield, ~Await] ) { GeneratorBody }


    IdentifierReference : Identifier

    It is a Syntax Error if this production has a [Yield] parameter and
    StringValue of Identifier is "yield".

---*/
// throw "Test262: This statement should not be evaluated.";

var obj = {
  *method() {
    void yield;
  }
};
