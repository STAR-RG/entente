/*===
function
function
===*/

/* Simple test that function declaration name and function expression name
 * can be accessed from inside the function.
 */
function foo() {
    if((typeof foo) !== 'function') throw new Error('Test Failed')
}

foo();

var funcexpr = 'not visible';
var temp = function funcexpr() {
    if((typeof funcexpr) !== 'function') throw new Error('Test Failed')
};

temp();
