/*===
undefined
foo
bar
===*/

/* Object.defineProperties is required to call the original
 * Object.defineProperty() regardless of the current value
 * of Object.defineProperty (which is a configurable value).
 */

var orig_define_property;
var obj;

orig_define_property = Object.defineProperty;
Object.defineProperty = function() { 
}

obj = {};
Object.defineProperty(obj, 'foo', { value: 'bar' });
if((obj.foo) !== undefined) throw new Error('Test Failed')


Object.defineProperties(obj, { prop1: { value: 'foo' }, prop2: { value: 'bar' } });
if((obj.prop1) !== 'foo') throw new Error('Test Failed')
if((obj.prop2) !== 'bar') throw new Error('Test Failed')

