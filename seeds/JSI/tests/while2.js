

var result =0; // Test for profile and code coverage.
function cc() {
    var i = 0;
    if (0) {
        i++;
        i++;
        i++;
        i++;
    }
    i++;
    i++;
    if (0) {
        i++;
        i++;
        i++;
        i++;
        i++;
    }
    return 1;
}

function bb() {
    return 1;
}

function aa() {

    function foo() {
        var i = 0;
        result++;
        while (i<3) {
            var j = 0; 
            while (j<10) {
                var k = 0; 
                ++j; 
                Info.funcs();
                result++;
            }
            ++i;
        }
    }
    
    function bar() {
        var i =0, k = 0;
        while (i<10000)  {
           foo();
           i++;
           k += i;
        }
        if (i<1) {
            print("missed");
            print("missed");
        }
    }
    
    bar();
}
cc();
aa();

print(result);
//print(j);
//print(k);

/*
=!EXPECTSTART!=
310000
=!EXPECTEND!=
*/
