function Person(name) {
  this.name = name;
  this.kill = function() { this.name += " is dead"; };
}

var a = new Person("Kenny");
a.kill();
assert(a.name == "Kenny is dead");

