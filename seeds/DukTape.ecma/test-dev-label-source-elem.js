/*
 *  A labelled statement can only be followed by a statement, not a
 *  source element, even at the top level.  Concretely, a function
 *  declaration cannot follow a label, nor can an expression statement
 *  begin with 'function'.
 *
 *  This is the E5 standards compliant behavior.  However, this test
 *  case tests for the default Duktape behavior (modelled after V8):
 *  function declarations are allowed outside top level in non-strict
 *  mode, and are treated like ordinary function declarations.  In
 *  strict mode they are not allowed.
 */

/*---
{
    "nonstandard": true
}
---*/

/*===
try finished
SyntaxError
try finished
===*/

try {
    /* Function f2 declaration follows label which is not allowed.
     * Also, an expression statement  cannot begin (directly) with
     * 'function', so this should result in SyntaxError in a fully
     * compliant implementation.
     *
     * V8 allows this in non-strict mode (as function statement).
     * This is also Duktape behavior now (unless DUK_USE_NONSTD_FUNC_STMT
     * is disabled).
     */

    eval("function f1() { mylabel: function f2() {} }");
    print("try finished");
} catch (e) {
    print(e.name);
}

try {
    /* Strict mode should have no effect on this, but this test
     * illustrates V8 behavior (i.e. V8 gives a SyntaxError here
     * but only in strict mode).
     */
    eval("function f1() { 'use strict'; mylabel: function f2() {} }");
    print("try finished");
} catch (e) {
    print(e.name);
}

try {
    /* Here function f2 is a function expression, so it is OK. */
    eval("function f1() { mylabel: (function f2() {}) }");
    print("try finished");
} catch (e) {
    print(e.name);
}
