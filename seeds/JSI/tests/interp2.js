

var ii = new Interp();
print(Info.named('Interp'));
print (ii.eval('3+4'));
ii.eval('exit(0)');
delete ii;


var ii = new Interp({isSafe:true, safeWriteDirs:['/tmp'], safeReadDirs:['/tmp']});
ii.eval("File.write('/tmp/xx.txt','hi');");
try {
  ii.eval("File.write('~/xx.txt','bye');");
} catch (e) {
  print(e);
}
delete ii;


var ii = new Interp({noSubInterps:true});
try {
  ii.eval("new Interp()");
} catch (e) {
    print(e);
}
delete ii;

/*
=!EXPECTSTART!=
[ "#Interp_1" ]
7
write access denied
subinterps disallowed
=!EXPECTEND!=
*/


