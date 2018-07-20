

this.name = 'TOP';

function a() {
    print(this.name);
};

function b(x, y) {
    a();
    print(this.name);
};

var n = { name: 'n', test: b };

n.test(1, 2);

/*
=!EXPECTSTART!=
TOP
n
=!EXPECTEND!=
*/
