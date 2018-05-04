
"use asserts";

assert(true,'true');
assert(2*3 == 6,'math');
try {
    assert(false,'false');
} catch(e) {
    print('caught error');
}
Interp.conf({asserts:false});
assert(false,'false2');
Interp.conf({asserts:true});

var i=1, j=2;
assert(function () { return (i<j); },'fail');
print("K"); 
try {
    assert(false,'false');
} catch(e) {
    print('caught error2: '+e);
}

assert(false,'this assert failed',{mode:'print', noStderr:true});

Interp.conf({assertMode:"print", noStderr:true});

assert(false,'assert also failed');

print('done');

/*
=!EXPECTSTART!=
caught error
K
caught error2: ASSERT: false
ASSERT: this assert failed
ASSERT: assert also failed
done
=!EXPECTEND!=
*/
