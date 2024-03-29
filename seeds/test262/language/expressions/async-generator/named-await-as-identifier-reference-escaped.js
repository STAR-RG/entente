// This file was procedurally generated from the following sources:
// - src/async-generators/await-as-identifier-reference-escaped.case
// - src/async-generators/syntax/async-expression-named.template
/*---
description: await is a reserved keyword within generator function bodies and may not be used as an identifier reference. (Named async generator expression)
esid: prod-AsyncGeneratorExpression
features: [async-iteration]
flags: [generated]
negative:
  phase: parse
  type: SyntaxError
info: |
    Async Generator Function Definitions

    AsyncGeneratorExpression :
      async [no LineTerminator here] function * BindingIdentifier ( FormalParameters ) {
        AsyncGeneratorBody }


    IdentifierReference : Identifier

    It is a Syntax Error if this production has a [Await] parameter and
    StringValue of Identifier is "await".

---*/
// throw "Test262: This statement should not be evaluated.";


var gen = async function *g() {
  void \u0061wait;
};
