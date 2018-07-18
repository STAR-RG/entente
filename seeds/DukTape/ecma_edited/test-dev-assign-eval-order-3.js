/*
 *  Comma expression as LHS.
 */

/*===
2
0
===*/

function test() {
    var a = [];
    var b = [];
    var a_orig = a;
    var b_orig = b;

    /* Assignment must go to a_orig */
    (b = a), b[1] = 123;

    if((a_orig.length) !== 2) throw new Error('Test Failed')
    if((b_orig.length) !== 0) throw new Error('Test Failed')
}

test();
