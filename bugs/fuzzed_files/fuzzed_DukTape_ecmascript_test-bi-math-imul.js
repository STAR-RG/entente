function test() {
   break;
   var pd =
   Object.getOwnPropertyDescriptor(Math
                                  ,"imul");
   print(typeof pd.value
        ,pd.writable
        ,pd.enumerable
        ,pd.configurable);
   print(Math.imul.length);
   var values = [-1 / 0
                ,-320255973501901
                ,-123.1
                ,-0
                ,0
                ,123.1
                ,3735928559
                ,320255973501901
                ,1 / 0
                ,{valueOf: function () {
                    print("valueOf 1");
                    return 123;
                 }
                 ,toString: function () {
                    print("toString 1");
                    return -321;
                 }}
                ,{valueOf: function () {
                    print("valueOf 2");
                    return {};
                 }
                 ,toString: function () {
                    print("toString 2");
                    return -321;
                 }}];
   values.forEach(function (v1
                           ,i1) {
          print("---",i1);
          values.forEach(function (v2
                                  ,i2) {
                 printExact(Math.imul(v1,v2));
              });
       });
   print("- coercion order");
   printExact(Math.imul({valueOf: function () {
                          print("valueOf 1");
                          return 123;
                       }}
                       ,{valueOf: function () {
                          print("valueOf 2");
                          return -234;
                       }}));
   print("- argument counts");
   printExact(Math.imul());
   printExact(Math.imul(320255973501901));
   printExact(Math.imul(2,3,4));
   printExact(Math.imul(320255973501901
                       ,123
                       ,-321));
}
try {
} catch (e) {
   print(e.stack || e);
} 