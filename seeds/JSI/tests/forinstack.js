

var a = {a:1, b:2};

try {
for (var n in a) {
    try {
        switch(n) {
            case "a":
                print("A");
                continue;
            case "b":
                print("B");
                throw("ex");
        }
    } catch(e) {
        print(e);
        throw(e);
    } finally {
        print("fin");
        throw("fock");
    }
}

} catch (e) {
    print(e);
}

/*
=!EXPECTSTART!=
A
fin
fock
=!EXPECTEND!=
*/
