// Copyright 2009 the Sputnik authors.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/*---
info: When appears not closed single-quote program failes
es5id: 8.4_A13_T3
description: Try to create variable using 4 single-quote
negative:
  phase: parse
  type: SyntaxError
---*/

// throw "Test262: This statement should not be evaluated.";

var str = '''';
