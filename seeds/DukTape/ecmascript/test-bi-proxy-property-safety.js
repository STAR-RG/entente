/*
 *  Ensure Proxy internal keys _Target and _Handler are not modifiable.
 *
 *  Note: for a fully implemented Proxy getting at the Proxy object properties
 *  (instead of the target object properties) is not easy.  Right now Duktape's
 *  Proxy is a subset of the ES2015 Proxy, and it's possible to access properties
 *  of the Proxy itself using e.g. Object.getOwnPropertyDescriptor() to check for
 *  property attributes.  Once that behavior is fixed, this test will fail and
 *  can maybe be reimplemented using the C API.
 *
 *  Skipped since Duktape 2.2: with duk_hproxy proxy target and handler are
 *  struct fields rather than internal properties.
 */

/*@include util-buffer.js@*/

/*---
{
    "custom": true,
    "skip": true
}
---*/

/*===
_Target
false
undefined string false false
object false false false
true false
_Handler
false
undefined string false false
object false false false
false true
===*/

function proxyPropertyTest(key) {
    var obj = {};
    var traps = {};
    var proxy = new Proxy(obj, traps);
    var val1, val2;

    // These don't really access the Proxy object itself - reads and writes will
    // fall back to the target object.

    print(key in proxy);
    val1 = proxy[key];
    proxy[key] = 'dummy';
    val2 = proxy[key];
    print(typeof val1, typeof val2, val1 === val2, val1 === obj);

    // In Duktape 1.x, with the Proxy subset, getOwnPropertyDescriptor() will
    // fetch the property descriptor from the proxy instead of the target.

    pd = Object.getOwnPropertyDescriptor(proxy, key);
    print(typeof pd.value, pd.writable, pd.enumerable, pd.configurable);
    print(pd.value === obj, pd.value === traps);
}

function proxyInternalKeysSandboxTest() {
    print('_Target');
    proxyPropertyTest(bufferToStringRaw(Duktape.dec('hex', 'ff546172676574')));
    print('_Handler');
    proxyPropertyTest(bufferToStringRaw(Duktape.dec('hex', 'ff48616e646c6572')));
}

try {
    proxyInternalKeysSandboxTest();
} catch (e) {
    print(e.stack || e);
}
