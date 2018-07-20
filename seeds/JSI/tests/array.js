

var y = [ '2', '1' ];
var x = { '0': 'A', '1':'B' };
print(x[0]);
var a = new Array(5,4,3,2,1);
a.dog = 9;
print(a[0]);
var b = a.shift();
print("SHIFTED: "+b);
print(a[0]);
a[7] = -1;
a[8] = 'dog';
a.unshift('pig', 'cat', 99);
for (var i in a) { print(i+" = "+a[i]); }
print('A = '+a.join(','));
print("IDX = "+a.indexOf('dog'));
var s = a.slice(1,4);
print('S = '+ s.join(','));
print("SLICE0 = "+s[0]);
print("SLICE* = "+s.join(','));

var t = a.concat('SICK!!!',s);
print('T: '+t.join(','));


var z = new Array(5,4,3,2,1);
var za = z.splice(2,2,'A','B');
print('Z: '+z.join(',') + " ==> "+za.join(','));


//var q = new Array(5,4,2,3,1);
var q = new Array('Aaa','aAb','AAc','Bba','bBb');
var qq = q.sort();

print('Q: '+qq.join(','));

var t = [ 5, 4, 3, 2, 1] ;
function mysort(a,b) { return (a-b); }
print(t);
print(t.sort(mysort));

/*
=!EXPECTSTART!=
A
5
SHIFTED: 5
4
0 = pig
1 = cat
2 = 99
3 = 4
4 = 3
5 = 2
6 = 1
10 = -1
11 = dog
A = pig,cat,99,4,3,2,1,-1,dog
IDX = 11
S = cat,99,4,3
SLICE0 = cat
SLICE* = cat,99,4,3
T: pig,cat,99,4,3,2,1,-1,dog,SICK!!!,cat,99,4,3
Z: 5,4,A,B,1 ==> 3,2
Q: AAc,Aaa,Bba,aAb,bBb
[ 5, 4, 3, 2, 1 ]
[ 1, 2, 3, 4, 5 ]
=!EXPECTEND!=
*/
