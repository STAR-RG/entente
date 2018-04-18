// Amanda Ferraz
// https://github.com/Microsoft/ChakraCore/issues/3407

function foo(a = function() {}){
	return a;
}

if(foo().name === ''){
	throw new Error("Should be a");
}
