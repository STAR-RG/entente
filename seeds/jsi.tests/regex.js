#!/usr/local/bin/jsish -u -echo true %s

while (1) {
    print("input the email");
    var res, email = console.input();
    if (email == undefined) break;
    if ((res = email.match(/([a-zA-Z0-9]+)@([a-zA-Z0-9]+)\.com/))) {
        print("match at: " + res[0]);
        print("name: " + res[1]);
        print("domain: " + res[2]);
    } else {
        print("invalid email format",email,'.');
    }
}
print('####Replace');
var s = 'a b b c d b';
print(s.replace('b','c'));
print(s.replace(/b/g,'c'));
print(s.replace(/b/,'c'));
res="There is a blue and white car by my blue house".replace(/blue|house|car/gi, function(x){return x.toUpperCase();});
print(res);

var ins = "<<file.c>>!!fool.c!!";
res = ins.replace(/([[a-zA-Z0-9_]*)\.c/gi, 'cc -c $& -o $1.o');
print(res);

print('####Search');
var str="The rain in SPAIN stays mainly in the plain"; 
//print(str.search(/ain/gi));
print(str.search(/AIN/));
print(str.search('ain'));

print('####Match');
print(str.match(/ain/gi));
var s = 'pm@gm.com';
print(s.match(/^([a-z]*)@([a-z.]*)$/));
print(s.match(/^([t-z]*)@([a-z.]*)$/));

var r = new RegExp('gm');
print(s.match(r));

function reg(match,p1,p2,offset,str) {
  //print([match,p1,p2,offset,str].join(', '));
  print(arguments.join(', '));
  return '('+p2+','+p1+')';
}

var re=/^function=([a-z]+),([a-z]+)$/gm;
var s = 'S\nfunction=a,b\nA,B\nfunction=c,d\nE';
print('OUT='+s.replace(re,reg));

print('####Exec');
var r = /abc/g;
var x = 'a abc def abc';
while (s = r.exec(x))
    print(s);

/*
=!INPUTSTART!=
input
test
abc@gmail.com
=!INPUTEND!=
*/

/*
=!EXPECTSTART!=
input the email
invalid email format input .
input the email
invalid email format test .
input the email
match at: abc@gmail.com
name: abc
domain: gmail
input the email
####Replace
a c b c d b
a c c c d c
a c b c d b
There is a BLUE and white CAR by my BLUE HOUSE
<<cc -c file.c -o file.o>>!!cc -c fool.c -o fool.o!!
####Search
14
5
####Match
[ "ain", "AIN", "ain", "ain" ]
[ "pm@gm.com", "pm", "gm.com" ]
null
[ "gm" ]
function=a,b, a, b, 2, S
function=a,b
A,B
function=c,d
E
function=c,d, c, d, 19, S
function=a,b
A,B
function=c,d
E
OUT=S
(b,a)
A,B
(d,c)
E
####Exec
[ "abc" ]
[ "abc" ]
=!EXPECTEND!=
*/


