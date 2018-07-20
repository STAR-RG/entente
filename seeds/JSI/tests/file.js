

var fn = Info.scriptDir()+'/filetest.txt';
try {
    var n, f = new Channel(fn);
    if (f) {
        while((n = f.gets())!=undefined) {
                print(n);
        }
    }
} catch(e) {
   print('Can not open '+fn);
}

/*
=!EXPECTSTART!=
Here is some random
Text.
=!EXPECTEND!=
*/
