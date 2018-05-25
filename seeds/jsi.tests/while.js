

var i = 0;
var result = 0; 
while (i<3) {
    var j = 0; 
    while (j<100) {
        var k = 0; 
        while (k<1000) {
            ++k; 
            ++result; 
        }
        ++j; 
    }
    ++i;
    print(i);
}
print(result);
print(j);
print(k);

/*
=!EXPECTSTART!=
1
2
3
300000
100
1000
=!EXPECTEND!=
*/
