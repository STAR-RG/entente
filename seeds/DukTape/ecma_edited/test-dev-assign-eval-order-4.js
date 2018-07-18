/*
 *  Assignment expression chain.
 */

/*===
["val01","abar","aquux"]
["val01","bbar","bquux"]
["val01","cbar","cquux"]
===*/

function test() {
    var a = [ 'afoo', 'abar', 'aquux' ];
    var b = [ 'bfoo', 'bbar', 'bquux' ];
    var c = [ 'cfoo', 'cbar', 'cquux' ];
    var a_orig = a;
    var b_orig = b;
    var c_orig = c;
    var i = 0;

    // All LHS "locations" are evaluated first, with i=0.

    a[i] = b[i] = c[i] = 'val' + (i++) + (i++);

    if((JSON.stringify(a)) !== '["val01","abar","aquux"]') throw new Error('Test Failed')
    if((JSON.stringify(b)) !== '["val01","bbar","bquux"]') throw new Error('Test Failed')
    if((JSON.stringify(c)) !== '["val01","cbar","cquux"]') throw new Error('Test Failed')
}

test();
