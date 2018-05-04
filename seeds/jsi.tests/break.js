

var i = 1;
ABC:
{
    i++;
    break ABC;
    print("FOO");
}
print("DONE");

/*
=!EXPECTSTART!=
DONE
FOO
=!EXPECTEND!=
*/

