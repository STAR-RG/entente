

function Person(name, sex) {
   this.name = name;
   this.sex = sex;
};
Person.prototype = {
   getName: function() {
       return this.name;
   },
   getSex: function() {
       return this.sex;
   },
   age: 18
};
var zhang = new Person("ZhangSan", "man");
print(zhang.getName()); // "ZhangSan"
var chun = new Person("ChunHua", "woman");
print(chun.getName()); // "ChunHua"

print(zhang.age);        //18
zhang.age = 20;
print(zhang.age);        //20
delete zhang.age;
print(zhang.age);

/*
=!EXPECTSTART!=
ZhangSan
ChunHua
18
20
18
=!EXPECTEND!=
*/
