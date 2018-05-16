/*---
{
    "nonstandard": true
}
---*/

/*===
RangeError
RangeError
1900-01-01T00:00:00.000Z
===*/

/* Date.UTC() has implementation defined results when it is given less than
 * 2 arguments.
 *
 * V8 sets internal time value to NaN, i.e. behaves the same as if two
 * 'undefined' arguments were given.  Rhino, on the other hand, defaults
 * the values to zero (leading to year 1970 and January).
 *
 * Our current behavior matches V8, so test for this behavior.
 */

try {
    d = new Date(Date.UTC()).toISOString();
    //print(new Date(Date.UTC()).toISOString());
} catch (e) {
    //print(e.name);
    if(e.name!=="RangeError") throw new Error('Test Failed');
}

try {
    d = new Date(Date.UTC(0)).toISOString();
    //print(new Date(Date.UTC(0)).toISOString());
    if(d!=="1900-01-01T00:00:00.000Z") throw new Error('Test Failed');
} catch (e) {
    //print(e.name);
    if(e.name!=="RangeError") throw new Error('Test Failed');
}

try {
    //print(new Date(Date.UTC(0,0)).toISOString());
    if(d!=="1900-01-01T00:00:00.000Z") throw new Error('Test Failed');

} catch (e) {
    //print(e.name);
    if(e.name!=="ReferenceError") throw new Error('Test Failed');
}
