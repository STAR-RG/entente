// Found by Mariana Moura
// https://github.com/Microsoft/ChakraCore/issues/3600

function foo(a = (() => b)(), b) {
}
foo();