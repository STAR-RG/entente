

var adder = function (x) {
    return function (y) {
        return x + y;
    };
};
var add5 = adder(5);
add5(1) == 6

/*
=!EXPECTSTART!=
true
=!EXPECTEND!=
*/
