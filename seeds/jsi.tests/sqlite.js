

require('Sqlite');

var db = new Sqlite('/tmp/testsql.db',{maxStmts:1000, readonly:false});
//var db = new Sqlite('/tmp/testsql.db');

db.eval('drop table IF EXISTS foo;');
try {
  db.query('drop table foo;');
} catch(e) {
  //print("OK");
};

db.eval('drop table IF EXISTS foo; create table foo(a,b);');
//db.eval('drop table IF EXISTS foo; create table foo(a,b);');
var n = 0;
var x = 99;
while (n++ < 3) {
  db.query('insert into foo values(@x,@n);');
  x -= 4;

  //db.query('insert into foo values("x",' + n + ');');
}
db.query('select * from foo;', function (n) {
    print("B="+n.b + ", A="+n.a);
});

print(db.query('select * from foo;').toString());

db.query('select * from foo;');

var dbc = db.conf();
dbc.version=0;
print("CONF: "+dbc.toString());
db.profile(function(sql,time) { print("EXECING: "+sql); });

print(db.onecolumn('select a from foo where b == 2;'));
var s = {};
s.b = 2;

print(db.query('select * from foo;'));
print(db.query('select * from foo;',{mode:'list'}));
print(db.query('select * from foo;',{mode:'list',headers:true}));
print(db.query('select * from foo;',{mode:'html'}));
print(db.query('select * from foo;',{mode:'html',headers:true}));
print(db.query('select * from foo;',{mode:'csv'}));
print(db.query('select * from foo;',{mode:'csv',headers:true}));
print(db.query('select * from foo;',{mode:'column'}));
print(db.query('select * from foo;',{mode:'column',headers:true}));
print(x=db.query('select * from foo;',{mode:'json'}));
JSON.parse(x);
print(x=db.query('select * from foo;',{mode:'json',headers:true}));
JSON.parse(x);
print(x=db.query('select * from foo;',{mode:'json2'}));
JSON.parse(x);
print(db.query('select * from foo;',{mode:'tabs'}));
print(db.query('select * from foo;',{mode:'tabs',headers:true}));
print(db.query('select * from foo;',{mode:'line'}));
print(db.query('select * from foo;',{mode:'insert'}));

var binds = [91,3];
db.query('insert into foo values(?,?);', {varName:'binds'});
db.query('insert into foo values(?,?);', {values:binds});
db.query('insert into foo values(?,?);', {values:[91,3]});

db.func('bar',function(n) { return n+'.000'; });


db.trace(function(sql) { print("TRACING: "+sql); });
print(db.onecolumn('select bar(a) from foo where b == 2;'));
print(db.trace());

//print(db.version());
delete db;


/*
var res1 = db.query('select * from table foo(a,b);');
for (i in res1) {
  print("CONS: "+i.toString()); 
}


var curs, n;
for (curs = db.query('select * from table foo(a,b);'),
    (n = db.getresult(curs))!=undefined,
    db.nextresult(curs)) {
    print(n.toString());
}
db.endresult(curs);


*/

/*
=!EXPECTSTART!=
B=1, A=99
B=2, A=95
B=3, A=91
[ { a:99, b:1 }, { a:95, b:2 }, { a:91, b:3 } ]
CONF: { bindWarn:false, debug:[], errorCnt:0, forceInt:false, maxStmts:1000, mutex:"default", name:"", nocreate:false, numSort:0, numStep:2, numStmts:2, queryOpts:{ callback:null, cdata:null, headers:false, limit:0, mapundef:false, mode:"rows", nocache:false, nullvalue:null, separator:null, table:null, typeCheck:"convert", values:null, varName:null, width:undefined }, readonly:false, version:0, vfs:null }
EXECING: select a from foo where b == 2;
95
EXECING: select * from foo;
[ { a:99, b:1 }, { a:95, b:2 }, { a:91, b:3 } ]
EXECING: select * from foo;
99|1
95|2
91|3
EXECING: select * from foo;
a|b
99|1
95|2
91|3
EXECING: select * from foo;
<TR><TD>99</TD><TD>1</TD></TR>
<TR><TD>95</TD><TD>2</TD></TR>
<TR><TD>91</TD><TD>3</TD></TR>
EXECING: select * from foo;
<TR><TH>a</TH><TH>b</TH></TR>
<TR><TD>99</TD><TD>1</TD></TR>
<TR><TD>95</TD><TD>2</TD></TR>
<TR><TD>91</TD><TD>3</TD></TR>
EXECING: select * from foo;
99,1
95,2
91,3
EXECING: select * from foo;
a,b
99,1
95,2
91,3
EXECING: select * from foo;
a          b          99         1         
95         2         
91         3         
EXECING: select * from foo;
a          b           
---------- ----------
99         1         
95         2         
91         3         
EXECING: select * from foo;
[ {"a":99, "b":1}, {"a":95, "b":2}, {"a":91, "b":3} ]
EXECING: select * from foo;
[ ["a", "b"], [99, 1], [95, 2], [91, 3] ]
EXECING: select * from foo;
{ "names": [ "a", "b" ], "values": [ [99, 1 ], [95, 2 ], [91, 3 ] ] } 
EXECING: select * from foo;
99	1
95	2
91	3
EXECING: select * from foo;
a	b
99	1
95	2
91	3
EXECING: select * from foo;
    a = 99    b = 1
    a = 95
    b = 2
    a = 91
    b = 3
EXECING: select * from foo;
INSERT INTO table VALUES(99,NULL);
INSERT INTO table VALUES(95,NULL);
INSERT INTO table VALUES(91,NULL);
EXECING: insert into foo values(?,?);
EXECING: insert into foo values(?,?);
EXECING: insert into foo values(?,?);
TRACING: select bar(a) from foo where b == 2;
EXECING: select bar(a) from foo where b == 2;
95.000
"function (sql) {...}"
=!EXPECTEND!=
*/

