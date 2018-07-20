// double function calls
function a(x) { return x+2; }
function b(x) { return a(x)+1; }
assert(a(3)==5 && b(3)==6);
