

for (var i = 0; i < 100; ++i) {
    try {
        if (i == 50) throw(1);
    } catch(e) {
        break;
    } finally {
        i++;
    }
}
print(i);

/*
=!EXPECTSTART!=
51
=!EXPECTEND!=
*/
