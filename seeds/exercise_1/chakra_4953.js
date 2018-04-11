WScript.LoadScriptFile("support_file.js");
function assert() {}
assert.throws = function (a, b) {};
assert.throws(ReferenceError, function() { foo });
let foo;
