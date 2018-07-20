

print(Object.prototype);
print("     should be {}");

Object.prototype.a = 123;
//Object.prototype = 123;

print(Object.prototype);
print("     should be { a:123 }");

var a = { b:1, c:2 };
print(a.a);
print("     should be 123");
a.a = 'shot';
print(a.a);
print("     should be shot");

print(Object.prototype);
print("     should be { a:123 }");

Number.prototype.fock = function() {
    print(this / 2);
};

var x = 12;

x.fock();
print("     should be 6");

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

function Employee(name, sex, employeeID) {
    this.name = name;
    this.sex = sex;
    this.employeeID = employeeID;
};

Employee.prototype = new Person("defaultName", "defaultSex");
Employee.prototype.getEmployeeID = function() {
    return this.employeeID;
};

var zhang = new Employee("ZhangSan", "man", "1234");
print(zhang.getName()); // "ZhangSan
print(zhang.age);            //18
delete zhang.name;
print(zhang.name);       //defaultName

function f() {}
function g() {}
g.prototype = new f();
var h = new g();
print(g.prototype.isPrototypeOf(h));
print(g.prototype.isPrototypeOf(f));

/*
=!EXPECTSTART!=
{  }
     should be {}
{ a:123 }
     should be { a:123 }
123
     should be 123
shot
     should be shot
{ a:123 }
     should be { a:123 }
6
     should be 6
ZhangSan
18
defaultName
true
false
=!EXPECTEND!=
*/
