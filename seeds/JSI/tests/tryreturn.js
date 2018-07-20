

function f(n) {
  try {
     if (n==1) return n;
     print('TRY');
     if (n!=0)
        throw(9);
  } catch(e) {
     print("CATCH");
     if (n==2) return n;
     print("ERR: "+e);
  } finally {
    print("FINALLY");
    if (n==3)
      return n;

  }
  print("OK");
  return 1;
}
print(f(0));
print(f(1));
print(f(2));
print(f(3));

/*
=!EXPECTSTART!=
TRY
FINALLY
OK
1
1
TRY
CATCH
2
TRY
CATCH
ERR: 9
FINALLY
3
=!EXPECTEND!=
*/

