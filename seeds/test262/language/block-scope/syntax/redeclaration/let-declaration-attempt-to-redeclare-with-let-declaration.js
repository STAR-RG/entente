// This file was procedurally generated from the following sources:
// - src/declarations/redeclare-with-let-declaration.case
// - src/declarations/redeclare/block-attempt-to-redeclare-let-declaration.template
/*---
description: redeclaration with let-LexicalDeclaration (LexicalDeclaration (let) in BlockStatement)
esid: sec-block-static-semantics-early-errors
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

{ let f; let f; }
