

var x = 9; 
var module = {
  x: 81,
    getX: function() { return this.x; }
};

print(module.getX()); // 81

var getX = module.getX;
print(getX()); // 9, because in this case, "this" refers to the global object

// create a new function with 'this' bound to module
var boundGetX = getX.bind(module);
print(boundGetX()); // 81


// Example showing binding some parameters
var sum = function(a, b) {
  return a + b;
};

var add5 = sum.bind(null, 5);
print(add5(10));
print(add5(10));
print(sum(5,10));
add5 = sum.bind(null, 6);
print(add5(10));
add5 = sum.bind(null);
print(add5(10,12));
add5 = sum.bind();
print(add5(10,11));
var nn = noOp.bind(null,99);
nn(10);
var pp = print.bind(null,'XX');
pp('HI');

/*
=!EXPECTSTART!=
81
9
81
15
15
15
16
22
21
XX HI
=!EXPECTEND!=
*/
