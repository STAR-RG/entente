

var j = Util.base64('1234');
print(Util.base64(j, true) + ' ---> ' + j);

/*
=!EXPECTSTART!=
1234 ---> MTIzNA==
=!EXPECTEND!=
*/
