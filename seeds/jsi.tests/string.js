

var a = "the original string";

print(a.substr());
print(a.substr(1));
print(a.substr(-1, 1));

print(a.substr(2, -1));
print(a.substr(-5, 3));
print(a.substr(100, 0));
print(a.substr(10, 1));
print(a.substring(10, 11));

print(a.indexOf("ori"));
print(a.indexOf("swer"));
print(a.indexOf("i"));
print(a.indexOf("i", 9));
print(String.fromCharCode(65));
var s = 'abcdabcd';
print(s.charAt(3));
print(s.indexOf('cd'));
print(s.lastIndexOf('cd'));

var res = "There is a BLUE and white CAR by my BLUE HOUSE";
print(res.map(['BLUE','RED','HOUSE','SHACK' ])); //not standard.
print(res.map(['blue','Red','house','Shack' ], true));

/*
=!EXPECTSTART!=
the original string
he original string
g

tri

a
al
4
-1
6
16
A
d
2
6
There is a RED and white CAR by my RED SHACK
There is a Red and white CAR by my Red Shack
=!EXPECTEND!=
*/
