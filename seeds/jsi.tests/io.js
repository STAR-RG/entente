

var rc = 0;
var fp;
if (console.args.length < 1) {
    print("Usage: jsi io.ss <filename>");
    exit(0);
}

try {
    fp = new Channel(console.args[0], "r");
    while ((line = fp.gets()) != undefined) {
        print(line);
    }
    
    fp.close();
}
catch (e) {
    print("Can not open file: " + console.args[0]);
}
exit(rc);

/*
=!ARGSTART!=
g 2 3
=!ARGEND!=

=!EXPECTSTART!=
Can not open file: g
=!EXPECTEND!=
*/

