assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// test for ternary

result = (true?3:4)==3 && (false?5:6)==6;
assert(result);
