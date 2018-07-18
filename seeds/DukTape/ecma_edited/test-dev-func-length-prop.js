/*===
0
2
===*/

function f1() {}
function f2(x,y) {};

if((f1.length) !== '0') throw new Error('Test Failed')
if((f2.length) !== '2') throw new Error('Test Failed')
