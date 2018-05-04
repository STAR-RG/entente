

//test void expr
print(void 1);

//test - expr
print(-1);
print(-0);
print(- true);
print(- "123" );

//wrong: should be NaN, not 0
print(- {a:1});

//test + expr
print(1 + 2);
print(1.3 + 2.3);
print(1.2 + "12.3");
print(4 + true);
print("2342" + true);
print({} + 12);

print("================");
print(1<<4);
print(1<<344.3);
print(2>>4);
print(-200000 >> -4);

print("===============");
print(1.0 < 2.3);
print(10000.456 < 10000.456);
print(10000.456 > 10000.456);
print(10000.456 <= 10000.456);
print(10000.456 >= 10000.456);
print("10000.456" < "10000.456");
print("10000.456" > "10000.456");
print("10000.456" <= "10000.456");
print("10000.456" >= "10000.456");
print("a" > "b");
print("a" >= "a");
print("a" < "aa");
print("a" < "b");
print("===============");
print(1 == 1);
print(2 == 1);
print("2" == 2);
print(true == null);
print("234234" == "234234");
print(true == 1);

print("===================");
print(1 === true);
print(1 === "1");
print("abc" === "abc");
print(3.1415926 === 3.1415926);

print("============");
print(1 | 2 | 4 | 8 | 16);
print(123 & 234);
print(3456 ^ 2342);

print("===============");
var a = 12;
a += 4;
print(a);
a -= 4;
print(a);
a /= 4;
print(a);
a *= 4;
print(a);
a %= 4;
print(a);
a <<= 4;
print(a);
a >>= 3;
print(a);
a += true;
print(a);
a += "fock";
print(a);

a = { a: 120 };
a.a += 4;
print(a);
a.a -= 4;
print(a);
a.a /= 4;
print(a);
a.a *= 4;
print(a);
a.a %= 4;
print(a);
a.a <<= 4;
print(a);
a.a >>= 3;
print(a);
a.a += true;
print(a);
a.a += "fock";
print(a);

Interp.conf({strict:false});
print(-NaN);
print(-Infinity);
print(NaN + NaN);
print(NaN + "NaN");
print(Infinity - Infinity);
print(NaN + 3);
print(NaN < NaN);
print(Infinity < -Infinity);
print(Infinity > -Infinity);
print(NaN == NaN);
print(NaN === NaN);

/*
=!EXPECTSTART!=
undefined
-1
0
-1
-123
0
3
3.6
1.212.3
5
2342true
12
================
16
16777216
0
-1
===============
true
false
false
true
true
false
false
true
true
false
true
true
true
===============
true
false
true
false
true
true
===================
false
false
true
true
============
31
106
1190
===============
16
12
3
12
0
0
0
1
1fock
{ a:124 }
{ a:120 }
{ a:30 }
{ a:120 }
{ a:0 }
{ a:0 }
{ a:0 }
{ a:1 }
{ a:"1fock" }
NaN
-Infinity
NaN
NaNNaN
NaN
NaN
undefined
false
true
false
false
=!EXPECTEND!=
*/
