

log("Starting");
function test(msg, debug) {
    var logDebug = (debug?log.bind(null, 'DEBUG: '):noOp);
    logDebug("testing 1, 2, 3: "+msg);
}
test('call1', false);
test('call2', true);

print('done');

/*
=!EXPECTSTART!=
"Starting", logging.js:3, 
"DEBUG:  testing 1, 2, 3: call2", logging.js:6, test()
done
=!EXPECTEND!=
*/
