

function test() {
    try {
        throw('abc');
    } finally {
    
    }
    return 0;
};

var a, n;
try {
    for (a = 0; a < 100; ++a) {
        try {
            try {
                n = test();
            } catch(e) {
                print("catch:");
                print(e);
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
print(n);

/*
=!EXPECTSTART!=
catch:
abc
final
shot
2
2th final
ff
fock
undefined
=!EXPECTEND!=
*/
