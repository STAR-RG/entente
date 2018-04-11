// Found by Mariana Moura
// https://bugs.chromium.org/p/v8/issues/detail?id=4962

Intl.NumberFormat.call(new Proxy({},{}))