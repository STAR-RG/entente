

print(Number.toPrecision(9.1234,2));
print(Number.toExponential(9.1234,2));
print(Number.toFixed(9.1234,1));
var j = new Number(9.1234);
print(j.toPrecision(2));
print(j.toExponential(2));
print(j.toFixed(1));

var num = 15;
print(String.replace(num, /5/, '2'));

/*
=!EXPECTSTART!=
9.1
9.12e+0
9.1
9.1
9.12e+0
9.1
12
=!EXPECTEND!=
*/
