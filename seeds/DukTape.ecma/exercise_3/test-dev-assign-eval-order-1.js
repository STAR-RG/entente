/*
 *  http://forums.spheredev.org/index.php?topic=1218.0
 */

/*===
3
foo
bar
quux
undefined
===*/

function test() {
    var a = [ 'foo', 'bar', 'quux' ];
    var b = [];
    var i = 0, n = a.length;

    while (i < n) {
        /* In Duktape 1.0 and 1.1 this evaluates so that a[i++] is evaluated
         * first so an extra 'undefined' element appears at offset 0 with
         * result length 4.
         *
         * Rhino evaluates the left side first with result length 3.
         * V8 agrees.
         *
         * E5.1 Section 11.13.1 (Simple Assignment) seems to indicate Rhino
         * and V8 are right: "lref" is evaluated first (but of course not
         * written to).
         */
        b[i] = a[i++];
    }

    if((b.length) != 3) throw new Error('Test Failed')
    if((b[0]) != 'foo') throw new Error('Test Failed')
    if((b[1]) != 'bar') throw new Error('Test Failed')
    if((b[2]) != 'quux') throw new Error('Test Failed')
    if((b[3]) != undefined) throw new Error('Test Failed')
}

try {
    test();
} catch (e) {
    print(e.stack || e);
}
