

var A = " a b c ";
print(A.trim());
var B = ",.a b c,.";
print(B.trim(',.'));
print(B.trimLeft(',.'));
print(B.trimRight(',.'));

var a = 'a,b,c';
var b = a.split(',');
var c = b.join(',');
print(b);
print(c);

var d = '{ a: 1, b : [ 9, "dog", 11 ] }';
eval('var e = '+d+';');
//print(d.a);
print(e.a);

/*
=!EXPECTSTART!=
a b c
a b c
a b c,.
,.a b c
[ "a", "b", "c" ]
a,b,c
1
=!EXPECTEND!=
*/
