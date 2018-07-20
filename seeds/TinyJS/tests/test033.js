// test for shift
var a = (2<<2);
var b = (16>>3);
var c = (-1 >>> 16);
assert(a==8 && b==2 && c == 0xFFFF);
