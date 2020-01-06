// Copyright (C) 2016 Jordan Harband. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/*---
esid: sec-string.prototype.padend
description: >
  String#padEnd should return the string unchanged when
  an explicit empty string is provided
author: Jordan Harband
---*/

assert.sameValue('abc'.padEnd(340282366920938463463374607431768211461, ''), 'abc');
