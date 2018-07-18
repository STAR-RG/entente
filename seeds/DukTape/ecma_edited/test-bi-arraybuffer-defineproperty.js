/*
 *  Duktape ArrayBuffer/view virtual properties don't work in
 *  Object.defineProperty().
 */

/*@include util-buffer.js@*/

/*---
{
    "custom": true
}
---*/

/*===
object 8 [object Uint8Array]
0
TypeError
0
object 8 [object Uint8Array]
===*/

function test() {
    var buf = new ArrayBuffer(8);
    var u8 = new Uint8Array(buf);
    //print(typeof u8, u8.length, String(u8));
    if(typeof u8 !== "object") throw new Error('Test Failed');
    if(u8.length !== 8) throw new Error('Test Failed');
    if(String(u8)!== [0,0,0,0,0,0,0,0]) throw new Error('Test Failed');

    //print(u8[4]);
    if(u8[4]!==0) throw new Error('Test Failed');

    try {
        Object.defineProperty(u8, '4', {
            value: 68
        });
    } catch (e) {
        // Duktape: TypeError: property is virtual
        // Node.js: TypeError: Cannot redefine a property of an object with external array elements
        
        //print(e.name);
        if(e.name!==TypeError) throw new Error('Test Failed');
    }
    //print(u8[4]);
    if(u8[4]!==68) throw new Error('Test Failed');

    //print(typeof u8, u8.length, String(u8));
    if(typeof u8 !== "object") throw new Error('Test Failed');
    if(u8.length !== 8) throw new Error('Test Failed');
    if(String(u8)!== [0,0,0,0,68,0,0,0]) throw new Error('Test Failed');
}

test();