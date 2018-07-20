

print(format("%.03d", 9));
var me = 'Me', cnt = 9;
print(format('Help %s = %d', me, cnt));
print(format('%d %ld %hd %05.2f %-6i %*d %#9x', 99, 99, 99, 99, 99, 9, 9, 9))

/*
=!EXPECTSTART!=
009
Help Me = 9
99 99 99 99.00 99             9       0x9
=!EXPECTEND!=
*/
