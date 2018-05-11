

var a = 1;
var b = 2;

function abc(a,b) {
    var c = a+b;
    var d = a * b;
    print(c);
    print(d);
    return d;
};
var x;
print(x = abc(5,6) + 100);

print(a);
print(b);
print(abc(3,4)+100);

print(x);

/*
=!EXPECTSTART!=
11
30
130
1
2
7
12
112
130
=!EXPECTEND!=
*/
