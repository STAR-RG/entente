// This file was procedurally generated from the following sources:
// - src/async-functions/await-as-binding-identifier.case
// - src/async-functions/syntax/async-expression.template
/*---
description: await is a reserved keyword within generator function bodies and may not be used as a binding identifier. (Unnamed async function expression)
esid: prod-AsyncFunctionExpression
features: [async-functions]
flags: [generated]
negative:
  phase: parse
  type: SyntaxError
info: |
    Async Function Definitions

    AsyncFunctionExpression :
      async [no LineTerminator here] function ( FormalParameters ) { AsyncFunctionBody }


    BindingIdentifier : Identifier

    It is a Syntax Error if this production has a [Await] parameter and
    StringValue of Identifier is "await".

---*/
// throw "Test262: This statement should not be evaluated.";


var fn = async function () {
  var await;
};
