/*===
true
true
true
true
true
true
true
bar
===*/

function test() {
    // Error constructor inheritance chains were changed in ES2015.
    // E.g. TypeError constructor internal prototype is the Error
    // constructor rather than Function.prototype directly.

    //print(Object.getPrototypeOf(Error) === Function.prototype);
    if((Object.getPrototypeOf(Error) === Function.prototype) != true) throw new Error('Test Failed');
    //print(Object.getPrototypeOf(EvalError) === Error);
    if((Object.getPrototypeOf(EvalError) === Error) != true) throw new Error('Test Failed');
    //print(Object.getPrototypeOf(RangeError) === Error);
    if((Object.getPrototypeOf(RangeError) === Error) != true) throw new Error('Test Failed');
    //print(Object.getPrototypeOf(ReferenceError) === Error);
    if((Object.getPrototypeOf(ReferenceError) === Error)!=true) throw new Error('Test Failed');
    //print(Object.getPrototypeOf(SyntaxError) === Error);
    if((Object.getPrototypeOf(SyntaxError) === Error) != true) throw new Error('Test Failed');
    //print(Object.getPrototypeOf(TypeError) === Error);
    if((Object.getPrototypeOf(TypeError) === Error)!=true) throw new Error('Test Failed');
    //print(Object.getPrototypeOf(URIError) === Error);
    if((Object.getPrototypeOf(URIError) === Error)!=true) throw new Error('Test Failed');

    // Demonstrate using an actual inherited property access.
    Error.foo = 'bar';
    //print(RangeError.foo);
    if(RangeError.foo != 'bar') throw new Error('Test Failed');
}

try {
    test();
} catch (e) {
    //print(e.name);
}
