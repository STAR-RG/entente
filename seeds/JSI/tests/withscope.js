

var  a = {
    b: {
        c: 1
    }
};

with (a.b) {
    c = 2;
        eval("var d = 4;");
}
print(a);
print(a.b.d);

/*
diff from ecma, var should make var in with

=!EXPECTSTART!=
{ b:{ c:2 } }
undefined
=!EXPECTEND!=

*/

