// This file was procedurally generated from the following sources:
// - src/declarations/redeclare-with-let-declaration.case
// - src/declarations/redeclare/switch-attempt-to-redeclare-async-generator-declaration.template
/*---
description: redeclaration with let-LexicalDeclaration (AsyncGeneratorDeclaration in SwitchStatement)
esid: sec-switch-statement-static-semantics-early-errors
features: [async-iteration]
flags: [generated]
negative:
  phase: parse
  type: SyntaxError
info: |
    SwitchStatement : switch ( Expression ) CaseBlock

    It is a Syntax Error if the LexicallyDeclaredNames of CaseBlock contains any
    duplicate entries.

---*/


// throw "Test262: This statement should not be evaluated.";

switch (0) { case 1: async function* f() {} default: let f; }
