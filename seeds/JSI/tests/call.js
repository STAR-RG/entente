

this.a = 1;
print(this);

function f(x, y, z) {
    var a = arguments[0] + arguments[1];
    print(this);
    print(x);
    print(y);
    print(z);
    print(a);
    var ff = function (a) {
        print(x);
        print(z);
        print(this);
    };
    return ff;
};

var fn = f(1, 2,3);

var fm = f.call({fock:32}, 4,5,6);

fn(456);
fm(789);

fn.call({fn:4}, 456);
fm.call({fm:8}, 55667);

/*
=!EXPECTSTART!=
{ Jsi_Auto:{}, a:1 }
{ Jsi_Auto:{}, a:1 }
1
2
3
3
{ fock:32 }
4
5
6
9
1
3
{ Jsi_Auto:{}, a:1 }
4
6
{ Jsi_Auto:{}, a:1 }
1
3
{ fn:4 }
4
6
{ fm:8 }
=!EXPECTEND!=
*/
