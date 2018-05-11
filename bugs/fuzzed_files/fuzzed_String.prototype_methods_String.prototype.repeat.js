function test() {

return typeof String.prototype.repeat === 'function'
  && "foo".repeat(657604378) === "foofoofoo";
      
}

if (!test())
    throw new Error("Test failed");

