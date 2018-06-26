/*
 *  Assignment eval order corner case
 *
 *  The RHS of an assignment may change the base variable of the LHS.  The
 *  write should go to the "original LHS".
 *
 *  In concrete terms, if the LHS is compiled into a property expression with
 *  a bound variable reference (register) as a base, and the variable is
 *  updated by the RHS, the write will go to the updated variable value.
 */

/*===
2
undefined
123
undefined
3
foo
bar
quux
true
===*/

function test() {
    var a = [];
    var b = [ 'foo', 'bar', 'quux' ];
    var orig_a = a;

    /* Because LHS is evaluated first, the write goes to the original 'a',
     * not 'a' after the assignment 'a = b'.
     */

    a[1] = ((a = b), 123);

    if((orig_a.length) !== 2) throw new Error('Test Failed')
    if((orig_a[0]) !== undefined) throw new Error('Test Failed')
    if((orig_a[1]) !== 123) throw new Error('Test Failed')
    if((orig_a[2]) !== undefined) throw new Error('Test Failed')

    if((b.length) !== 3) throw new Error('Test Failed')
    if((b[0]) !== 'foo') throw new Error('Test Failed')
    if((b[1]) !== 'bar') throw new Error('Test Failed')
    if((b[2]) !== 'quux') throw new Error('Test Failed')
    if((a==b) !== true) throw new Error('Test Failed')
}

test();