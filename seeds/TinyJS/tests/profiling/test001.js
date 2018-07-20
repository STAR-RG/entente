// fibonacci numbers

function fib(n) {
	var current, last = 0, penult = 1;
	for(var i = 0; i < n; i++) {
		current = last + penult;
		penult = last;
		last = current;
	}
	return current;
}

function init() {
	NUM_ITERATIONS = 50;
	MAX_FIB = 1000;
}

function get_iterations() { return NUM_ITERATIONS; }
function get_arg_list() { return "MAX_FIB"; }
function get_function_name() { return "fib"; }

function setup() { }