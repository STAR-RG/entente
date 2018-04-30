assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
// recursion
function a(x) { 
  if (x>1)
    return x*a(x-1);
  return 1;
}
result = a(5)==1*2*3*4*5;
assert(result);
