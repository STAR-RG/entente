

this.top = 'top';

function a(a,b,c) {
    print(this);
    print(a);
    print(b);
    print(c);
};

a.apply({a:'a'});
a.apply({b:'b'}, [1,2]);
a.apply({c:'c'}, [1,2,3,4]);

/*
=!EXPECTSTART!=
{ a:"a" }
undefined
undefined
undefined
{ b:"b" }
1
2
undefined
{ c:"c" }
1
2
3
=!EXPECTEND!=
*/
