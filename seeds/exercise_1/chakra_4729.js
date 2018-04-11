// Found by Davino Junior
// https://github.com/Microsoft/ChakraCore/issues/4729

// Simple obj (could be anything)
function Foo() {}

// Proxy from target 'Foo' 
class Bar extends new Proxy(Foo, {}) { foobar() { return "foobar"; } }

if(new Bar().foobar == 'undefined'){
    throw new Error("Should be foobar, but is 'undefined'");
}