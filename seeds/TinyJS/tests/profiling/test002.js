// factorial

function factorial(n) {
	var total = 1;
	for(var i = 1; i <= n; i++) {
		total = total * i;
	}
	return total;
}

function init() {
	NUM_ITERATIONS = 50;
	MAX_FACT = 1000;
}

function get_iterations() { return NUM_ITERATIONS; }
function get_arg_list() { return "MAX_FACT"; }
function get_function_name() { return "factorial"; }

function setup() { }