assert = function(is_true){if (!(is_true)) {throw new Error("Test failed")}} 
function Person(name) {
  this.name = name;
  this.kill = function() { this.name += " is dead"; };
}

var a = new Person("Kenny");
a.kill();
result = a.name == "Kenny is dead";

assert(result);
