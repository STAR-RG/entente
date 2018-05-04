

var a = new Array(1);

print(a);
a[1] = 2;
print(a);

print(a.push(1,2,3));
print(a.pop());
print(a.pop());
print(a.pop());
print(a.length);
print(a.pop());
print(a.pop());
print(a.pop());
print(a.pop());
print(a.length);

/*
=!EXPECTSTART!=
[ undefined ]
[ undefined, 2 ]
5
3
2
1
2
2
undefined
undefined
undefined
0
=!EXPECTEND!=
*/
