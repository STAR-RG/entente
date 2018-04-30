// Bug report found by Arthur Lapprand
// https://bugzilla.mozilla.org/show_bug.cgi?id=1395844
try {
    new Date().toLocaleTimeString();
} catch (error) {
    throw new Error('Test failed');
}