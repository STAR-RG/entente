

function a(x) {
    arguments[0] = 100; 
    print(x);
};

a(1);

/*
=!EXPECTSTART!=
100
=!EXPECTEND!=
*/
