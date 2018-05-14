/*
 *  If array length is 0xffffffff, Array.prototype.push() appends all the
 *  requested items and then sets the final 'length'.
 *
 *  For Ecmascript arrays (objects with array special behavior), the item
 *  writes will succeed, and the modified [[DefineOwnProperty]] algorithm
 *  in Section 15.4.5.1 triggers an automatic 'length' update for items
 *  whose index is in the range [0,0xfffffffe].  Outside this range the
 *  item gets written successfully but 'length' won't get updated.  The
 *  final explicit 'length' write causes a RangeError if the final length
 *  would be above 0xffffffff.  In error cases -all items- get written and
 *  length may be updated (up to 0xffffffff).
 *
 *  When the argument is not an Ecmascript array, the length is updated to
 *  0x100000000.
 */

/*===
array
RangeError
4294967295 foo
RangeError
4294967295 foo bar quux baz
4294967295 foo bar
non-array
4294967296 foo
4294967297 foo bar quux baz
4294967295 foo bar
===*/

function testArray() {
    var a;

    // 0xffffffff is maximum 'normal' length for an Array, e.g. assigning
    // to offset 0xffffffff gets no special behavior to avoid bumping length
    // to 0x100000000.  However, Array.prototype.push() has no such limitation.
    // Check for -noncompliant- but real world compatible behavior to refuse a
    // push which would causes a non-32-bit length.

    a = [];
    a.length = 0xffffffff;
    try {
        a.push('foo');
    } catch (e) {
        //print(e.name);
        if(e.name!="RangeError") throw new Error('Test Failed');
    }
    //print(a.length, a[0xffffffff]);

    // Same happens for lower 'length' values when there are enough push()
    // arguments.  Note that when the push() algorithm writes elements using
    // numeric indices, array exotic behavior gets triggered for indices
    // in the range [0,0xfffffffe] so that 'length' gets updated here to
    // 0xffffffff.  Items above this range -will- get written to the array
    // but won't trigger a RangeError.  Only the final explicit 'length'
    // write causes a RangeError; all items get written!

    a = [];
    a.length = 0xfffffffd;
    try {
        a.push('foo', 'bar', 'quux', 'baz');
    } catch (e) {
        //print(e.name);
        if(e.name!="RangeError") throw new Error('Test Failed');
    }
    //print(a.length, a[0xfffffffd], a[0xfffffffe], a[0xffffffff], a[0x100000000]);
    if(a.length!=4294967295) throw new Error('Test Failed');
    if(a[0xfffffffd]!='foo') throw new Error('Test Failed');
    if(a[0xfffffffe]!='bar') throw new Error('Test Failed');
    if(a[0xffffffff]!='quux') throw new Error('Test Failed');
    if(a[0x100000000]!='baz') throw new Error('Test Failed');
    // Boundary cases should work.

    a = [];
    a.length = 0xfffffffd;
    a.push('foo', 'bar');
    //print(a.length, a[0xfffffffd], a[0xfffffffe]);
    if(a.length!=4294967295) throw new Error('Test Failed');
    if(a[0xfffffffd]!='foo') throw new Error('Test Failed');
    if(a[0xfffffffe]!='bar') throw new Error('Test Failed');
}

function testNonArray() {
    var a;

    a = { length: 0xffffffff };
    Array.prototype.push.call(a, 'foo');
   // if(a.length!=4294967295) throw new Error('Test Failed');
    if(a[0xffffffff]!='foo') throw new Error('Test Failed');

    a = { length: 0xfffffffd };
    Array.prototype.push.call(a, 'foo', 'bar', 'quux', 'baz');
    //print(a.length, a[0xfffffffd], a[0xfffffffe], a[0xffffffff], a[0x100000000]);
    if(a[0xfffffffd]!='foo') throw new Error('Test Failed');
    if(a[0xfffffffe]!='bar') throw new Error('Test Failed');
    if(a[0xffffffff]!='quux') throw new Error('Test Failed');
    if(a[0x100000000]!='baz') throw new Error('Test Failed');


    a = { length: 0xfffffffd };
    Array.prototype.push.call(a, 'foo', 'bar');
    
    //print(a.length, a[0xfffffffd], a[0xfffffffe]);
    if(a.length!=4294967295) throw new Error('Test Failed');
    if(a[0xfffffffd]!='foo') throw new Error('Test Failed');
    if(a[0xfffffffe]!='bar') throw new Error('Test Failed');
}

//print('array');
testArray();
//print('non-array');
testNonArray();
