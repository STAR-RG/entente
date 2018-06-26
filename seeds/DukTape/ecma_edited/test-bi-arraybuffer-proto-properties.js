/*
 *  Properties of ArrayBuffer.prototype
 */

/*---
{
    "custom": true
}
---*/

function encValue(v) {
    if (typeof v === 'function') { return 'function'; }
    return String(v);
}

/*===
ArrayBuffer prototype properties test
slice true function function
isView false undefined undefined
constructor true function function
true
===*/

function arrayBufferPrototypePropertiesTest() {
    var props = [
        'slice',
        'isView',  // not present, provided by ArrayBuffer constructor
        'constructor'
    ];

    var i=0;
    props.forEach(function (propname) {
        try {
            var obj = ArrayBuffer.prototype;
            var val = obj[propname];
            i=i+1;
            //print(propname, propname in obj, typeof val, encValue(val));
            if(i==1) {
                if(propname!=='slice') throw new Error('Test Failed');
                if(propname in obj !== true) throw new Error('Test Failed');
                if(typeof val !== "function") throw new Error('Test Failed');
                if(encValue(val) !== "function") throw new Error('Test Failed');
            }
            if(i==2) {
                if(propname!=='isView') throw new Error('Test Failed');
                if(propname in obj !== false) throw new Error('Test Failed');
                if(typeof val !== "undefined") throw new Error('Test Failed');
                if(encValue(val) !== "undefined") throw new Error('Test Failed');
            }
            if(i==3) {
                if(propname!=='constructor') throw new Error('Test Failed');
                if(propname in obj !== true) throw new Error('Test Failed');
                if(typeof val !== "function") throw new Error('Test Failed');
                if(encValue(val) !== "function") throw new Error('Test Failed');
            }
        } catch (e) {
            throw new Error(e);
        }
    });

    //print(ArrayBuffer.prototype.constructor === ArrayBuffer);
    if((ArrayBuffer.prototype.constructor === ArrayBuffer) !== true) throw new Error('Test Failed');
}

//print('ArrayBuffer prototype properties test');
arrayBufferPrototypePropertiesTest();
