

if (console.args.length < 1) {
    print("Usage: jsi grep.ss <PATTERN>");
    exit(-1);
}

var reg = new RegExp(console.args[0]);
var line = "";
while (1) {
    line = console.input();
    if (line == undefined) break;
    if (line.match(reg)) {
        print(line);
    }
}

/*
=!ARGSTART!=
g 2 3
=!ARGEND!=

=!INPUTSTART!=
input
test
abc@gmail.com

=!INPUTEND!=

=!EXPECTSTART!=
abc@gmail.com
=!EXPECTEND!=

*/
