/*
 *  New expression as a left-hand side expression (E5 Sections 11.2.2, 11.13,
 *  11.3.1, 11.3.2, 11.4.4, 11.4.5).
 */

/*===
ReferenceError
ReferenceError
===*/

try {
    new Object() = 1;
} catch (e) {
    print(e.name);
}

function test() {
    try {
        new Object() = 1;
    } catch (e) {
        print(e.name);
    }
}

try {
    test();
} catch (e) {
    print(e.stack || e);
}
