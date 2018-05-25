

function jc(n)
{
    if (n <= 1) return 1;
    return jc(n - 1) * n;
};

print(jc(10));

/*
=!EXPECTSTART!=
3628800
=!EXPECTEND!=
*/
