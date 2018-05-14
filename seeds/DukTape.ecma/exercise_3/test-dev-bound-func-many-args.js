/*===
65535
foo-0
foo-65535
undefined
undefined
===*/

function target() {
    if((arguments.length) != '65535') throw new Error('Test Failed')
    if((this) != 'foo-0') throw new Error('Test Failed')
    if((arguments[65534]) != 'foo-65535') throw new Error('Test Failed')
    if((arguments[65535]) != undefined) throw new Error('Test Failed')
    if((arguments[65536]) != undefined) throw new Error('Test Failed')
}

var args = [];
while (args.length < 65536) {
    args.push('foo-' + args.length);
}
var f = Function.prototype.bind.apply(target, args);
f();
