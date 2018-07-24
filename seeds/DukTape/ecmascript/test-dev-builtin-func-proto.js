/*
 *  Built-in functions internal prototype is required to be the initial
 *  Function.prototype.  This prevents Duktape/C functions from having
 *  an intermediate prototype providing a virtual 'length', at least for
 *  built-in functions.
 */

/*===
true
===*/

try {
    print(Object.getPrototypeOf(Math.cos) === Function.prototype);
} catch (e) {
    print(e);
}
