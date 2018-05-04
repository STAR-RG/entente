

var w = {a:1,b:2,c:3};
var x = [1,2,3];
var z = 2;
var k = (z in x);
print('K = '+k);
print(2 in x);
print(4 in x);
print('a' in w);
print('d' in w);



var a = {a: 1,b:2,c:3,d:4};
for(var s in a) { 
	print(s + ":" + a[s]);
	delete a.b; 
}

/*
=!EXPECTSTART!=
K = true
true
false
true
false
a:1
c:3
d:4
=!EXPECTEND!=
*/
