

function add(a, b) {
   add.invokeTimes++;
   return a + b;
};


add.invokeTimes = 0;
add(1, 1);
add(2, 3);
print(add.invokeTimes); // 2

/*
=!EXPECTSTART!=
2
=!EXPECTEND!=
*/
