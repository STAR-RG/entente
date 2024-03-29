// This file was procedurally generated from the following sources:
// - src/async-generators/yield-as-binding-identifier-escaped.case
// - src/async-generators/syntax/async-declaration.template
/*---
description: yield is a reserved keyword within generator function bodies and may not be used as a binding identifier. (Async generator Function declaration)
esid: prod-AsyncGeneratorDeclaration
features: [async-iteration]
flags: [generated]
negative:
  phase: parse
  type: SyntaxError
info: |
    Async Generator Function Definitions

    AsyncGeneratorDeclaration:
      async [no LineTerminator here] function * BindingIdentifier ( FormalParameters ) {
        AsyncGeneratorBody }


    BindingIdentifier : Identifier

    It is a Syntax Error if this production has a [Yield] parameter and
    StringValue of Identifier is "yield".

---*/
// throw "Test262: This statement should not be evaluated.";


async function *gen() {
  var yi\u0065ld;
}
