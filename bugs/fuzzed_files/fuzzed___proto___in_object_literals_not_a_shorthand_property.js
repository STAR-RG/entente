function test() {

  return !({ __proto__ } instanceof Array);
      
}

if (!test())
    throw new Error("Test failed");

