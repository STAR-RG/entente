

var s = strftime(0);
print(strptime(s));
var s = strftime(0,{utc:true});
print(strptime(s,{utc:true}));
var t = strptime(s,{utc:true,fmt:"%c"});
print(strftime(t,{utc:true,fmt:"%Y-%m-%d"}));

/*
=!EXPECTSTART!=
0
0
1970-01-01
=!EXPECTEND!=
*/
