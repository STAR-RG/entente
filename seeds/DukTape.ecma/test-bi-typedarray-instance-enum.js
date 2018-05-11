/*
 *  Enumerating a TypedArray instance
 */

/*---
{
    "custom": true
}
---*/

/*===
for-in: 0
for-in: 1
for-in: 2
for-in: 3
for-in: 4
for-in: 5
for-in: 6
for-in: 7
Object.keys: 0
Object.keys: 1
Object.keys: 2
Object.keys: 3
Object.keys: 4
Object.keys: 5
Object.keys: 6
Object.keys: 7
Object.getOwnPropertyNames: 0
Object.getOwnPropertyNames: 1
Object.getOwnPropertyNames: 2
Object.getOwnPropertyNames: 3
Object.getOwnPropertyNames: 4
Object.getOwnPropertyNames: 5
Object.getOwnPropertyNames: 6
Object.getOwnPropertyNames: 7
Object.getOwnPropertyNames: length
===*/

/* Test enum with one non-8-bit view. */

function typedArrayEnumTest() {
    var buf = new ArrayBuffer(64);
    var view = new Uint32Array(buf, 4, 8);

    for (var k in view) {
        print('for-in:', k);
    }

    Object.keys(view).forEach(function (k) {
        print('Object.keys:', k);
    });

    Object.getOwnPropertyNames(view).forEach(function (k) {
        print('Object.getOwnPropertyNames:', k);
    });
}

try {
    typedArrayEnumTest();
} catch (e) {
    print(e.stack || e);
}
