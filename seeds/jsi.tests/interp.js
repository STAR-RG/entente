

function foo(n) {
  print('foo');
};

foo(1);
eval('foo(1);');
var x1 = Info.interp();
eval('foo(1);');
var x2 = Info.interp();
print(x1.codeCacheHits+' '+x2.codeCacheHits);
print(x1.funcCallCnt+' '+x2.funcCallCnt);
print(x1.cmdCallCnt+' '+x2.cmdCallCnt);

/*
=!EXPECTSTART!=
foo
foo
foo
0 1
2 3
2 4
=!EXPECTEND!=
*/
