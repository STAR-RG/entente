

var i = 0;
do {
        if (i < 20) continue;
        print(i);
        if (i > 25) break;
        i++;
} while (++i < 30);


/*
=!EXPECTSTART!=
20
22
24
26
=!EXPECTEND!=
*/
