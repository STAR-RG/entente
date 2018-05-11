   const nativeErrors = [
     TypeError,
     EvalError,
     RangeError,
     ReferenceError,
     SyntaxError,
     TypeError,
     URIError
 ];

  for (const error of nativeErrors)
      assertEq(Reflect.getPrototypeOf(error), Error);

