

var a = exec('ls -d /tmp');
print("A="+a);
var b = exec('ls -d /tmp',{noTrim:true});
print("B="+b);
var c = exec('gobbledeygook', null);
print("C="+c);
var d = exec('gobbledeygook', {retCode:true});
print("D="+d);
var e = exec('gobbledeygook 2>&1', {retAll:true});
print("E="+e.toString());
var f = exec('grep -q bakker', {input:"able\nbaker\ncharlie\n"});
print("F="+f);
var g = exec('grep baker', "able\nbaker\ncharlie\n");
print("G="+g);
var h = exec('ls /tmp', {retCode:true});
print("H="+h);
var i = exec('sleep 1&');
print("I="+i);
var j = exec('sleep 1', {bg:true});
print("J="+j);

/*
=!EXPECTSTART!=
baker
A=/tmp
B=/tmp

C=
D=127
E={ code:127, data:"sh: 1: gobbledeygook: not found", status:0 }
F=1
G=0
H=0
I=0
J=0
=!EXPECTEND!=
*/
