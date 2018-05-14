/*
 *  Development time bug caused by too lenient string-to-array-index
 *  conversion.
 */

/*===
quux
quux
===*/

try {
    var arr = [ 'foo', 'bar', 'quux', 'baz' ];
    //print(arr[2]);
    if((arr[2]) != 'quux') throw new Error('Test Failed')
    //print(arr['2']);
    if((arr['2']) != 'quux') throw new Error('Test Failed')
} catch (e) {
    print(e);
}
