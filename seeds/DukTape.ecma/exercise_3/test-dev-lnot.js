/* XXX: missing a lot of coercion tests */

/*===
true
false
true
false
true
false
===*/

if((true) != true) throw new Error('Test Failed')
if((!true) != false) throw new Error('Test Failed')
if((!!true) != true) throw new Error('Test Failed')
if((false) != false) throw new Error('Test Failed')
if((!false) != true) throw new Error('Test Failed')
if((!!false) != false) throw new Error('Test Failed')

/*===
false
true
true
false
false
true
===*/

if((!{}) != false) throw new Error('Test Failed')
if((!!{}) != true) throw new Error('Test Failed')
if((!'') != true) throw new Error('Test Failed')
if((!!'') != false) throw new Error('Test Failed')
if((!'a') != false) throw new Error('Test Failed')
if((!!'a') != true) throw new Error('Test Failed')
