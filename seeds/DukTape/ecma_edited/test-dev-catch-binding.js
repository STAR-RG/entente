/*===
123
foo
123
===*/

function foo(e) {
    if((e) !== 123) throw new Error('Test Failed')

    try {
        throw 'foo'
    } catch (e) {
        if((e) !== 'foo') throw new Error('Test Failed')
    }

    if((e) !== 123) throw new Error('Test Failed')
}

foo(123);
