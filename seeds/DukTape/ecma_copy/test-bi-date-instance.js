/*===
[object Date]
===*/

// Date instance [[Class]] is "Date"

var d = new Date();
//print(Object.prototype.toString.call(d));
if(Object.prototype.toString.call(d) !== "[object Date]") throw new Error('Test Failed');