// This file was procedurally generated from the following sources:
// - src/declarations/redeclare-with-async-function-declaration.case
// - src/declarations/redeclare/block-attempt-to-redeclare-async-function-declaration.template
/*---
description: redeclaration with AsyncFunctionDeclaration (AsyncFunctionDeclaration in BlockStatement)
esid: sec-block-static-semantics-early-errors
features: [async-functions]
flags: [generated]
negative:
  phase: parse
  type: SyntaxError
info: |
    Block : { StatementList }

    It is a Syntax Error if the LexicallyDeclaredNames of StatementList contains
    any duplicate entries.

---*/


// throw "Test262: This statement should not be evaluated.";

{ async function f() {} async function f() {} }
