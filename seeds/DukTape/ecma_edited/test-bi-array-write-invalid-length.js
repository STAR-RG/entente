/*
 *  Attempt to write a value outside unsigned 32-bit range to an Array's
 *  'length' property is a RangeError.
 */

/*===
RangeError
0
4294967295
RangeError
0
RangeError
0
4294967295
RangeError
0
===*/

function test() {
    var a;

    // Write directly

    try {
        a = [];
        a.length = -1;
    } catch (e) {
        //print(e.name);
        if(e.name !== "RangeError") throw new Error('Test Failed');
    }
    //print(a.length);
    if(a.length!==0) throw new Error('Test Failed');

    try {
        a = [];
        a.length = 0xffffffff;  // valid
    } catch (e) {
        //print(e.name);
        if(e.name !== "RangeError") throw new Error('Test Failed');
    }
    //print(a.length);
    if(a.length !== 4294967295) throw new Error('Test Failed');

    try {
        a = [];
        a.length = 0xffffffff + 1;
    } catch (e) {
        //print(e.name);
        if(e.name !== "RangeError") throw new Error('Test Failed');
    }
    //print(a.length);
    if(a.length !== 0) throw new Error('Test Failed');

    // Write using defineProperty()

    try {
        a = [];
        Object.defineProperty(a, 'length', { value: -1 });
    } catch (e) {
        //print(e.name);
        if(e.name !== "RangeError") throw new Error('Test Failed');
    }
    //print(a.length);
    if(a.length !== 0) throw new Error('Test Failed');

    try {
        a = [];
        Object.defineProperty(a, 'length', { value: 0xffffffff });  // valid
    } catch (e) {
        //print(e.name);
        if(e.name !== "RangeError") throw new Error('Test Failed');
    }
    //print(a.length);
    if(a.length !== 4294967295) throw new Error('Test Failed');

    try {
        a = [];
        Object.defineProperty(a, 'length', { value: 0xffffffff + 1 });
    } catch (e) {
        //print(e.name);
        if(e.name !== "RangeError") throw new Error('Test Failed');
    }
    //print(a.length);
    if(a.length !== 0) throw new Error('Test Failed');
}

test();