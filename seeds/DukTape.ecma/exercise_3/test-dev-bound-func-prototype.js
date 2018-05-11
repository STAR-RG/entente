/*
 *  Bound function internal prototype is copied from the target in ES2015.
 *  In ES5 it is always Function.prototype.  Test for ES2015 behavior.
 */

/*===
bar
bar
true
quux
bar
false
===*/

function test() {
    var F = function foo() {};
    var proto = { foo: 'bar' };
    Object.setPrototypeOf(F, proto);

    // Create a bound function; its prototype is copied from the current
    // prototype of the target.
    var G = Function.prototype.bind.call(F);
    if((F.foo) != 'bar') throw new Error('Test Failed')
    if((G.foo) != 'bar') throw new Error('Test Failed')
    if((Object.getPrototypeOf(G) === proto) != true) throw new Error('Test Failed')

    // Alter target's internal prototype; doesn't affect the bound function.
    proto = { foo: 'quux' };
    Object.setPrototypeOf(F, proto);
    if((F.foo) != 'quux') throw new Error('Test Failed')
    if((G.foo) != 'bar') throw new Error('Test Failed')
    if((Object.getPrototypeOf(G) === proto) != false) throw new Error('Test Failed')
}

try {
    test();
} catch (e) {
    print(e.stack || e);
}
