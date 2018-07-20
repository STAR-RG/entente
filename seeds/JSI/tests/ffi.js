

var a = {a: 1,b:2,c:3,d:4};
print(a.e);

print("================");
for(var s in a) { print(s + ":" + a[s]); }

a.shite = "fock";

print("================");
for(var s in a) { a.fock = "shite"; print(s + ":" + a[s]); }

print("================");
for(var s in a) { 
    print(s + ":" + a[s]);
    delete a.shite; 
}

/*
=!EXPECTSTART!=
undefined
================
a:1
b:2
c:3
d:4
================
a:1
b:2
c:3
d:4
shite:fock
================
a:1
b:2
c:3
d:4
fock:shite
=!EXPECTEND!=
*/
