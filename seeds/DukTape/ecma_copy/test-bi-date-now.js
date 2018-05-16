/*===
object number
===*/

function dateNowTest() {
    var d1, d2;

    // these two are equivalent
    d1 = new Date();  // Date object
    d2 = Date.now();  // number
    if ((typeof d1) !== 'object') throw new Error('Test Failed')
    if ((typeof d2) !== 'number') throw new Error('Test Failed')
    }

dateNowTest();
