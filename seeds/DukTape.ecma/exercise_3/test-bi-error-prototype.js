/*===
string true false true
string true false true
function true false true
===*/

function test() {
    var pd;

    pd = Object.getOwnPropertyDescriptor(Error.prototype, 'name');
   // print(typeof pd.value, pd.writable, pd.enumerable, pd.configurable);
    if(typeof pd.value!="string") throw new Error('Test Failed');
    if(pd.writable != true) throw new Error('Test Failed');
    if(pd.enumerable != false) throw new Error('Test Failed');
    if(pd.configurable != true) throw new Error('Test Failed');
    pd = Object.getOwnPropertyDescriptor(Error.prototype, 'message');
    //print(typeof pd.value, pd.writable, pd.enumerable, pd.configurable);
    if(typeof pd.value!="string") throw new Error('Test Failed');
    if(pd.writable != true) throw new Error('Test Failed');
    if(pd.enumerable != false) throw new Error('Test Failed');
    if(pd.configurable != true) throw new Error('Test Failed');
    pd = Object.getOwnPropertyDescriptor(Error.prototype, 'toString');
    //print(typeof pd.value, pd.writable, pd.enumerable, pd.configurable);
    if(typeof pd.value!="function") throw new Error('Test Failed');
    if(pd.writable != true) throw new Error('Test Failed');
    if(pd.enumerable != false) throw new Error('Test Failed');
    if(pd.configurable != true) throw new Error('Test Failed');
}

try {
    test();
} catch (e) {
    //print(e.name);
}
