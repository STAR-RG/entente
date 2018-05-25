

var a = ["a", "b", "c"];
a.forEach(function(entry) {
    print(entry);
});
a = a.reverse();
for (var i in a) {
    print(a[i]);
}
var b = a.filter(function(x) { return (x != 'b'); });
print(b);
var c = [];
for (var i in a) {
  var x = a[i];
  if (x != 'b') c.push(x);
}
print(c);

/*
=!EXPECTSTART!=
a
b
c
c
b
a
[ "c", "a" ]
[ "c", "a" ]
=!EXPECTEND!=
*/
