

function a() {
    print('in a');
};

function b() {
    print('in b');
};

var c = a;

c((c = b), 2);

/*
=!EXPECTSTART!=
in b
=!EXPECTEND!=
*/
