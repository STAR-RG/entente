

try {
    eval("throw('abc');");
} catch(e) {
    print(e);
} finally {
    print("finally");
}

/*
=!EXPECTSTART!=
abc
finally
=!EXPECTEND!=
*/
