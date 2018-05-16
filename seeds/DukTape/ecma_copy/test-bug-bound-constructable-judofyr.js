/*
 *  Bug reported by http://www.reddit.com/user/judofyr:
 *
 *  This raises an error (because the bound function is not constructable).
 *  According to MDC this should work:
 *
 *    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#Bound_functions_used_as_constructors
 *
 *  (and I believe there's code out there that depends on it).
 */

/*===
object
1
===*/

function Thing(value) {
    if ((typeof this) !== 'object') throw new Error('Test Failed');
    this.value = value;
}

function test() {
    one = Thing.bind(null, 1);
    var obj = new one;
    if(obj.value !== 1) throw new Error('Test failed');
}

test();