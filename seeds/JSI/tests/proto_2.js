

function Cat(name){
    this.name = name;
};
Cat.prototype;
var garfield = new Cat('Garfield');
garfield.__proto__ === Cat.prototype;
Cat.prototype.greet = function(){
    print('Meow, I am ' + this.name);
};
garfield.greet();
var felix = new Cat('Felix');
felix.greet();
garfield.greet = function(){
    print("What's new?");
};
garfield.greet();
felix.greet();
function Animal(){
};
Cat.prototype = new Animal;
Cat.prototype.constructor = Cat;
Animal.prototype.breed = function(){
    print('Making a new animal!');
    return new this.constructor();
};
// TODO: Fails, but comment out next line and it passes, but leaks memory.
var kitty = garfield.breed();
function f(i,j) {}
function g() {}
g.prototype = new f();
var i = new f();
var h = new g();
print(g.prototype.isPrototypeOf(h));
print(g.prototype.isPrototypeOf(f));
print(i.constructor);
print(h.constructor);
print(h.constructor == f);
function Fee() {
    // . . .
}

function Fi() {
    // . . .
}
Fi.prototype = new Fee();

function Fo() {
    // . . .
}
Fo.prototype = new Fi();

function Fum() {
    // . . .
}
Fum.prototype = new Fo();

var fum = new Fum();

if (Fi.prototype.isPrototypeOf(fum)) {
    // do something safe
    print("OK");
}

/*
=!EXPECTSTART!=
Meow, I am Garfield
Meow, I am Felix
What's new?
Meow, I am Felix
true
false
"function f(i, j) {...}"
"function f(i, j) {...}"
true
OK
=!EXPECTEND!=
*/
