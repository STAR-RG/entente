assert = function(isTrue) {
    if (!(isTrue)) {
        throw new Error('Test failed');
    }
}