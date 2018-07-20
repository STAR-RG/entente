

print(parseFloat(2400));
print(parseFloat('2400'));
print(1.2 + "12.3");
print(parseFloat('xx'));
print(parseFloat('99'));
print(parseInt('xx'));
print(parseInt('99'));
print(parseInt('99.9'));
print(parseInt('01001',2));
print(parseInt('0x16',16));
print(parseInt('0x16'));
print(parseInt('16',8));
print(parseInt('016'));

/*
=!EXPECTSTART!=
2400
2400
1.212.3
NaN
99
NaN
99
99
9
22
22
14
14
=!EXPECTEND!=
*/
