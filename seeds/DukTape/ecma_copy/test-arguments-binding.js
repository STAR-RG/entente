/*
 *  Some 'arguments' binding tests
 */

/*===
object
number
object
false
object
===*/

/* A non-strict 'arguments' binding is writable but not deletable. */

function arguments_write() {
    if ((typeof arguments) !== 'object') throw new Error('Test failed')
    arguments = 1;
    if ((typeof arguments) !== 'number') throw new Error('Test failed')
    
}

function arguments_delete() {
    if ((typeof arguments) !== 'object') throw new Error('Test failed')
    if ((delete arguments) !== false) throw new Error('Test failed')
    if ((typeof arguments) !== 'object') throw new Error('Test failed')
}

arguments_write();

arguments_delete();

/*===
SyntaxError
SyntaxError
===*/

/* A strict 'arguments' binding is immutable.  It cannot be deleted nor can
 * it be assigned to; doing so would be a SyntaxError.
 *
 * XXX: how to test that the binding is actually immutable, as it is a
 * SyntaxError trying to delete it or assign to it?  Even an eval() call
 * does not work: the eval will be parsed in strict mode too.
 */

try {
    eval("function arguments_strict_delete() { 'use strict'; delete arguments; }");
} catch (e) {
    if ((e.name) !== 'SyntaxError') throw new Error('Test failed')
}

try {
    eval("function arguments_strict_delete() { 'use strict'; arguments = 1; }");
} catch (e) {
    if ((e.name) !== 'SyntaxError') throw new Error('Test failed')
}
