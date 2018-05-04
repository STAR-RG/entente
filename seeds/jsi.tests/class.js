

function Person(name, gender){

    this.name = name;
    this.gender = gender;
}

Person.prototype = { spake: function() { return print(this.name); } };
Person.prototype.speak = function(){ print("Howdy, my name is" + this.name); };


var person = new Person("Bob", "M");

person.speak();
person.spake();
print(typeof person);
print(person.hasOwnProperty('toString'));
print(person.hasOwnProperty('name'));

var y = [1,2,3];
var x = typeof(y);
print(x);
print(typeof((9)));

/*
=!EXPECTSTART!=
Howdy, my name isBob
Bob
object
false
true
array
number
=!EXPECTEND!=
*/
