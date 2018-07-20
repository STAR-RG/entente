
"use nowith";

var a = {
    b: {
        c: 0
    },
    x: 0
};

for (var i = 0; i < 10; ++i) {
    try {
        print("try1");

        with(a.b) {
            c = i;
            try {
                if (i == 5) throw("shit");
            } catch (e) {
                print(e);
                with (a) {
                    x = 'shit';
                    throw("sadf");
                }
            } finally {
                print("finally2");
                throw("fock");
            }
        }
    } catch(e) {
        print(e);
        break;
    } finally {
        print("finally1");
    }
}

print(a);

/*
=!EXPECTSTART!=
try1
finally2
fock
finally1
{ b:{ c:0 }, x:0 }
=!EXPECTEND!=
*/
