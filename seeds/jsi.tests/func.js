

function a(n) {
    var sum = 0;
    for (var i = 0; i < n; i++) {
        sum = sum + i;
    }
    return sum;
};

print(a(10));
print(a(100));

/*
=!EXPECTSTART!=
45
4950
=!EXPECTEND!=
*/

