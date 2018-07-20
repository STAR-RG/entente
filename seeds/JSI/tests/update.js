

var i=0, j = 0, k = 0;
function foo() {
   i++,j++;
}
var id = setInterval(foo,100);
print(Event.names());
while (true) {
   if (k++<=3)
     print("UPDATE");
   if (i>5) { clearInterval(id); break; }
   Event.update(50);
}
print("FOO CALLED: "+j);
Event.update();

/*
=!EXPECTSTART!=
[ 0 ]
UPDATE
UPDATE
UPDATE
UPDATE
FOO CALLED: 6
=!EXPECTEND!=
*/
