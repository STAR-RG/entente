

var x = '{"type":"", "label":"editTran", "data" : [6,2961]}';
var x2 = '{"type":"", "label":"editTran", data : [6,2961]}';
print(JSON.check(x,false));
print(JSON.check(x));
print(JSON.check(x2,false));
print(JSON.check(x2));
print(JSON.parse(x, false));
print(JSON.parse(x));

print(JSON.parse(x2, false));
try { print(JSON.parse(x2)); } catch(e) { print(e); }
var dat = { able:1, baker:undefined };
print(JSON.stringify(dat));

var x = JSON.parse('["A\\u0020B",1]');
print(x.toString());

JSON.parse('{ "Columns": [ 1, 2], "A" : 1 }');
var x = JSON.parse('{ "Columns": [ 1, 2, {"A\u0020B":1, "B":[2,3]}, 2], "A" : 1 }');
print(x.toString());

/*
=!EXPECTSTART!=
true
true
true
false
{ data:[ 6, 2961 ], label:"editTran", type:"" }
{ data:[ 6, 2961 ], label:"editTran", type:"" }
{ data:[ 6, 2961 ], label:"editTran", type:"" }
JSON parse error (unexpected char in strict mode) at offset 32 "data : [6,2961]}"
{ "able":1 }
[ "A B", 1 ]
{ A:1, Columns:[ 1, 2, { Au0020B:1, B:[ 2, 3 ] }, 2 ] }
=!EXPECTEND!=
*/
