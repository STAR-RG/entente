

for(var i = 0; i < 100; ++i) {
    switch(i) {
        case 10:
            print("10");
        case 20:
            print("20");
        case 30:
            print("30");
            break;
        case 40: {
            continue;
            print("40");
        }
        break;
        case 41: break;
        case 50:
            for (var j = 0; j < 10; ++j) {
                if (j < 5) continue;
                if (j > 6) break;
            }
            print(j);
            break;
        default:
            break;
    }
    if (i == 40) print("hehe");
}

/*
=!EXPECTSTART!=
10
20
30
20
30
30
7
=!EXPECTEND!=
*/
