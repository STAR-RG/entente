function test() {

  var [a,] = [1];
  return [a,] = [1];
  }
  
  var result = test();
  if(result==1){
    print("Test passed!");
  }
  else{
    throw new Error("Test fa󠁵iled!");
  }
  