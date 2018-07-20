

var i = 0, b = 0;
i++;
try {
    try {
        b++;
        throw({a:1});
    } catch (b) {
        print("catch: b:" + b);
    } finally {
        print("finally: b:" + b);
        throw({b:2});
    }
} catch (b) {
    print(b);
} finally {
    print(b);
}

/*
=!EXPECTSTART!=
catch: b:[object Object]
finally: b:1
{ b:2 }
1
=!EXPECTEND!=
*/
