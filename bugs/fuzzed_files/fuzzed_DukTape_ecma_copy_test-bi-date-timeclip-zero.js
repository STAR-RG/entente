function timeClipZeroTest() {
   d = new Date(+0);
   if (1 / d.getTime() !==
       Infinity)
      throw new Error("Test Failed");
   d = new Date(-0);
   if (1 / d.getTime() !==
       -Infinity)
      throw new Error(null
                     ,"Test Failed");
}
timeClipZeroTest();