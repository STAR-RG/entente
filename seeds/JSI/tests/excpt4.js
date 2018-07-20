

var a;
try {
for (a = 0; a < 100; ++a) {
    try {
        try {
            throw(1);
        } catch(e) {
            print("catch");
            continue;
        } finally {
            print("final");
            throw(2);
        }
    } catch(f) {
        print("shot");
        print(f);
        throw('ff');
    } finally {
        print("2th final");
    }
}
} catch(x) {
    print(x);
}
print("fock");

/*
=!EXPECTSTART!=
catch
final
shot
2
2th final
ff
fock
=!EXPECTEND!=
*/
