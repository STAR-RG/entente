// Copyright (C) 2017 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Verify that a subArray is contained within an array.
---*/

/**
 * @param {Array} array
 * @param {Array} subArray
 */

function arrayContains(array, subArray) {
  var found;
  for (var i = 0; i < subArray.length; i++) {
    found = false;
    for (var j = 0; j < array.length; j++) {
      if (subArray[i] === array[j]) {
        found = true;
        break;
      }
    }
    if (!found) {
      return false;
    }
  }
  return true;
}
// Copyright (C) 2017 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Collection of assertion functions used throughout test262
---*/

function assert(mustBeTrue, message) {
  if (mustBeTrue === true) {
    return;
  }

  if (message === undefined) {
    message = 'Expected true but got ' + String(mustBeTrue);
  }
  print(message);
}

assert._isSameValue = function (a, b) {
  if (a === b) {
    // Handle +/-0 vs. -/+0
    return a !== 0 || 1 / a === 1 / b;
  }

  // Handle NaN vs. NaN
  return a !== a && b !== b;
};

assert.sameValue = function (actual, expected, message) {
  if (assert._isSameValue(actual, expected)) {
    return;
  }

  if (message === undefined) {
    message = '';
  } else {
    message += ' ';
  }

  message += 'Expected SameValue(«' + String(actual) + '», «' + String(expected) + '») to be true';

  print(message);
};

assert.notSameValue = function (actual, unexpected, message) {
  if (!assert._isSameValue(actual, unexpected)) {
    return;
  }

  if (message === undefined) {
    message = '';
  } else {
    message += ' ';
  }

  message += 'Expected SameValue(«' + String(actual) + '», «' + String(unexpected) + '») to be false';

  print(message);
};

assert.throws = function (expectedErrorConstructor, func, message) {
  if (typeof func !== "function") {
    print('assert.throws requires two arguments: the error constructor ' +
      'and a function to run');
    return;
  }
  if (message === undefined) {
    message = '';
  } else {
    message += ' ';
  }

  try {
    func();
  } catch (thrown) {
    if (typeof thrown !== 'object' || thrown === null) {
      message += 'Thrown value was not an object!';
      print(message);
    } else if (thrown.constructor !== expectedErrorConstructor) {
      message += 'Expected a ' + expectedErrorConstructor.name + ' but got a ' + thrown.constructor.name;
      print(message);
    }
    return;
  }

  message += 'Expected a ' + expectedErrorConstructor.name + ' to be thrown but no exception was thrown at all';
  print(message);
};

assert.throws.early = function(err, code) {
  var wrappedCode = 'function wrapperFn() { ' + code + ' }';
  var ieval = eval;

  assert.throws(err, function() { Function(wrappedCode); }, 'Function: ' + code);
};
// Copyright (C) 2015 the V8 project authors. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Verify that the given date object's Number representation describes the
    correct number of milliseconds since the Unix epoch relative to the local
    time zone (as interpreted at the specified date).
---*/

/**
 * @param {Date} date
 * @param {Number} expectedMs
 */
function assertRelativeDateMs(date, expectedMs) {
  var actualMs = date.valueOf();
  var localOffset = date.getTimezoneOffset() * 60000;

  if (actualMs - localOffset !== expectedMs) {
    print(
      'Expected ' + date + ' to be ' + expectedMs +
      ' milliseconds from the Unix epoch'
    );
  }
}
// Copyright (C) 2017 Mozilla Corporation.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: >
    Collection of functions used to interact with Atomics.* operations across agent boundaries.
---*/

/**
 * The amount of slack allowed for testing time-related Atomics methods (i.e. wait and wake).
 * The absolute value of the difference of the observed time and the expected time must
 * be epsilon-close.
 */
// $262.agent.MAX_TIME_EPSILON = 100;

/**
 * @return {String} A report sent from an agent.
 */
{
  // This is only necessary because the original
  // $262.agent.getReport API was insufficient.
  //
  // All runtimes currently have their own
  // $262.agent.getReport which is wrong, so we
  // will pave over it with a corrected version.
  //
  // Binding $262.agent is necessary to prevent
  // breaking SpiderMonkey's $262.agent.getReport
  // let getReport = $262.agent.getReport.bind($262.agent);

  // $262.agent.getReport = function() {
  //   var r;
  //   while ((r = getReport()) == null) {
  //     $262.agent.sleep(1);
  //   }
  //   return r;
  // };
}
/**
 * With a given Int32Array or BigInt64Array, wait until the expected number of agents have
 * reported themselves by calling:
 *
 *    Atomics.add(typedArray, index, 1);
 *
 * @param {(Int32Array|BigInt64Array)} typedArray An Int32Array or BigInt64Array with a SharedArrayBuffer
 * @param {number} index    The index of which all agents will report.
 * @param {number} expected The number of agents that are expected to report as active.
 */
// $262.agent.waitUntil = function(typedArray, index, expected) {
//   var agents = 0;
//   while ((agents = Atomics.load(typedArray, index)) !== expected) {
//     /* nothing */
//   }
//   assert.sameValue(agents, expected, "Reporting number of 'agents' equals the value of 'expected'");
// };

/**
 * Timeout values used throughout the Atomics tests. All timeouts are specified in milliseconds.
 *
 * @property {number} yield Used for `$262.agent.tryYield`. Must not be used in other functions.
 * @property {number} small Used when agents will always timeout and `Atomics.wake` is not part
 *                          of the test semantics. Must be larger than `$262.agent.timeouts.yield`.
 * @property {number} long  Used when some agents may timeout and `Atomics.wake` is called on some
 *                          agents. The agents are required to wait and this needs to be observable
 *                          by the main thread.
 * @property {number} huge  Used when `Atomics.wake` is called on all waiting agents. The waiting
 *                          must not timeout. The agents are required to wait and this needs to be
 *                          observable by the main thread. All waiting agents must be woken by the
 *                          main thread.
 *
 * Usage for `$262.agent.timeouts.small`:
 *   const WAIT_INDEX = 0;
 *   const RUNNING = 1;
 *   const TIMEOUT = $262.agent.timeouts.small;
 *   const i32a = new Int32Array(new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT * 2));
 *
 *   $262.agent.start(`
 *     $262.agent.receiveBroadcast(function(sab) {
 *       const i32a = new Int32Array(sab);
 *       Atomics.add(i32a, ${RUNNING}, 1);
 *
 *       $262.agent.report(Atomics.wait(i32a, ${WAIT_INDEX}, 0, ${TIMEOUT}));
 *
 *       $262.agent.leaving();
 *     });
 *   `);
 *   $262.agent.broadcast(i32a.buffer);
 *
 *   // Wait until the agent was started and then try to yield control to increase
 *   // the likelihood the agent has called `Atomics.wait` and is now waiting.
 *   $262.agent.waitUntil(i32a, RUNNING, 1);
 *   $262.agent.tryYield();
 *
 *   // The agent is expected to time out.
 *   assert.sameValue($262.agent.getReport(), "timed-out");
 *
 *
 * Usage for `$262.agent.timeouts.long`:
 *   const WAIT_INDEX = 0;
 *   const RUNNING = 1;
 *   const NUMAGENT = 2;
 *   const TIMEOUT = $262.agent.timeouts.long;
 *   const i32a = new Int32Array(new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT * 2));
 *
 *   for (let i = 0; i < NUMAGENT; i++) {
 *     $262.agent.start(`
 *       $262.agent.receiveBroadcast(function(sab) {
 *         const i32a = new Int32Array(sab);
 *         Atomics.add(i32a, ${RUNNING}, 1);
 *
 *         $262.agent.report(Atomics.wait(i32a, ${WAIT_INDEX}, 0, ${TIMEOUT}));
 *
 *         $262.agent.leaving();
 *       });
 *     `);
 *   }
 *   $262.agent.broadcast(i32a.buffer);
 *
 *   // Wait until the agents were started and then try to yield control to increase
 *   // the likelihood the agents have called `Atomics.wait` and are now waiting.
 *   $262.agent.waitUntil(i32a, RUNNING, NUMAGENT);
 *   $262.agent.tryYield();
 *
 *   // Wake exactly one agent.
 *   assert.sameValue(Atomics.wake(i32a, WAIT_INDEX, 1), 1);
 *
 *   // When it doesn't matter how many agents were woken at once, a while loop
 *   // can be used to make the test more resilient against intermittent failures
 *   // in case even though `tryYield` was called, the agents haven't started to
 *   // wait.
 *   //
 *   // // Repeat until exactly one agent was woken.
 *   // var woken = 0;
 *   // while ((woken = Atomics.wake(i32a, WAIT_INDEX, 1)) !== 0) ;
 *   // assert.sameValue(woken, 1);
 *
 *   // One agent was woken and the other one timed out.
 *   const reports = [$262.agent.getReport(), $262.agent.getReport()];
 *   assert(reports.includes("ok"));
 *   assert(reports.includes("timed-out"));
 *
 *
 * Usage for `$262.agent.timeouts.huge`:
 *   const WAIT_INDEX = 0;
 *   const RUNNING = 1;
 *   const NUMAGENT = 2;
 *   const TIMEOUT = $262.agent.timeouts.huge;
 *   const i32a = new Int32Array(new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT * 2));
 *
 *   for (let i = 0; i < NUMAGENT; i++) {
 *     $262.agent.start(`
 *       $262.agent.receiveBroadcast(function(sab) {
 *         const i32a = new Int32Array(sab);
 *         Atomics.add(i32a, ${RUNNING}, 1);
 *
 *         $262.agent.report(Atomics.wait(i32a, ${WAIT_INDEX}, 0, ${TIMEOUT}));
 *
 *         $262.agent.leaving();
 *       });
 *     `);
 *   }
 *   $262.agent.broadcast(i32a.buffer);
 *
 *   // Wait until the agents were started and then try to yield control to increase
 *   // the likelihood the agents have called `Atomics.wait` and are now waiting.
 *   $262.agent.waitUntil(i32a, RUNNING, NUMAGENT);
 *   $262.agent.tryYield();
 *
 *   // Wake all agents.
 *   assert.sameValue(Atomics.wake(i32a, WAIT_INDEX), NUMAGENT);
 *
 *   // When it doesn't matter how many agents were woken at once, a while loop
 *   // can be used to make the test more resilient against intermittent failures
 *   // in case even though `tryYield` was called, the agents haven't started to
 *   // wait.
 *   //
 *   // // Repeat until all agents were woken.
 *   // for (var wokenCount = 0; wokenCount < NUMAGENT; ) {
 *   //   var woken = 0;
 *   //   while ((woken = Atomics.wake(i32a, WAIT_INDEX)) !== 0) ;
 *   //   // Maybe perform an action on the woken agents here.
 *   //   wokenCount += woken;
 *   // }
 *
 *   // All agents were woken and none timeout.
 *   for (var i = 0; i < NUMAGENT; i++) {
 *     assert($262.agent.getReport(), "ok");
 *   }
 */
// $262.agent.timeouts = {
//   yield: 100,
//   small: 200,
//   long: 1000,
//   huge: 10000,
// };

/**
 * Try to yield control to the agent threads.
 *
 * Usage:
 *   const VALUE = 0;
 *   const RUNNING = 1;
 *   const i32a = new Int32Array(new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT * 2));
 *
 *   $262.agent.start(`
 *     $262.agent.receiveBroadcast(function(sab) {
 *       const i32a = new Int32Array(sab);
 *       Atomics.add(i32a, ${RUNNING}, 1);
 *
 *       Atomics.store(i32a, ${VALUE}, 1);
 *
 *       $262.agent.leaving();
 *     });
 *   `);
 *   $262.agent.broadcast(i32a.buffer);
 *
 *   // Wait until agent was started and then try to yield control.
 *   $262.agent.waitUntil(i32a, RUNNING, 1);
 *   $262.agent.tryYield();
 *
 *   // Note: This result is not guaranteed, but should hold in practice most of the time.
 *   assert.sameValue(Atomics.load(i32a, VALUE), 1);
 *
 * The default implementation simply waits for `$262.agent.timeouts.yield` milliseconds.
 */
// $262.agent.tryYield = function() {
//   $262.agent.sleep($262.agent.timeouts.yield);
// };

/**
 * Try to sleep the current agent for the given amount of milliseconds. It is acceptable,
 * but not encouraged, to ignore this sleep request and directly continue execution.
 *
 * The default implementation calls `$262.agent.sleep(ms)`.
 *
 * @param {number} ms Time to sleep in milliseconds.
 */
// $262.agent.trySleep = function(ms) {
//   $262.agent.sleep(ms);
// };
// Copyright (C) 2016 the V8 project authors. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Provide a list for original and expected values for different byte
    conversions.
    This helper is mostly used on tests for TypedArray and DataView, and each
    array from the expected values must match the original values array on every
    index containing its original value.
---*/
var byteConversionValues = {
  values: [
    127,         // 2 ** 7 - 1
    128,         // 2 ** 7
    32767,       // 2 ** 15 - 1
    32768,       // 2 ** 15
    2147483647,  // 2 ** 31 - 1
    2147483648,  // 2 ** 31
    255,         // 2 ** 8 - 1
    256,         // 2 ** 8
    65535,       // 2 ** 16 - 1
    65536,       // 2 ** 16
    4294967295,  // 2 ** 32 - 1
    4294967296,  // 2 ** 32
    9007199254740991, // 2 ** 53 - 1
    9007199254740992, // 2 ** 53
    1.1,
    0.1,
    0.5,
    0.50000001,
    0.6,
    0.7,
    undefined,
    -1,
    -0,
    -0.1,
    -1.1,
    NaN,
    -127,        // - ( 2 ** 7 - 1 )
    -128,        // - ( 2 ** 7 )
    -32767,      // - ( 2 ** 15 - 1 )
    -32768,      // - ( 2 ** 15 )
    -2147483647, // - ( 2 ** 31 - 1 )
    -2147483648, // - ( 2 ** 31 )
    -255,        // - ( 2 ** 8 - 1 )
    -256,        // - ( 2 ** 8 )
    -65535,      // - ( 2 ** 16 - 1 )
    -65536,      // - ( 2 ** 16 )
    -4294967295, // - ( 2 ** 32 - 1 )
    -4294967296, // - ( 2 ** 32 )
    Infinity,
    -Infinity,
    0
  ],

  expected: {
    Int8: [
      127,  // 127
      -128, // 128
      -1,   // 32767
      0,    // 32768
      -1,   // 2147483647
      0,    // 2147483648
      -1,   // 255
      0,    // 256
      -1,   // 65535
      0,    // 65536
      -1,   // 4294967295
      0,    // 4294967296
      -1,   // 9007199254740991
      0,    // 9007199254740992
      1,    // 1.1
      0,    // 0.1
      0,    // 0.5
      0,    // 0.50000001,
      0,    // 0.6
      0,    // 0.7
      0,    // undefined
      -1,   // -1
      0,    // -0
      0,    // -0.1
      -1,   // -1.1
      0,    // NaN
      -127, // -127
      -128, // -128
      1,    // -32767
      0,    // -32768
      1,    // -2147483647
      0,    // -2147483648
      1,    // -255
      0,    // -256
      1,    // -65535
      0,    // -65536
      1,    // -4294967295
      0,    // -4294967296
      0,    // Infinity
      0,    // -Infinity
      0
    ],
    Uint8: [
      127, // 127
      128, // 128
      255, // 32767
      0,   // 32768
      255, // 2147483647
      0,   // 2147483648
      255, // 255
      0,   // 256
      255, // 65535
      0,   // 65536
      255, // 4294967295
      0,   // 4294967296
      255, // 9007199254740991
      0,   // 9007199254740992
      1,   // 1.1
      0,   // 0.1
      0,   // 0.5
      0,   // 0.50000001,
      0,   // 0.6
      0,   // 0.7
      0,   // undefined
      255, // -1
      0,   // -0
      0,   // -0.1
      255, // -1.1
      0,   // NaN
      129, // -127
      128, // -128
      1,   // -32767
      0,   // -32768
      1,   // -2147483647
      0,   // -2147483648
      1,   // -255
      0,   // -256
      1,   // -65535
      0,   // -65536
      1,   // -4294967295
      0,   // -4294967296
      0,   // Infinity
      0,   // -Infinity
      0
    ],
    Uint8Clamped: [
      127, // 127
      128, // 128
      255, // 32767
      255, // 32768
      255, // 2147483647
      255, // 2147483648
      255, // 255
      255, // 256
      255, // 65535
      255, // 65536
      255, // 4294967295
      255, // 4294967296
      255, // 9007199254740991
      255, // 9007199254740992
      1,   // 1.1,
      0,   // 0.1
      0,   // 0.5
      1,   // 0.50000001,
      1,   // 0.6
      1,   // 0.7
      0,   // undefined
      0,   // -1
      0,   // -0
      0,   // -0.1
      0,   // -1.1
      0,   // NaN
      0,   // -127
      0,   // -128
      0,   // -32767
      0,   // -32768
      0,   // -2147483647
      0,   // -2147483648
      0,   // -255
      0,   // -256
      0,   // -65535
      0,   // -65536
      0,   // -4294967295
      0,   // -4294967296
      255, // Infinity
      0,   // -Infinity
      0
    ],
    Int16: [
      127,    // 127
      128,    // 128
      32767,  // 32767
      -32768, // 32768
      -1,     // 2147483647
      0,      // 2147483648
      255,    // 255
      256,    // 256
      -1,     // 65535
      0,      // 65536
      -1,     // 4294967295
      0,      // 4294967296
      -1,     // 9007199254740991
      0,      // 9007199254740992
      1,      // 1.1
      0,      // 0.1
      0,      // 0.5
      0,      // 0.50000001,
      0,      // 0.6
      0,      // 0.7
      0,      // undefined
      -1,     // -1
      0,      // -0
      0,      // -0.1
      -1,     // -1.1
      0,      // NaN
      -127,   // -127
      -128,   // -128
      -32767, // -32767
      -32768, // -32768
      1,      // -2147483647
      0,      // -2147483648
      -255,   // -255
      -256,   // -256
      1,      // -65535
      0,      // -65536
      1,      // -4294967295
      0,      // -4294967296
      0,      // Infinity
      0,      // -Infinity
      0
    ],
    Uint16: [
      127,   // 127
      128,   // 128
      32767, // 32767
      32768, // 32768
      65535, // 2147483647
      0,     // 2147483648
      255,   // 255
      256,   // 256
      65535, // 65535
      0,     // 65536
      65535, // 4294967295
      0,     // 4294967296
      65535, // 9007199254740991
      0,     // 9007199254740992
      1,     // 1.1
      0,     // 0.1
      0,     // 0.5
      0,     // 0.50000001,
      0,     // 0.6
      0,     // 0.7
      0,     // undefined
      65535, // -1
      0,     // -0
      0,     // -0.1
      65535, // -1.1
      0,     // NaN
      65409, // -127
      65408, // -128
      32769, // -32767
      32768, // -32768
      1,     // -2147483647
      0,     // -2147483648
      65281, // -255
      65280, // -256
      1,     // -65535
      0,     // -65536
      1,     // -4294967295
      0,     // -4294967296
      0,     // Infinity
      0,     // -Infinity
      0
    ],
    Int32: [
      127,         // 127
      128,         // 128
      32767,       // 32767
      32768,       // 32768
      2147483647,  // 2147483647
      -2147483648, // 2147483648
      255,         // 255
      256,         // 256
      65535,       // 65535
      65536,       // 65536
      -1,          // 4294967295
      0,           // 4294967296
      -1,          // 9007199254740991
      0,           // 9007199254740992
      1,           // 1.1
      0,           // 0.1
      0,           // 0.5
      0,           // 0.50000001,
      0,           // 0.6
      0,           // 0.7
      0,           // undefined
      -1,          // -1
      0,           // -0
      0,           // -0.1
      -1,          // -1.1
      0,           // NaN
      -127,        // -127
      -128,        // -128
      -32767,      // -32767
      -32768,      // -32768
      -2147483647, // -2147483647
      -2147483648, // -2147483648
      -255,        // -255
      -256,        // -256
      -65535,      // -65535
      -65536,      // -65536
      1,           // -4294967295
      0,           // -4294967296
      0,           // Infinity
      0,           // -Infinity
      0
    ],
    Uint32: [
      127,        // 127
      128,        // 128
      32767,      // 32767
      32768,      // 32768
      2147483647, // 2147483647
      2147483648, // 2147483648
      255,        // 255
      256,        // 256
      65535,      // 65535
      65536,      // 65536
      4294967295, // 4294967295
      0,          // 4294967296
      4294967295, // 9007199254740991
      0,          // 9007199254740992
      1,          // 1.1
      0,          // 0.1
      0,          // 0.5
      0,          // 0.50000001,
      0,          // 0.6
      0,          // 0.7
      0,          // undefined
      4294967295, // -1
      0,          // -0
      0,          // -0.1
      4294967295, // -1.1
      0,          // NaN
      4294967169, // -127
      4294967168, // -128
      4294934529, // -32767
      4294934528, // -32768
      2147483649, // -2147483647
      2147483648, // -2147483648
      4294967041, // -255
      4294967040, // -256
      4294901761, // -65535
      4294901760, // -65536
      1,          // -4294967295
      0,          // -4294967296
      0,          // Infinity
      0,          // -Infinity
      0
    ],
    Float32: [
      127,                  // 127
      128,                  // 128
      32767,                // 32767
      32768,                // 32768
      2147483648,           // 2147483647
      2147483648,           // 2147483648
      255,                  // 255
      256,                  // 256
      65535,                // 65535
      65536,                // 65536
      4294967296,           // 4294967295
      4294967296,           // 4294967296
      9007199254740992,     // 9007199254740991
      9007199254740992,     // 9007199254740992
      1.100000023841858,    // 1.1
      0.10000000149011612,  // 0.1
      0.5,                  // 0.5
      0.5,                  // 0.50000001,
      0.6000000238418579,   // 0.6
      0.699999988079071,    // 0.7
      NaN,                  // undefined
      -1,                   // -1
      -0,                   // -0
      -0.10000000149011612, // -0.1
      -1.100000023841858,   // -1.1
      NaN,                  // NaN
      -127,                 // -127
      -128,                 // -128
      -32767,               // -32767
      -32768,               // -32768
      -2147483648,          // -2147483647
      -2147483648,          // -2147483648
      -255,                 // -255
      -256,                 // -256
      -65535,               // -65535
      -65536,               // -65536
      -4294967296,          // -4294967295
      -4294967296,          // -4294967296
      Infinity,             // Infinity
      -Infinity,            // -Infinity
      0
    ],
    Float64: [
      127,         // 127
      128,         // 128
      32767,       // 32767
      32768,       // 32768
      2147483647,  // 2147483647
      2147483648,  // 2147483648
      255,         // 255
      256,         // 256
      65535,       // 65535
      65536,       // 65536
      4294967295,  // 4294967295
      4294967296,  // 4294967296
      9007199254740991, // 9007199254740991
      9007199254740992, // 9007199254740992
      1.1,         // 1.1
      0.1,         // 0.1
      0.5,         // 0.5
      0.50000001,  // 0.50000001,
      0.6,         // 0.6
      0.7,         // 0.7
      NaN,         // undefined
      -1,          // -1
      -0,          // -0
      -0.1,        // -0.1
      -1.1,        // -1.1
      NaN,         // NaN
      -127,        // -127
      -128,        // -128
      -32767,      // -32767
      -32768,      // -32768
      -2147483647, // -2147483647
      -2147483648, // -2147483648
      -255,        // -255
      -256,        // -256
      -65535,      // -65535
      -65536,      // -65536
      -4294967295, // -4294967295
      -4294967296, // -4294967296
      Infinity,    // Infinity
      -Infinity,   // -Infinity
      0
    ]
  }
};
// Copyright (C) 2017 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Compare the contents of two arrays
---*/

function compareArray(a, b) {
  if (b.length !== a.length) {
    return false;
  }

  for (var i = 0; i < a.length; i++) {
    if (b[i] !== a[i]) {
      return false;
    }
  }
  return true;
}

assert.compareArray = function(actual, expected, message) {
  assert(compareArray(actual, expected),
         'Expected [' + actual.join(', ') + '] and [' + expected.join(', ') + '] to have the same contents. ' + message);
};
// Copyright (C) 2018 Peter Wong.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: Compare the values of an iterator with an array of expected values
---*/

// Example:
//
//    function* numbers() {
//      yield 1;
//      yield 2;
//      yield 3;
//    }
//
//    compareIterator(numbers(), [
//      v => assert.sameValue(v, 1),
//      v => assert.sameValue(v, 2),
//      v => assert.sameValue(v, 3),
//    ]);
//
assert.compareIterator = function(iter, validators, message) {
  message = message || '';

  var i, result;
  for (i = 0; i < validators.length; i++) {
    result = iter.next();
    assert(!result.done, 'Expected ' + i + ' values(s). Instead iterator only produced ' + (i - 1) + ' value(s). ' + message);
    validators[i](result.value);
  }

  result = iter.next();
  assert(result.done, 'Expected only ' + i + ' values(s). Instead iterator produced more. ' + message);
  assert.sameValue(result.value, undefined, 'Expected value of `undefined` when iterator completes. ' + message);
}
// Copyright (C) 2009 the Sputnik authors.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Collection of date-centric values
---*/

var date_1899_end = -2208988800001;
var date_1900_start = -2208988800000;
var date_1969_end = -1;
var date_1970_start = 0;
var date_1999_end = 946684799999;
var date_2000_start = 946684800000;
var date_2099_end = 4102444799999;
var date_2100_start = 4102444800000;

var start_of_time = -8.64e15;
var end_of_time = 8.64e15;
// Copyright (C) 2017 André Bargull. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Collection of functions used to assert the correctness of various encoding operations.
---*/

function decimalToHexString(n) {
  var hex = "0123456789ABCDEF";
  n >>>= 0;
  var s = "";
  while (n) {
    s = hex[n & 0xf] + s;
    n >>>= 4;
  }
  while (s.length < 4) {
    s = "0" + s;
  }
  return s;
}

function decimalToPercentHexString(n) {
  var hex = "0123456789ABCDEF";
  return "%" + hex[(n >> 4) & 0xf] + hex[n & 0xf];
}
// Copyright (C) 2016 the V8 project authors.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    A function used in the process of asserting correctness of TypedArray objects.

    $262.detachArrayBuffer is defined by a host.

---*/

function $DETACHBUFFER(buffer) {
  if (!$262 || typeof $262.detachArrayBuffer !== "function") {
    throw new Test262Error("No method available to detach an ArrayBuffer");
  }
  $262.detachArrayBuffer(buffer);
}
// Copyright (C) 2017 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |

---*/

function __consolePrintHandle__(msg){
  print(msg);
}

function $DONE(){
  if(!arguments[0])
    // __consolePrintHandle__('Test262:AsyncTestComplete');
    __consolePrintHandle__('');
  else
    __consolePrintHandle__('Test262:AsyncTestFailure:' + arguments[0]);
}
// Copyright (C) 2017 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Produce a reliable global object
---*/

var __globalObject = Function("return this;")();
function fnGlobalObject() {
  return __globalObject;
}
// Copyright (C) 2017 André Bargull. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/*---
description: |
    Test if a given function is a constructor function.
---*/

function isConstructor(f) {
    try {
        Reflect.construct(function(){}, [], f);
    } catch (e) {
        return false;
    }
    return true;
}
// Copyright (C) 2016 the V8 project authors.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    A collection of NaN values produced from expressions that have been observed
    to create distinct bit representations on various platforms. These provide a
    weak basis for assertions regarding the consistent canonicalization of NaN
    values in Array buffers.
---*/

var NaNs = [
  NaN,
  Number.NaN,
  NaN * 0,
  0/0,
  Infinity/Infinity,
  -(0/0),
  Math.pow(-1, 0.5),
  -Math.pow(-1, 0.5),
  Number("Not-a-Number"),
];
// Copyright (C) 2016 Michael Ficarra.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: Assert _NativeFunction_ Syntax
info: |
    This regex makes a best-effort determination that the tested string matches
    the NativeFunction grammar production without requiring a correct tokeniser.

    NativeFunction :
      function _IdentifierName_ opt ( _FormalParameters_ ) { [ native code ] }

---*/
const NATIVE_FUNCTION_RE = /\bfunction\b[\s\S]*\([\s\S]*\)[\s\S]*\{[\s\S]*\[[\s\S]*\bnative\b[\s\S]+\bcode\b[\s\S]*\][\s\S]*\}/;

const assertToStringOrNativeFunction = function(fn, expected) {
  const actual = "" + fn;
  try {
    assert.sameValue(actual, expected);
  } catch (unused) {
    assertNativeFunction(fn, expected);
  }
};

const assertNativeFunction = function(fn, special) {
  const actual = "" + fn;
  assert(
    NATIVE_FUNCTION_RE.test(actual),
    "Conforms to NativeFunction Syntax: '" + actual + "'." + (special ? "(" + special + ")" : "")
  );
};
// Copyright (C) 2017 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Check that an array contains a numeric sequence starting at 1
    and incrementing by 1 for each entry in the array. Used by
    Promise tests to assert the order of execution in deep Promise
    resolution pipelines.
---*/

function checkSequence(arr, message) {
  arr.forEach(function(e, i) {
    if (e !== (i+1)) {
      print((message ? message : "Steps in unexpected sequence:") +
             " '" + arr.join(',') + "'");
    }
  });

  return true;
}
// Copyright (C) 2017 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Collection of functions used to safely verify the correctness of
    property descriptors.
---*/

function verifyProperty(obj, name, desc, options) {
  assert(
    arguments.length > 2,
    'verifyProperty should receive at least 3 arguments: obj, name, and descriptor'
  );

  var originalDesc = Object.getOwnPropertyDescriptor(obj, name);
  var nameStr = String(name);

  // Allows checking for undefined descriptor if it's explicitly given.
  if (desc === undefined) {
    assert.sameValue(
      originalDesc,
      undefined,
      "obj['" + nameStr + "'] descriptor should be undefined"
    );

    // desc and originalDesc are both undefined, problem solved;
    return true;
  }

  assert(
    Object.prototype.hasOwnProperty.call(obj, name),
    "obj should have an own property " + nameStr
  );

  assert.notSameValue(
    desc,
    null,
    "The desc argument should be an object or undefined, null"
  );

  assert.sameValue(
    typeof desc,
    "object",
    "The desc argument should be an object or undefined, " + String(desc)
  );

  var failures = [];

  if (Object.prototype.hasOwnProperty.call(desc, 'value')) {
    if (desc.value !== originalDesc.value) {
      failures.push("descriptor value should be " + desc.value);
    }
  }

  if (Object.prototype.hasOwnProperty.call(desc, 'enumerable')) {
    if (desc.enumerable !== originalDesc.enumerable ||
        desc.enumerable !== isEnumerable(obj, name)) {
      failures.push('descriptor should ' + (desc.enumerable ? '' : 'not ') + 'be enumerable');
    }
  }

  if (Object.prototype.hasOwnProperty.call(desc, 'writable')) {
    if (desc.writable !== originalDesc.writable ||
        desc.writable !== isWritable(obj, name)) {
      failures.push('descriptor should ' + (desc.writable ? '' : 'not ') + 'be writable');
    }
  }

  if (Object.prototype.hasOwnProperty.call(desc, 'configurable')) {
    if (desc.configurable !== originalDesc.configurable ||
        desc.configurable !== isConfigurable(obj, name)) {
      failures.push('descriptor should ' + (desc.configurable ? '' : 'not ') + 'be configurable');
    }
  }

  assert(!failures.length, failures.join('; '));

  if (options && options.restore) {
    Object.defineProperty(obj, name, originalDesc);
  }

  return true;
}

function isConfigurable(obj, name) {
  try {
    delete obj[name];
  } catch (e) {
    if (!(e instanceof TypeError)) {
      print("Expected TypeError, got " + e);
    }
  }
  return !Object.prototype.hasOwnProperty.call(obj, name);
}

function isEnumerable(obj, name) {
  var stringCheck = false;

  if (typeof name === "string") {
    for (var x in obj) {
      if (x === name) {
        stringCheck = true;
        break;
      }
    }
  } else {
    // skip it if name is not string, works for Symbol names.
    stringCheck = true;
  }

  return stringCheck &&
    Object.prototype.hasOwnProperty.call(obj, name) &&
    Object.prototype.propertyIsEnumerable.call(obj, name);
}

function isEqualTo(obj, name, expectedValue) {
  var actualValue = obj[name];

  return assert._isSameValue(actualValue, expectedValue);
}

function isWritable(obj, name, verifyProp, value) {
  var newValue = value || "unlikelyValue";
  var hadValue = Object.prototype.hasOwnProperty.call(obj, name);
  var oldValue = obj[name];
  var writeSucceeded;

  try {
    obj[name] = newValue;
  } catch (e) {
    if (!(e instanceof TypeError)) {
      print("Expected TypeError, got " + e);
    }
  }

  writeSucceeded = isEqualTo(obj, verifyProp || name, newValue);

  // Revert the change only if it was successful (in other cases, reverting
  // is unnecessary and may trigger exceptions for certain property
  // configurations)
  if (writeSucceeded) {
    if (hadValue) {
      obj[name] = oldValue;
    } else {
      delete obj[name];
    }
  }

  return writeSucceeded;
}

function verifyEqualTo(obj, name, value) {
  if (!isEqualTo(obj, name, value)) {
    print("Expected obj[" + String(name) + "] to equal " + value +
           ", actually " + obj[name]);
  }
}

function verifyWritable(obj, name, verifyProp, value) {
  if (!verifyProp) {
    assert(Object.getOwnPropertyDescriptor(obj, name).writable,
         "Expected obj[" + String(name) + "] to have writable:true.");
  }
  if (!isWritable(obj, name, verifyProp, value)) {
    print("Expected obj[" + String(name) + "] to be writable, but was not.");
  }
}

function verifyNotWritable(obj, name, verifyProp, value) {
  if (!verifyProp) {
    assert(!Object.getOwnPropertyDescriptor(obj, name).writable,
         "Expected obj[" + String(name) + "] to have writable:false.");
  }
  if (isWritable(obj, name, verifyProp)) {
    print("Expected obj[" + String(name) + "] NOT to be writable, but was.");
  }
}

function verifyEnumerable(obj, name) {
  assert(Object.getOwnPropertyDescriptor(obj, name).enumerable,
       "Expected obj[" + String(name) + "] to have enumerable:true.");
  if (!isEnumerable(obj, name)) {
    print("Expected obj[" + String(name) + "] to be enumerable, but was not.");
  }
}

function verifyNotEnumerable(obj, name) {
  assert(!Object.getOwnPropertyDescriptor(obj, name).enumerable,
       "Expected obj[" + String(name) + "] to have enumerable:false.");
  if (isEnumerable(obj, name)) {
    print("Expected obj[" + String(name) + "] NOT to be enumerable, but was.");
  }
}

function verifyConfigurable(obj, name) {
  assert(Object.getOwnPropertyDescriptor(obj, name).configurable,
       "Expected obj[" + String(name) + "] to have configurable:true.");
  if (!isConfigurable(obj, name)) {
    print("Expected obj[" + String(name) + "] to be configurable, but was not.");
  }
}

function verifyNotConfigurable(obj, name) {
  assert(!Object.getOwnPropertyDescriptor(obj, name).configurable,
       "Expected obj[" + String(name) + "] to have configurable:false.");
  if (isConfigurable(obj, name)) {
    print("Expected obj[" + String(name) + "] NOT to be configurable, but was.");
  }
}
// Copyright (C) 2016 Jordan Harband.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Used to assert the correctness of object behavior in the presence
    and context of Proxy objects.
---*/

function allowProxyTraps(overrides) {
  function throwTest262Error(msg) {
    return function () { throw new Test262Error(msg); };
  }
  if (!overrides) { overrides = {}; }
  return {
    getPrototypeOf: overrides.getPrototypeOf || throwTest262Error('[[GetPrototypeOf]] trap called'),
    setPrototypeOf: overrides.setPrototypeOf || throwTest262Error('[[SetPrototypeOf]] trap called'),
    isExtensible: overrides.isExtensible || throwTest262Error('[[IsExtensible]] trap called'),
    preventExtensions: overrides.preventExtensions || throwTest262Error('[[PreventExtensions]] trap called'),
    getOwnPropertyDescriptor: overrides.getOwnPropertyDescriptor || throwTest262Error('[[GetOwnProperty]] trap called'),
    has: overrides.has || throwTest262Error('[[HasProperty]] trap called'),
    get: overrides.get || throwTest262Error('[[Get]] trap called'),
    set: overrides.set || throwTest262Error('[[Set]] trap called'),
    deleteProperty: overrides.deleteProperty || throwTest262Error('[[Delete]] trap called'),
    defineProperty: overrides.defineProperty || throwTest262Error('[[DefineOwnProperty]] trap called'),
    enumerate: throwTest262Error('[[Enumerate]] trap called: this trap has been removed'),
    ownKeys: overrides.ownKeys || throwTest262Error('[[OwnPropertyKeys]] trap called'),
    apply: overrides.apply || throwTest262Error('[[Call]] trap called'),
    construct: overrides.construct || throwTest262Error('[[Construct]] trap called')
  };
}
// Copyright (C) 2017 Mathias Bynens.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Collection of functions used to assert the correctness of RegExp objects.
---*/

function buildString({ loneCodePoints, ranges }) {
  const CHUNK_SIZE = 10000;
  let result = String.fromCodePoint(...loneCodePoints);
  for (const [start, end] of ranges) {
    const codePoints = [];
    for (let length = 0, codePoint = start; codePoint <= end; codePoint++) {
      codePoints[length++] = codePoint;
      if (length === CHUNK_SIZE) {
        result += String.fromCodePoint(...codePoints);
        codePoints.length = length = 0;
      }
    }
    result += String.fromCodePoint(...codePoints);
  }
  return result;
}

function testPropertyEscapes(regex, string, expression) {
  if (!regex.test(string)) {
    for (const symbol of string) {
      const hex = symbol
        .codePointAt(0)
        .toString(16)
        .toUpperCase()
        .padStart(6, "0");
      assert(
        regex.test(symbol),
        `\`${ expression }\` should match U+${ hex } (\`${ symbol }\`)`
      );
    }
  }
}

// Returns a function that will validate RegExp match result
//
// Example:
//
//    var validate = matchValidator(['b'], 1, 'abc');
//    validate(/b/.exec('abc'));
//
function matchValidator(expectedEntries, expectedIndex, expectedInput) {
  return function(match) {
    assert.compareArray(match, expectedEntries, 'Match entries');
    assert.sameValue(match.index, expectedIndex, 'Match index');
    assert.sameValue(match.input, expectedInput, 'Match input');
  }
}
// Copyright (c) 2012 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Provides both:

    - An error class to avoid false positives when testing for thrown exceptions
    - A function to explicitly throw an exception using the Test262Error class
---*/


function Test262Error(message) {
  this.message = message || "Test failed";
}

Test262Error.prototype.toString = function () {
  return "Test262Error: " + this.message;
};

var print;
print = function print(message) {
  throw new Test262Error(message);
};
// Copyright (C) 2016 the V8 project authors. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    This defines the number of consecutive recursive function calls that must be
    made in order to prove that stack frames are properly destroyed according to
    ES2015 tail call optimization semantics.
---*/




var $MAX_ITERATIONS = 100000;
// Copyright (C) 2017 Mozilla Corporation. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Collection of functions used to assert the correctness of SharedArrayBuffer objects.
---*/


/**
 * Calls the provided function for a each bad index that should throw a
 * RangeError when passed to an Atomics method on a SAB-backed view where
 * index 125 is out of range.
 *
 * @param f - the function to call for each bad index.
 */
function testWithAtomicsOutOfBoundsIndices(f) {
  var bad_indices = [
    function(view) { return -1; },
    function(view) { return view.length; },
    function(view) { return view.length * 2; },
    function(view) { return Number.POSITIVE_INFINITY; },
    function(view) { return Number.NEGATIVE_INFINITY; },
    function(view) { return { valueOf: function() { return 125; } }; },
    function(view) { return { toString: function() { return '125'; }, valueOf: false }; }, // non-callable valueOf triggers invocation of toString
  ];

  for (var i = 0; i < bad_indices.length; ++i) {
    var IdxGen = bad_indices[i];
    try {
      f(IdxGen);
    } catch (e) {
      e.message += ' (Testing with index gen ' + IdxGen + '.)';
      throw e;
    }
  }
}

/**
 * Calls the provided function for each good index that should not throw when
 * passed to an Atomics method on a SAB-backed view.
 *
 * The view must have length greater than zero.
 *
 * @param f - the function to call for each good index.
 */
function testWithAtomicsInBoundsIndices(f) {
  // Most of these are eventually coerced to +0 by ToIndex.
  var good_indices = [
    function(view) { return 0/-1; },
    function(view) { return '-0'; },
    function(view) { return undefined; },
    function(view) { return NaN; },
    function(view) { return 0.5; },
    function(view) { return '0.5'; },
    function(view) { return -0.9; },
    function(view) { return { password: 'qumquat' }; },
    function(view) { return view.length - 1; },
    function(view) { return { valueOf: function() { return 0; } }; },
    function(view) { return { toString: function() { return '0'; }, valueOf: false }; }, // non-callable valueOf triggers invocation of toString
  ];

  for (var i = 0; i < good_indices.length; ++i) {
    var IdxGen = good_indices[i];
    try {
      f(IdxGen);
    } catch (e) {
      e.message += ' (Testing with index gen ' + IdxGen + '.)';
      throw e;
    }
  }
}

/**
 * Calls the provided function for each value that should throw a TypeError
 * when passed to an Atomics method as a view.
 *
 * @param f - the function to call for each non-view value.
 */

function testWithAtomicsNonViewValues(f) {
  var values = [
    null,
    undefined,
    true,
    false,
    new Boolean(true),
    10,
    3.14,
    new Number(4),
    'Hi there',
    new Date,
    /a*utomaton/g,
    { password: 'qumquat' },
    new DataView(new ArrayBuffer(10)),
    new ArrayBuffer(128),
    new SharedArrayBuffer(128),
    new Error('Ouch'),
    [1,1,2,3,5,8],
    function(x) { return -x; },
    Symbol('halleluja'),
    // TODO: Proxy?
    Object,
    Int32Array,
    Date,
    Math,
    Atomics
  ];

  for (var i = 0; i < values.length; ++i) {
    var nonView = values[i];
    try {
      f(nonView);
    } catch (e) {
      e.message += ' (Testing with non-view value ' + nonView + '.)';
      throw e;
    }
  }
}

// Copyright (C) 2015 André Bargull. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Collection of functions used to assert the correctness of BigInt TypedArray objects.
---*/

/**
 * The %TypedArray% intrinsic constructor function.
 */
var TypedArray = Object.getPrototypeOf(Int8Array);

/**
 * Calls the provided function for every typed array constructor.
 *
 * @param {typedArrayConstructorCallback} f - the function to call for each typed array constructor.
 */
function testWithBigIntTypedArrayConstructors(f) {
  /**
   * Array containing every BigInt typed array constructor.
   */
  var constructors = [
    BigInt64Array,
    BigUint64Array
  ];

  for (var i = 0; i < constructors.length; ++i) {
    var constructor = constructors[i];
    try {
      f(constructor);
    } catch (e) {
      e.message += " (Testing with " + constructor.name + ".)";
      throw e;
    }
  }
}
// Copyright (C) 2011 2012 Norbert Lindenberg. All rights reserved.
// Copyright (C) 2012 2013 Mozilla Corporation. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    This file contains shared functions for the tests in the conformance test
    suite for the ECMAScript Internationalization API.
author: Norbert Lindenberg
---*/

/**
 */


/**
 * @description Calls the provided function for every service constructor in
 * the Intl object.
 * @param {Function} f the function to call for each service constructor in
 *   the Intl object.
 *   @param {Function} Constructor the constructor object to test with.
 */
function testWithIntlConstructors(f) {
  var constructors = ["Collator", "NumberFormat", "DateTimeFormat"];

  // Optionally supported Intl constructors.
  ["PluralRules"].forEach(function(constructor) {
    if (typeof Intl[constructor] === "function") {
      constructors[constructors.length] = constructor;
    }
  });

  constructors.forEach(function (constructor) {
    var Constructor = Intl[constructor];
    try {
      f(Constructor);
    } catch (e) {
      e.message += " (Testing with " + constructor + ".)";
      throw e;
    }
  });
}


/**
 * Taints a named data property of the given object by installing
 * a setter that throws an exception.
 * @param {object} obj the object whose data property to taint
 * @param {string} property the property to taint
 */
function taintDataProperty(obj, property) {
  Object.defineProperty(obj, property, {
    set: function(value) {
      print("Client code can adversely affect behavior: setter for " + property + ".");
    },
    enumerable: false,
    configurable: true
  });
}


/**
 * Taints a named method of the given object by replacing it with a function
 * that throws an exception.
 * @param {object} obj the object whose method to taint
 * @param {string} property the name of the method to taint
 */
function taintMethod(obj, property) {
  Object.defineProperty(obj, property, {
    value: function() {
      print("Client code can adversely affect behavior: method " + property + ".");
    },
    writable: true,
    enumerable: false,
    configurable: true
  });
}


/**
 * Taints the given properties (and similarly named properties) by installing
 * setters on Object.prototype that throw exceptions.
 * @param {Array} properties an array of property names to taint
 */
function taintProperties(properties) {
  properties.forEach(function (property) {
    var adaptedProperties = [property, "__" + property, "_" + property, property + "_", property + "__"];
    adaptedProperties.forEach(function (property) {
      taintDataProperty(Object.prototype, property);
    });
  });
}


/**
 * Taints the Array object by creating a setter for the property "0" and
 * replacing some key methods with functions that throw exceptions.
 */
function taintArray() {
  taintDataProperty(Array.prototype, "0");
  taintMethod(Array.prototype, "indexOf");
  taintMethod(Array.prototype, "join");
  taintMethod(Array.prototype, "push");
  taintMethod(Array.prototype, "slice");
  taintMethod(Array.prototype, "sort");
}


/**
 * Gets locale support info for the given constructor object, which must be one
 * of Intl constructors.
 * @param {object} Constructor the constructor for which to get locale support info
 * @return {object} locale support info with the following properties:
 *   supported: array of fully supported language tags
 *   byFallback: array of language tags that are supported through fallbacks
 *   unsupported: array of unsupported language tags
 */
function getLocaleSupportInfo(Constructor) {
  var languages = ["zh", "es", "en", "hi", "ur", "ar", "ja", "pa"];
  var scripts = ["Latn", "Hans", "Deva", "Arab", "Jpan", "Hant"];
  var countries = ["CN", "IN", "US", "PK", "JP", "TW", "HK", "SG"];

  var allTags = [];
  var i, j, k;
  var language, script, country;
  for (i = 0; i < languages.length; i++) {
    language = languages[i];
    allTags.push(language);
    for (j = 0; j < scripts.length; j++) {
      script = scripts[j];
      allTags.push(language + "-" + script);
      for (k = 0; k < countries.length; k++) {
        country = countries[k];
        allTags.push(language + "-" + script + "-" + country);
      }
    }
    for (k = 0; k < countries.length; k++) {
      country = countries[k];
      allTags.push(language + "-" + country);
    }
  }

  var supported = [];
  var byFallback = [];
  var unsupported = [];
  for (i = 0; i < allTags.length; i++) {
    var request = allTags[i];
    var result = new Constructor([request], {localeMatcher: "lookup"}).resolvedOptions().locale;
    if (request === result) {
      supported.push(request);
    } else if (request.indexOf(result) === 0) {
      byFallback.push(request);
    } else {
      unsupported.push(request);
    }
  }

  return {
    supported: supported,
    byFallback: byFallback,
    unsupported: unsupported
  };
}


/**
 * Returns an array of strings for which IsStructurallyValidLanguageTag() returns false
 */
function getInvalidLanguageTags() {
  var invalidLanguageTags = [
    "", // empty tag
    "i", // singleton alone
    "x", // private use without subtag
    "u", // extension singleton in first place
    "419", // region code in first place
    "u-nu-latn-cu-bob", // extension sequence without language
    "hans-cmn-cn", // "hans" could theoretically be a 4-letter language code,
                   // but those can't be followed by extlang codes.
    "cmn-hans-cn-u-u", // duplicate singleton
    "cmn-hans-cn-t-u-ca-u", // duplicate singleton
    "de-gregory-gregory", // duplicate variant
    "*", // language range
    "de-*", // language range
    "中文", // non-ASCII letters
    "en-ß", // non-ASCII letters
    "ıd", // non-ASCII letters
    "es-Latn-latn", // two scripts
    "pl-PL-pl", // two regions
    "u-ca-gregory", // extension in first place
    "de-1996-1996", // duplicate numeric variant
    "pt-u-ca-gregory-u-nu-latn", // duplicate singleton subtag

    // underscores in different parts of the language tag
    "de_DE",
    "DE_de",
    "cmn_Hans",
    "cmn-hans_cn",
    "es_419",
    "es-419-u-nu-latn-cu_bob",
    "i_klingon",
    "cmn-hans-cn-t-ca-u-ca-x_t-u",
    "enochian_enochian",
    "de-gregory_u-ca-gregory",

    "en\u0000", // null-terminator sequence
    " en", // leading whitespace
    "en ", // trailing whitespace
    "it-IT-Latn", // country before script tag
    "de-u", // incomplete Unicode extension sequences
    "de-u-",
    "de-u-ca-",
    "de-u-ca-gregory-",
    "si-x", // incomplete private-use tags
    "x-",
    "x-y-",
  ];

  // make sure the data above is correct
  for (var i = 0; i < invalidLanguageTags.length; ++i) {
    var invalidTag = invalidLanguageTags[i];
    assert(
      !isCanonicalizedStructurallyValidLanguageTag(invalidTag),
      "Test data \"" + invalidTag + "\" is a canonicalized and structurally valid language tag."
    );
  }

  return invalidLanguageTags;
}


/**
 * @description Tests whether locale is a String value representing a
 * structurally valid and canonicalized BCP 47 language tag, as defined in
 * sections 6.2.2 and 6.2.3 of the ECMAScript Internationalization API
 * Specification.
 * @param {String} locale the string to be tested.
 * @result {Boolean} whether the test succeeded.
 */
function isCanonicalizedStructurallyValidLanguageTag(locale) {

  /**
   * Regular expression defining BCP 47 language tags.
   *
   * Spec: RFC 5646 section 2.1.
   */
  var alpha = "[a-zA-Z]",
    digit = "[0-9]",
    alphanum = "(" + alpha + "|" + digit + ")",
    regular = "(art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu|zh-hakka|zh-min|zh-min-nan|zh-xiang)",
    irregular = "(en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao|i-tay|i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE)",
    grandfathered = "(" + irregular + "|" + regular + ")",
    privateuse = "(x(-[a-z0-9]{1,8})+)",
    singleton = "(" + digit + "|[A-WY-Za-wy-z])",
    extension = "(" + singleton + "(-" + alphanum + "{2,8})+)",
    variant = "(" + alphanum + "{5,8}|(" + digit + alphanum + "{3}))",
    region = "(" + alpha + "{2}|" + digit + "{3})",
    script = "(" + alpha + "{4})",
    extlang = "(" + alpha + "{3}(-" + alpha + "{3}){0,2})",
    language = "(" + alpha + "{2,3}(-" + extlang + ")?|" + alpha + "{4}|" + alpha + "{5,8})",
    langtag = language + "(-" + script + ")?(-" + region + ")?(-" + variant + ")*(-" + extension + ")*(-" + privateuse + ")?",
    languageTag = "^(" + langtag + "|" + privateuse + "|" + grandfathered + ")$",
    languageTagRE = new RegExp(languageTag, "i");
  var duplicateSingleton = "-" + singleton + "-(.*-)?\\1(?!" + alphanum + ")",
    duplicateSingletonRE = new RegExp(duplicateSingleton, "i"),
    duplicateVariant = "(" + alphanum + "{2,8}-)+" + variant + "-(" + alphanum + "{2,8}-)*\\3(?!" + alphanum + ")",
    duplicateVariantRE = new RegExp(duplicateVariant, "i");


  /**
   * Verifies that the given string is a well-formed BCP 47 language tag
   * with no duplicate variant or singleton subtags.
   *
   * Spec: ECMAScript Internationalization API Specification, draft, 6.2.2.
   */
  function isStructurallyValidLanguageTag(locale) {
    if (!languageTagRE.test(locale)) {
      return false;
    }
    locale = locale.split(/-x-/)[0];
    return !duplicateSingletonRE.test(locale) && !duplicateVariantRE.test(locale);
  }


  /**
   * Mappings from complete tags to preferred values.
   *
   * Spec: IANA Language Subtag Registry.
   */
  var __tagMappings = {
    // property names must be in lower case; values in canonical form

    // grandfathered tags from IANA language subtag registry, file date 2018-04-23
    "art-lojban": "jbo",
    "cel-gaulish": "cel-gaulish",
    "en-gb-oed": "en-GB-oxendict",
    "i-ami": "ami",
    "i-bnn": "bnn",
    "i-default": "i-default",
    "i-enochian": "i-enochian",
    "i-hak": "hak",
    "i-klingon": "tlh",
    "i-lux": "lb",
    "i-mingo": "i-mingo",
    "i-navajo": "nv",
    "i-pwn": "pwn",
    "i-tao": "tao",
    "i-tay": "tay",
    "i-tsu": "tsu",
    "no-bok": "nb",
    "no-nyn": "nn",
    "sgn-be-fr": "sfb",
    "sgn-be-nl": "vgt",
    "sgn-ch-de": "sgg",
    "zh-guoyu": "cmn",
    "zh-hakka": "hak",
    "zh-min": "zh-min",
    "zh-min-nan": "nan",
    "zh-xiang": "hsn",
    // deprecated redundant tags from IANA language subtag registry, file date 2018-04-23
    "sgn-br": "bzs",
    "sgn-co": "csn",
    "sgn-de": "gsg",
    "sgn-dk": "dsl",
    "sgn-es": "ssp",
    "sgn-fr": "fsl",
    "sgn-gb": "bfi",
    "sgn-gr": "gss",
    "sgn-ie": "isg",
    "sgn-it": "ise",
    "sgn-jp": "jsl",
    "sgn-mx": "mfs",
    "sgn-ni": "ncs",
    "sgn-nl": "dse",
    "sgn-no": "nsl",
    "sgn-pt": "psr",
    "sgn-se": "swl",
    "sgn-us": "ase",
    "sgn-za": "sfs",
    "zh-cmn": "cmn",
    "zh-cmn-hans": "cmn-Hans",
    "zh-cmn-hant": "cmn-Hant",
    "zh-gan": "gan",
    "zh-wuu": "wuu",
    "zh-yue": "yue",
    // deprecated variant with prefix from IANA language subtag registry, file date 2018-04-23
    "ja-latn-hepburn-heploc": "ja-Latn-alalc97"
  };


  /**
   * Mappings from non-extlang subtags to preferred values.
   *
   * Spec: IANA Language Subtag Registry.
   */
  var __subtagMappings = {
    // property names and values must be in canonical case
    // language subtags with Preferred-Value mappings from IANA language subtag registry, file date 2018-04-23
    "in": "id",
    "iw": "he",
    "ji": "yi",
    "jw": "jv",
    "mo": "ro",
    "aam": "aas",
    "adp": "dz",
    "aue": "ktz",
    "ayx": "nun",
    "bgm": "bcg",
    "bjd": "drl",
    "ccq": "rki",
    "cjr": "mom",
    "cka": "cmr",
    "cmk": "xch",
    "coy": "pij",
    "cqu": "quh",
    "drh": "khk",
    "drw": "prs",
    "gav": "dev",
    "gfx": "vaj",
    "ggn": "gvr",
    "gti": "nyc",
    "guv": "duz",
    "hrr": "jal",
    "ibi": "opa",
    "ilw": "gal",
    "jeg": "oyb",
    "kgc": "tdf",
    "kgh": "kml",
    "koj": "kwv",
    "krm": "bmf",
    "ktr": "dtp",
    "kvs": "gdj",
    "kwq": "yam",
    "kxe": "tvd",
    "kzj": "dtp",
    "kzt": "dtp",
    "lii": "raq",
    "lmm": "rmx",
    "meg": "cir",
    "mst": "mry",
    "mwj": "vaj",
    "myt": "mry",
    "nad": "xny",
    "ncp": "kdz",
    "nnx": "ngv",
    "nts": "pij",
    "oun": "vaj",
    "pcr": "adx",
    "pmc": "huw",
    "pmu": "phr",
    "ppa": "bfy",
    "ppr": "lcq",
    "pry": "prt",
    "puz": "pub",
    "sca": "hle",
    "skk": "oyb",
    "tdu": "dtp",
    "thc": "tpo",
    "thx": "oyb",
    "tie": "ras",
    "tkk": "twm",
    "tlw": "weo",
    "tmp": "tyj",
    "tne": "kak",
    "tnf": "prs",
    "tsf": "taj",
    "uok": "ema",
    "xba": "cax",
    "xia": "acn",
    "xkh": "waw",
    "xsj": "suj",
    "ybd": "rki",
    "yma": "lrr",
    "ymt": "mtm",
    "yos": "zom",
    "yuu": "yug",
    // region subtags with Preferred-Value mappings from IANA language subtag registry, file date 2018-04-23
    "BU": "MM",
    "DD": "DE",
    "FX": "FR",
    "TP": "TL",
    "YD": "YE",
    "ZR": "CD"
  };


  /**
   * Mappings from extlang subtags to preferred values.
   *
   * Spec: IANA Language Subtag Registry.
   */
  var __extlangMappings = {
    // extlang subtags with Preferred-Value mappings from IANA language subtag registry, file date 2018-04-23
    // values are arrays with [0] the replacement value, [1] (if present) the prefix to be removed
    "aao": ["aao", "ar"],
    "abh": ["abh", "ar"],
    "abv": ["abv", "ar"],
    "acm": ["acm", "ar"],
    "acq": ["acq", "ar"],
    "acw": ["acw", "ar"],
    "acx": ["acx", "ar"],
    "acy": ["acy", "ar"],
    "adf": ["adf", "ar"],
    "ads": ["ads", "sgn"],
    "aeb": ["aeb", "ar"],
    "aec": ["aec", "ar"],
    "aed": ["aed", "sgn"],
    "aen": ["aen", "sgn"],
    "afb": ["afb", "ar"],
    "afg": ["afg", "sgn"],
    "ajp": ["ajp", "ar"],
    "apc": ["apc", "ar"],
    "apd": ["apd", "ar"],
    "arb": ["arb", "ar"],
    "arq": ["arq", "ar"],
    "ars": ["ars", "ar"],
    "ary": ["ary", "ar"],
    "arz": ["arz", "ar"],
    "ase": ["ase", "sgn"],
    "asf": ["asf", "sgn"],
    "asp": ["asp", "sgn"],
    "asq": ["asq", "sgn"],
    "asw": ["asw", "sgn"],
    "auz": ["auz", "ar"],
    "avl": ["avl", "ar"],
    "ayh": ["ayh", "ar"],
    "ayl": ["ayl", "ar"],
    "ayn": ["ayn", "ar"],
    "ayp": ["ayp", "ar"],
    "bbz": ["bbz", "ar"],
    "bfi": ["bfi", "sgn"],
    "bfk": ["bfk", "sgn"],
    "bjn": ["bjn", "ms"],
    "bog": ["bog", "sgn"],
    "bqn": ["bqn", "sgn"],
    "bqy": ["bqy", "sgn"],
    "btj": ["btj", "ms"],
    "bve": ["bve", "ms"],
    "bvl": ["bvl", "sgn"],
    "bvu": ["bvu", "ms"],
    "bzs": ["bzs", "sgn"],
    "cdo": ["cdo", "zh"],
    "cds": ["cds", "sgn"],
    "cjy": ["cjy", "zh"],
    "cmn": ["cmn", "zh"],
    "coa": ["coa", "ms"],
    "cpx": ["cpx", "zh"],
    "csc": ["csc", "sgn"],
    "csd": ["csd", "sgn"],
    "cse": ["cse", "sgn"],
    "csf": ["csf", "sgn"],
    "csg": ["csg", "sgn"],
    "csl": ["csl", "sgn"],
    "csn": ["csn", "sgn"],
    "csq": ["csq", "sgn"],
    "csr": ["csr", "sgn"],
    "czh": ["czh", "zh"],
    "czo": ["czo", "zh"],
    "doq": ["doq", "sgn"],
    "dse": ["dse", "sgn"],
    "dsl": ["dsl", "sgn"],
    "dup": ["dup", "ms"],
    "ecs": ["ecs", "sgn"],
    "esl": ["esl", "sgn"],
    "esn": ["esn", "sgn"],
    "eso": ["eso", "sgn"],
    "eth": ["eth", "sgn"],
    "fcs": ["fcs", "sgn"],
    "fse": ["fse", "sgn"],
    "fsl": ["fsl", "sgn"],
    "fss": ["fss", "sgn"],
    "gan": ["gan", "zh"],
    "gds": ["gds", "sgn"],
    "gom": ["gom", "kok"],
    "gse": ["gse", "sgn"],
    "gsg": ["gsg", "sgn"],
    "gsm": ["gsm", "sgn"],
    "gss": ["gss", "sgn"],
    "gus": ["gus", "sgn"],
    "hab": ["hab", "sgn"],
    "haf": ["haf", "sgn"],
    "hak": ["hak", "zh"],
    "hds": ["hds", "sgn"],
    "hji": ["hji", "ms"],
    "hks": ["hks", "sgn"],
    "hos": ["hos", "sgn"],
    "hps": ["hps", "sgn"],
    "hsh": ["hsh", "sgn"],
    "hsl": ["hsl", "sgn"],
    "hsn": ["hsn", "zh"],
    "icl": ["icl", "sgn"],
    "iks": ["iks", "sgn"],
    "ils": ["ils", "sgn"],
    "inl": ["inl", "sgn"],
    "ins": ["ins", "sgn"],
    "ise": ["ise", "sgn"],
    "isg": ["isg", "sgn"],
    "isr": ["isr", "sgn"],
    "jak": ["jak", "ms"],
    "jax": ["jax", "ms"],
    "jcs": ["jcs", "sgn"],
    "jhs": ["jhs", "sgn"],
    "jls": ["jls", "sgn"],
    "jos": ["jos", "sgn"],
    "jsl": ["jsl", "sgn"],
    "jus": ["jus", "sgn"],
    "kgi": ["kgi", "sgn"],
    "knn": ["knn", "kok"],
    "kvb": ["kvb", "ms"],
    "kvk": ["kvk", "sgn"],
    "kvr": ["kvr", "ms"],
    "kxd": ["kxd", "ms"],
    "lbs": ["lbs", "sgn"],
    "lce": ["lce", "ms"],
    "lcf": ["lcf", "ms"],
    "liw": ["liw", "ms"],
    "lls": ["lls", "sgn"],
    "lsg": ["lsg", "sgn"],
    "lsl": ["lsl", "sgn"],
    "lso": ["lso", "sgn"],
    "lsp": ["lsp", "sgn"],
    "lst": ["lst", "sgn"],
    "lsy": ["lsy", "sgn"],
    "ltg": ["ltg", "lv"],
    "lvs": ["lvs", "lv"],
    "lws": ["lws", "sgn"],
    "lzh": ["lzh", "zh"],
    "max": ["max", "ms"],
    "mdl": ["mdl", "sgn"],
    "meo": ["meo", "ms"],
    "mfa": ["mfa", "ms"],
    "mfb": ["mfb", "ms"],
    "mfs": ["mfs", "sgn"],
    "min": ["min", "ms"],
    "mnp": ["mnp", "zh"],
    "mqg": ["mqg", "ms"],
    "mre": ["mre", "sgn"],
    "msd": ["msd", "sgn"],
    "msi": ["msi", "ms"],
    "msr": ["msr", "sgn"],
    "mui": ["mui", "ms"],
    "mzc": ["mzc", "sgn"],
    "mzg": ["mzg", "sgn"],
    "mzy": ["mzy", "sgn"],
    "nan": ["nan", "zh"],
    "nbs": ["nbs", "sgn"],
    "ncs": ["ncs", "sgn"],
    "nsi": ["nsi", "sgn"],
    "nsl": ["nsl", "sgn"],
    "nsp": ["nsp", "sgn"],
    "nsr": ["nsr", "sgn"],
    "nzs": ["nzs", "sgn"],
    "okl": ["okl", "sgn"],
    "orn": ["orn", "ms"],
    "ors": ["ors", "ms"],
    "pel": ["pel", "ms"],
    "pga": ["pga", "ar"],
    "pgz": ["pgz", "sgn"],
    "pks": ["pks", "sgn"],
    "prl": ["prl", "sgn"],
    "prz": ["prz", "sgn"],
    "psc": ["psc", "sgn"],
    "psd": ["psd", "sgn"],
    "pse": ["pse", "ms"],
    "psg": ["psg", "sgn"],
    "psl": ["psl", "sgn"],
    "pso": ["pso", "sgn"],
    "psp": ["psp", "sgn"],
    "psr": ["psr", "sgn"],
    "pys": ["pys", "sgn"],
    "rms": ["rms", "sgn"],
    "rsi": ["rsi", "sgn"],
    "rsl": ["rsl", "sgn"],
    "rsm": ["rsm", "sgn"],
    "sdl": ["sdl", "sgn"],
    "sfb": ["sfb", "sgn"],
    "sfs": ["sfs", "sgn"],
    "sgg": ["sgg", "sgn"],
    "sgx": ["sgx", "sgn"],
    "shu": ["shu", "ar"],
    "slf": ["slf", "sgn"],
    "sls": ["sls", "sgn"],
    "sqk": ["sqk", "sgn"],
    "sqs": ["sqs", "sgn"],
    "ssh": ["ssh", "ar"],
    "ssp": ["ssp", "sgn"],
    "ssr": ["ssr", "sgn"],
    "svk": ["svk", "sgn"],
    "swc": ["swc", "sw"],
    "swh": ["swh", "sw"],
    "swl": ["swl", "sgn"],
    "syy": ["syy", "sgn"],
    "szs": ["szs", "sgn"],
    "tmw": ["tmw", "ms"],
    "tse": ["tse", "sgn"],
    "tsm": ["tsm", "sgn"],
    "tsq": ["tsq", "sgn"],
    "tss": ["tss", "sgn"],
    "tsy": ["tsy", "sgn"],
    "tza": ["tza", "sgn"],
    "ugn": ["ugn", "sgn"],
    "ugy": ["ugy", "sgn"],
    "ukl": ["ukl", "sgn"],
    "uks": ["uks", "sgn"],
    "urk": ["urk", "ms"],
    "uzn": ["uzn", "uz"],
    "uzs": ["uzs", "uz"],
    "vgt": ["vgt", "sgn"],
    "vkk": ["vkk", "ms"],
    "vkt": ["vkt", "ms"],
    "vsi": ["vsi", "sgn"],
    "vsl": ["vsl", "sgn"],
    "vsv": ["vsv", "sgn"],
    "wbs": ["wbs", "sgn"],
    "wuu": ["wuu", "zh"],
    "xki": ["xki", "sgn"],
    "xml": ["xml", "sgn"],
    "xmm": ["xmm", "ms"],
    "xms": ["xms", "sgn"],
    "yds": ["yds", "sgn"],
    "ygs": ["ygs", "sgn"],
    "yhs": ["yhs", "sgn"],
    "ysl": ["ysl", "sgn"],
    "yue": ["yue", "zh"],
    "zib": ["zib", "sgn"],
    "zlm": ["zlm", "ms"],
    "zmi": ["zmi", "ms"],
    "zsl": ["zsl", "sgn"],
    "zsm": ["zsm", "ms"],
  };


  /**
   * Canonicalizes the given well-formed BCP 47 language tag, including regularized case of subtags.
   *
   * Spec: ECMAScript Internationalization API Specification, draft, 6.2.3.
   * Spec: RFC 5646, section 4.5.
   */
  function canonicalizeLanguageTag(locale) {

    // start with lower case for easier processing, and because most subtags will need to be lower case anyway
    locale = locale.toLowerCase();

    // handle mappings for complete tags
    if (__tagMappings.hasOwnProperty(locale)) {
      return __tagMappings[locale];
    }

    var subtags = locale.split("-");
    var i = 0;

    // handle standard part: all subtags before first singleton or "x"
    while (i < subtags.length) {
      var subtag = subtags[i];
      if (subtag.length === 1 && (i > 0 || subtag === "x")) {
        break;
      } else if (i !== 0 && subtag.length === 2) {
        subtag = subtag.toUpperCase();
      } else if (subtag.length === 4) {
        subtag = subtag[0].toUpperCase() + subtag.substring(1).toLowerCase();
      }
      if (__subtagMappings.hasOwnProperty(subtag)) {
        subtag = __subtagMappings[subtag];
      } else if (__extlangMappings.hasOwnProperty(subtag)) {
        subtag = __extlangMappings[subtag][0];
        if (i === 1 && __extlangMappings[subtag][1] === subtags[0]) {
          subtags.shift();
          i--;
        }
      }
      subtags[i] = subtag;
      i++;
    }
    var normal = subtags.slice(0, i).join("-");

    // handle extensions
    var extensions = [];
    while (i < subtags.length && subtags[i] !== "x") {
      var extensionStart = i;
      i++;
      while (i < subtags.length && subtags[i].length > 1) {
        i++;
      }
      var extension = subtags.slice(extensionStart, i).join("-");
      extensions.push(extension);
    }
    extensions.sort();

    // handle private use
    var privateUse;
    if (i < subtags.length) {
      privateUse = subtags.slice(i).join("-");
    }

    // put everything back together
    var canonical = normal;
    if (extensions.length > 0) {
      canonical += "-" + extensions.join("-");
    }
    if (privateUse !== undefined) {
      if (canonical.length > 0) {
        canonical += "-" + privateUse;
      } else {
        canonical = privateUse;
      }
    }

    return canonical;
  }

  return typeof locale === "string" && isStructurallyValidLanguageTag(locale) &&
      canonicalizeLanguageTag(locale) === locale;
}


/**
 * Returns an array of error cases handled by CanonicalizeLocaleList().
 */
function getInvalidLocaleArguments() {
  function CustomError() {}

  var topLevelErrors = [
    // fails ToObject
    [null, TypeError],

    // fails Get
    [{ get length() { throw new CustomError(); } }, CustomError],

    // fail ToLength
    [{ length: Symbol.toPrimitive }, TypeError],
    [{ length: { get [Symbol.toPrimitive]() { throw new CustomError(); } } }, CustomError],
    [{ length: { [Symbol.toPrimitive]() { throw new CustomError(); } } }, CustomError],
    [{ length: { get valueOf() { throw new CustomError(); } } }, CustomError],
    [{ length: { valueOf() { throw new CustomError(); } } }, CustomError],
    [{ length: { get toString() { throw new CustomError(); } } }, CustomError],
    [{ length: { toString() { throw new CustomError(); } } }, CustomError],

    // fail type check
    [[undefined], TypeError],
    [[null], TypeError],
    [[true], TypeError],
    [[Symbol.toPrimitive], TypeError],
    [[1], TypeError],
    [[0.1], TypeError],
    [[NaN], TypeError],
  ];

  var invalidLanguageTags = [
    "", // empty tag
    "i", // singleton alone
    "x", // private use without subtag
    "u", // extension singleton in first place
    "419", // region code in first place
    "u-nu-latn-cu-bob", // extension sequence without language
    "hans-cmn-cn", // "hans" could theoretically be a 4-letter language code,
                   // but those can't be followed by extlang codes.
    "cmn-hans-cn-u-u", // duplicate singleton
    "cmn-hans-cn-t-u-ca-u", // duplicate singleton
    "de-gregory-gregory", // duplicate variant
    "*", // language range
    "de-*", // language range
    "中文", // non-ASCII letters
    "en-ß", // non-ASCII letters
    "ıd" // non-ASCII letters
  ];

  return topLevelErrors.concat(
    invalidLanguageTags.map(tag => [tag, RangeError]),
    invalidLanguageTags.map(tag => [[tag], RangeError]),
    invalidLanguageTags.map(tag => [["en", tag], RangeError]),
  )
}

/**
 * Tests whether the named options property is correctly handled by the given constructor.
 * @param {object} Constructor the constructor to test.
 * @param {string} property the name of the options property to test.
 * @param {string} type the type that values of the property are expected to have
 * @param {Array} [values] an array of allowed values for the property. Not needed for boolean.
 * @param {any} fallback the fallback value that the property assumes if not provided.
 * @param {object} testOptions additional options:
 *   @param {boolean} isOptional whether support for this property is optional for implementations.
 *   @param {boolean} noReturn whether the resulting value of the property is not returned.
 *   @param {boolean} isILD whether the resulting value of the property is implementation and locale dependent.
 *   @param {object} extra additional option to pass along, properties are value -> {option: value}.
 */
function testOption(Constructor, property, type, values, fallback, testOptions) {
  var isOptional = testOptions !== undefined && testOptions.isOptional === true;
  var noReturn = testOptions !== undefined && testOptions.noReturn === true;
  var isILD = testOptions !== undefined && testOptions.isILD === true;

  function addExtraOptions(options, value, testOptions) {
    if (testOptions !== undefined && testOptions.extra !== undefined) {
      var extra;
      if (value !== undefined && testOptions.extra[value] !== undefined) {
        extra = testOptions.extra[value];
      } else if (testOptions.extra.any !== undefined) {
        extra = testOptions.extra.any;
      }
      if (extra !== undefined) {
        Object.getOwnPropertyNames(extra).forEach(function (prop) {
          options[prop] = extra[prop];
        });
      }
    }
  }

  var testValues, options, obj, expected, actual, error;

  // test that the specified values are accepted. Also add values that convert to specified values.
  if (type === "boolean") {
    if (values === undefined) {
      values = [true, false];
    }
    testValues = values.slice(0);
    testValues.push(888);
    testValues.push(0);
  } else if (type === "string") {
    testValues = values.slice(0);
    testValues.push({toString: function () { return values[0]; }});
  }
  testValues.forEach(function (value) {
    options = {};
    options[property] = value;
    addExtraOptions(options, value, testOptions);
    obj = new Constructor(undefined, options);
    if (noReturn) {
      if (obj.resolvedOptions().hasOwnProperty(property)) {
        print("Option property " + property + " is returned, but shouldn't be.");
      }
    } else {
      actual = obj.resolvedOptions()[property];
      if (isILD) {
        if (actual !== undefined && values.indexOf(actual) === -1) {
          print("Invalid value " + actual + " returned for property " + property + ".");
        }
      } else {
        if (type === "boolean") {
          expected = Boolean(value);
        } else if (type === "string") {
          expected = String(value);
        }
        if (actual !== expected && !(isOptional && actual === undefined)) {
          print("Option value " + value + " for property " + property +
            " was not accepted; got " + actual + " instead.");
        }
      }
    }
  });

  // test that invalid values are rejected
  if (type === "string") {
    var invalidValues = ["invalidValue", -1, null];
    // assume that we won't have values in caseless scripts
    if (values[0].toUpperCase() !== values[0]) {
      invalidValues.push(values[0].toUpperCase());
    } else {
      invalidValues.push(values[0].toLowerCase());
    }
    invalidValues.forEach(function (value) {
      options = {};
      options[property] = value;
      addExtraOptions(options, value, testOptions);
      error = undefined;
      try {
        obj = new Constructor(undefined, options);
      } catch (e) {
        error = e;
      }
      if (error === undefined) {
        print("Invalid option value " + value + " for property " + property + " was not rejected.");
      } else if (error.name !== "RangeError") {
        print("Invalid option value " + value + " for property " + property + " was rejected with wrong error " + error.name + ".");
      }
    });
  }

  // test that fallback value or another valid value is used if no options value is provided
  if (!noReturn) {
    options = {};
    addExtraOptions(options, undefined, testOptions);
    obj = new Constructor(undefined, options);
    actual = obj.resolvedOptions()[property];
    if (!(isOptional && actual === undefined)) {
      if (fallback !== undefined) {
        if (actual !== fallback) {
          print("Option fallback value " + fallback + " for property " + property +
            " was not used; got " + actual + " instead.");
        }
      } else {
        if (values.indexOf(actual) === -1 && !(isILD && actual === undefined)) {
          print("Invalid value " + actual + " returned for property " + property + ".");
        }
      }
    }
  }
}


/**
 * Properties of the RegExp constructor that may be affected by use of regular
 * expressions, and the default values of these properties. Properties are from
 * https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Deprecated_and_obsolete_features#RegExp_Properties
 */
var regExpProperties = ["$1", "$2", "$3", "$4", "$5", "$6", "$7", "$8", "$9",
  "$_", "$*", "$&", "$+", "$`", "$'",
  "input", "lastMatch", "lastParen", "leftContext", "rightContext"
];

var regExpPropertiesDefaultValues = (function () {
  var values = Object.create(null);
  regExpProperties.forEach(function (property) {
    values[property] = RegExp[property];
  });
  return values;
}());


/**
 * Tests that executing the provided function (which may use regular expressions
 * in its implementation) does not create or modify unwanted properties on the
 * RegExp constructor.
 */
function testForUnwantedRegExpChanges(testFunc) {
  regExpProperties.forEach(function (property) {
    RegExp[property] = regExpPropertiesDefaultValues[property];
  });
  testFunc();
  regExpProperties.forEach(function (property) {
    if (RegExp[property] !== regExpPropertiesDefaultValues[property]) {
      print("RegExp has unexpected property " + property + " with value " +
        RegExp[property] + ".");
    }
  });
}


/**
 * Tests whether name is a valid BCP 47 numbering system name
 * and not excluded from use in the ECMAScript Internationalization API.
 * @param {string} name the name to be tested.
 * @return {boolean} whether name is a valid BCP 47 numbering system name and
 *   allowed for use in the ECMAScript Internationalization API.
 */

function isValidNumberingSystem(name) {

  // source: CLDR file common/bcp47/number.xml; version CLDR 32.
  var numberingSystems = [
    "adlm",
    "ahom",
    "arab",
    "arabext",
    "armn",
    "armnlow",
    "bali",
    "beng",
    "bhks",
    "brah",
    "cakm",
    "cham",
    "cyrl",
    "deva",
    "ethi",
    "finance",
    "fullwide",
    "geor",
    "gonm",
    "grek",
    "greklow",
    "gujr",
    "guru",
    "hanidays",
    "hanidec",
    "hans",
    "hansfin",
    "hant",
    "hantfin",
    "hebr",
    "hmng",
    "java",
    "jpan",
    "jpanfin",
    "kali",
    "khmr",
    "knda",
    "lana",
    "lanatham",
    "laoo",
    "latn",
    "lepc",
    "limb",
    "mathbold",
    "mathdbl",
    "mathmono",
    "mathsanb",
    "mathsans",
    "mlym",
    "modi",
    "mong",
    "mroo",
    "mtei",
    "mymr",
    "mymrshan",
    "mymrtlng",
    "native",
    "newa",
    "nkoo",
    "olck",
    "orya",
    "osma",
    "roman",
    "romanlow",
    "saur",
    "shrd",
    "sind",
    "sinh",
    "sora",
    "sund",
    "takr",
    "talu",
    "taml",
    "tamldec",
    "telu",
    "thai",
    "tirh",
    "tibt",
    "traditio",
    "vaii",
    "wara",
  ];

  var excluded = [
    "finance",
    "native",
    "traditio"
  ];


  return numberingSystems.indexOf(name) !== -1 && excluded.indexOf(name) === -1;
}


/**
 * Provides the digits of numbering systems with simple digit mappings,
 * as specified in 11.3.2.
 */

var numberingSystemDigits = {
  arab: "٠١٢٣٤٥٦٧٨٩",
  arabext: "۰۱۲۳۴۵۶۷۸۹",
  bali: "\u1B50\u1B51\u1B52\u1B53\u1B54\u1B55\u1B56\u1B57\u1B58\u1B59",
  beng: "০১২৩৪৫৬৭৮৯",
  deva: "०१२३४५६७८९",
  fullwide: "０１２３４５６７８９",
  gujr: "૦૧૨૩૪૫૬૭૮૯",
  guru: "੦੧੨੩੪੫੬੭੮੯",
  hanidec: "〇一二三四五六七八九",
  khmr: "០១២៣៤៥៦៧៨៩",
  knda: "೦೧೨೩೪೫೬೭೮೯",
  laoo: "໐໑໒໓໔໕໖໗໘໙",
  latn: "0123456789",
  limb: "\u1946\u1947\u1948\u1949\u194A\u194B\u194C\u194D\u194E\u194F",
  mlym: "൦൧൨൩൪൫൬൭൮൯",
  mong: "᠐᠑᠒᠓᠔᠕᠖᠗᠘᠙",
  mymr: "၀၁၂၃၄၅၆၇၈၉",
  orya: "୦୧୨୩୪୫୬୭୮୯",
  tamldec: "௦௧௨௩௪௫௬௭௮௯",
  telu: "౦౧౨౩౪౫౬౭౮౯",
  thai: "๐๑๒๓๔๕๖๗๘๙",
  tibt: "༠༡༢༣༤༥༦༧༨༩"
};


/**
 * Tests that number formatting is handled correctly. The function checks that the
 * digit sequences in formatted output are as specified, converted to the
 * selected numbering system, and embedded in consistent localized patterns.
 * @param {Array} locales the locales to be tested.
 * @param {Array} numberingSystems the numbering systems to be tested.
 * @param {Object} options the options to pass to Intl.NumberFormat. Options
 *   must include {useGrouping: false}, and must cause 1.1 to be formatted
 *   pre- and post-decimal digits.
 * @param {Object} testData maps input data (in ES5 9.3.1 format) to expected output strings
 *   in unlocalized format with Western digits.
 */

function testNumberFormat(locales, numberingSystems, options, testData) {
  locales.forEach(function (locale) {
    numberingSystems.forEach(function (numbering) {
      var digits = numberingSystemDigits[numbering];
      var format = new Intl.NumberFormat([locale + "-u-nu-" + numbering], options);

      function getPatternParts(positive) {
        var n = positive ? 1.1 : -1.1;
        var formatted = format.format(n);
        var oneoneRE = "([^" + digits + "]*)[" + digits + "]+([^" + digits + "]+)[" + digits + "]+([^" + digits + "]*)";
        var match = formatted.match(new RegExp(oneoneRE));
        if (match === null) {
          print("Unexpected formatted " + n + " for " +
            format.resolvedOptions().locale + " and options " +
            JSON.stringify(options) + ": " + formatted);
        }
        return match;
      }

      function toNumbering(raw) {
        return raw.replace(/[0-9]/g, function (digit) {
          return digits[digit.charCodeAt(0) - "0".charCodeAt(0)];
        });
      }

      function buildExpected(raw, patternParts) {
        var period = raw.indexOf(".");
        if (period === -1) {
          return patternParts[1] + toNumbering(raw) + patternParts[3];
        } else {
          return patternParts[1] +
            toNumbering(raw.substring(0, period)) +
            patternParts[2] +
            toNumbering(raw.substring(period + 1)) +
            patternParts[3];
        }
      }

      if (format.resolvedOptions().numberingSystem === numbering) {
        // figure out prefixes, infixes, suffixes for positive and negative values
        var posPatternParts = getPatternParts(true);
        var negPatternParts = getPatternParts(false);

        Object.getOwnPropertyNames(testData).forEach(function (input) {
          var rawExpected = testData[input];
          var patternParts;
          if (rawExpected[0] === "-") {
            patternParts = negPatternParts;
            rawExpected = rawExpected.substring(1);
          } else {
            patternParts = posPatternParts;
          }
          var expected = buildExpected(rawExpected, patternParts);
          var actual = format.format(input);
          if (actual !== expected) {
            print("Formatted value for " + input + ", " +
            format.resolvedOptions().locale + " and options " +
            JSON.stringify(options) + " is " + actual + "; expected " + expected + ".");
          }
        });
      }
    });
  });
}


/**
 * Return the components of date-time formats.
 * @return {Array} an array with all date-time components.
 */

function getDateTimeComponents() {
  return ["weekday", "era", "year", "month", "day", "hour", "minute", "second", "timeZoneName"];
}


/**
 * Return the valid values for the given date-time component, as specified
 * by the table in section 12.1.1.
 * @param {string} component a date-time component.
 * @return {Array} an array with the valid values for the component.
 */

function getDateTimeComponentValues(component) {

  var components = {
    weekday: ["narrow", "short", "long"],
    era: ["narrow", "short", "long"],
    year: ["2-digit", "numeric"],
    month: ["2-digit", "numeric", "narrow", "short", "long"],
    day: ["2-digit", "numeric"],
    hour: ["2-digit", "numeric"],
    minute: ["2-digit", "numeric"],
    second: ["2-digit", "numeric"],
    timeZoneName: ["short", "long"]
  };

  var result = components[component];
  if (result === undefined) {
    print("Internal error: No values defined for date-time component " + component + ".");
  }
  return result;
}


/**
 * @description Tests whether timeZone is a String value representing a
 * structurally valid and canonicalized time zone name, as defined in
 * sections 6.4.1 and 6.4.2 of the ECMAScript Internationalization API
 * Specification.
 * @param {String} timeZone the string to be tested.
 * @result {Boolean} whether the test succeeded.
 */

function isCanonicalizedStructurallyValidTimeZoneName(timeZone) {
  /**
   * Regular expression defining IANA Time Zone names.
   *
   * Spec: IANA Time Zone Database, Theory file
   */
  var fileNameComponent = "(?:[A-Za-z_]|\\.(?!\\.?(?:/|$)))[A-Za-z.\\-_]{0,13}";
  var fileName = fileNameComponent + "(?:/" + fileNameComponent + ")*";
  var etcName = "(?:Etc/)?GMT[+-]\\d{1,2}";
  var systemVName = "SystemV/[A-Z]{3}\\d{1,2}(?:[A-Z]{3})?";
  var legacyName = etcName + "|" + systemVName + "|CST6CDT|EST5EDT|MST7MDT|PST8PDT|NZ";
  var zoneNamePattern = new RegExp("^(?:" + fileName + "|" + legacyName + ")$");

  if (typeof timeZone !== "string") {
    return false;
  }
  // 6.4.2 CanonicalizeTimeZoneName (timeZone), step 3
  if (timeZone === "UTC") {
    return true;
  }
  // 6.4.2 CanonicalizeTimeZoneName (timeZone), step 3
  if (timeZone === "Etc/UTC" || timeZone === "Etc/GMT") {
    return false;
  }
  return zoneNamePattern.test(timeZone);
}
// Copyright (C) 2015 André Bargull. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Collection of functions used to assert the correctness of TypedArray objects.
---*/

/**
 * Array containing every typed array constructor.
 */
var typedArrayConstructors = [
  Float64Array,
  Float32Array,
  Int32Array,
  Int16Array,
  Int8Array,
  Uint32Array,
  Uint16Array,
  Uint8Array,
  Uint8ClampedArray
];

var floatArrayConstructors = typedArrayConstructors.slice(0, 2);
var intArrayConstructors = typedArrayConstructors.slice(2, 7);

/**
 * The %TypedArray% intrinsic constructor function.
 */
var TypedArray = Object.getPrototypeOf(Int8Array);

/**
 * Callback for testing a typed array constructor.
 *
 * @callback typedArrayConstructorCallback
 * @param {Function} Constructor the constructor object to test with.
 */

/**
 * Calls the provided function for every typed array constructor.
 *
 * @param {typedArrayConstructorCallback} f - the function to call for each typed array constructor.
 * @param {Array} selected - An optional Array with filtered typed arrays
 */
function testWithTypedArrayConstructors(f, selected) {
  var constructors = selected || typedArrayConstructors;
  for (var i = 0; i < constructors.length; ++i) {
    var constructor = constructors[i];
    try {
      f(constructor);
    } catch (e) {
      e.message += " (Testing with " + constructor.name + ".)";
      throw e;
    }
  }
}

/**
 * Helper for conversion operations on TypedArrays, the expected values
 * properties are indexed in order to match the respective value for each
 * TypedArray constructor
 * @param  {Function} fn - the function to call for each constructor and value.
 *                         will be called with the constructor, value, expected
 *                         value, and a initial value that can be used to avoid
 *                         a false positive with an equivalent expected value.
 */
function testTypedArrayConversions(byteConversionValues, fn) {
  var values = byteConversionValues.values;
  var expected = byteConversionValues.expected;

  testWithTypedArrayConstructors(function(TA) {
    var name = TA.name.slice(0, -5);

    return values.forEach(function(value, index) {
      var exp = expected[name][index];
      var initial = 0;
      if (exp === 0) {
        initial = 1;
      }
      fn(TA, value, exp, initial);
    });
  });
}
// Copyright (C) 2017 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Used in website/scripts/sth.js
---*/
//setTimeout is not available, hence this script was loaded
if (Promise === undefined && this.setTimeout === undefined) {
  if(/\$DONE()/.test(code))
    print("Async test capability is not supported in your test environment");
}

if (Promise !== undefined && this.setTimeout === undefined) {
  (function(that) {
     that.setTimeout = function(callback, delay) {
      var p = Promise.resolve();
      var start = Date.now();
      var end = start + delay;
      function check(){
        var timeLeft = end - Date.now();
        if(timeLeft > 0)
          p.then(check);
        else
          callback();
      }
      p.then(check);
    }
  })(this);
}
// Copyright (C) 2017 Josh Wolfe. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    Functions to help generate test cases for testing type coercion abstract
    operations like ToNumber.
---*/

function testCoercibleToIndexZero(test) {
  testCoercibleToIntegerZero(test);
}

function testCoercibleToIndexOne(test) {
  testCoercibleToIntegerOne(test);
}

function testCoercibleToIndexFromIndex(nominalIndex, test) {
  assert(Number.isInteger(nominalIndex));
  assert(0 <= nominalIndex && nominalIndex <= 2**53 - 1);
  testCoercibleToIntegerFromInteger(nominalIndex, test);
}

function testCoercibleToIntegerZero(test) {
  testCoercibleToNumberZero(test);

  testCoercibleToIntegerFromInteger(0, test);

  // NaN -> +0
  testCoercibleToNumberNan(test);

  // When toString() returns a string that parses to NaN:
  test({});
  test([]);
}

function testCoercibleToIntegerOne(test) {
  testCoercibleToNumberOne(test);

  testCoercibleToIntegerFromInteger(1, test);

  // When toString() returns "1"
  test([1]);
  test(["1"]);
}

function testCoercibleToNumberZero(test) {
  function testPrimitiveValue(value) {
    test(value);
    // ToPrimitive
    testPrimitiveWrappers(value, "number", test);
  }

  testPrimitiveValue(null);
  testPrimitiveValue(false);
  testPrimitiveValue(0);
  testPrimitiveValue("0");
}

function testCoercibleToNumberNan(test) {
  function testPrimitiveValue(value) {
    test(value);
    // ToPrimitive
    testPrimitiveWrappers(value, "number", test);
  }

  testPrimitiveValue(undefined);
  testPrimitiveValue(NaN);
  testPrimitiveValue("");
  testPrimitiveValue("foo");
  testPrimitiveValue("true");
}

function testCoercibleToNumberOne(test) {
  function testPrimitiveValue(value) {
    test(value);
    // ToPrimitive
    testPrimitiveWrappers(value, "number", test);
  }

  testPrimitiveValue(true);
  testPrimitiveValue(1);
  testPrimitiveValue("1");
}

function testCoercibleToIntegerFromInteger(nominalInteger, test) {
  assert(Number.isInteger(nominalInteger));

  function testPrimitiveValue(value) {
    test(value);
    // ToPrimitive
    testPrimitiveWrappers(value, "number", test);

    // Non-primitive values that coerce to the nominal integer:
    // toString() returns a string that parsers to a primitive value.
    test([value]);
  }

  function testPrimitiveNumber(number) {
    testPrimitiveValue(number);
    // ToNumber: String -> Number
    testPrimitiveValue(number.toString());
  }

  testPrimitiveNumber(nominalInteger);

  // ToInteger: floor(abs(number))
  if (nominalInteger >= 0) {
    testPrimitiveNumber(nominalInteger + 0.9);
  }
  if (nominalInteger <= 0) {
    testPrimitiveNumber(nominalInteger - 0.9);
  }
}

function testPrimitiveWrappers(primitiveValue, hint, test) {
  if (primitiveValue != null) {
    // null and undefined result in {} rather than a proper wrapper,
    // so skip this case for those values.
    test(Object(primitiveValue));
  }

  testCoercibleToPrimitiveWithMethod(hint, function() {
    return primitiveValue;
  }, test);
}

function testCoercibleToPrimitiveWithMethod(hint, method, test) {
  var methodNames;
  if (hint === "number") {
    methodNames = ["valueOf", "toString"];
  } else if (hint === "string") {
    methodNames = ["toString", "valueOf"];
  } else {
    throw new Test262Error();
  }
  // precedence order
  test({
    [Symbol.toPrimitive]: method,
    [methodNames[0]]: function() { throw new Test262Error(); },
    [methodNames[1]]: function() { throw new Test262Error(); },
  });
  test({
    [methodNames[0]]: method,
    [methodNames[1]]: function() { throw new Test262Error(); },
  });
  if (hint === "number") {
    // The default valueOf returns an object, which is unsuitable.
    // The default toString returns a String, which is suitable.
    // Therefore this test only works for valueOf falling back to toString.
    test({
      // this is toString:
      [methodNames[1]]: method,
    });
  }

  // GetMethod: if func is undefined or null, return undefined.
  test({
    [Symbol.toPrimitive]: undefined,
    [methodNames[0]]: method,
    [methodNames[1]]: method,
  });
  test({
    [Symbol.toPrimitive]: null,
    [methodNames[0]]: method,
    [methodNames[1]]: method,
  });

  // if methodNames[0] is not callable, fallback to methodNames[1]
  test({
    [methodNames[0]]: null,
    [methodNames[1]]: method,
  });
  test({
    [methodNames[0]]: 1,
    [methodNames[1]]: method,
  });
  test({
    [methodNames[0]]: {},
    [methodNames[1]]: method,
  });

  // if methodNames[0] returns an object, fallback to methodNames[1]
  test({
    [methodNames[0]]: function() { return {}; },
    [methodNames[1]]: method,
  });
  test({
    [methodNames[0]]: function() { return Object(1); },
    [methodNames[1]]: method,
  });
}

function testNotCoercibleToIndex(test) {
  function testPrimitiveValue(value) {
    test(RangeError, value);
    // ToPrimitive
    testPrimitiveWrappers(value, "number", function(value) {
      test(RangeError, value);
    });
  }

  // Let integerIndex be ? ToInteger(value).
  testNotCoercibleToInteger(test);

  // If integerIndex < 0, throw a RangeError exception.
  testPrimitiveValue(-1);
  testPrimitiveValue(-2.5);
  testPrimitiveValue("-2.5");
  testPrimitiveValue(-Infinity);

  // Let index be ! ToLength(integerIndex).
  // If SameValueZero(integerIndex, index) is false, throw a RangeError exception.
  testPrimitiveValue(2 ** 53);
  testPrimitiveValue(Infinity);
}

function testNotCoercibleToInteger(test) {
  // ToInteger only throws from ToNumber.
  testNotCoercibleToNumber(test);
}

function testNotCoercibleToNumber(test) {
  function testPrimitiveValue(value) {
    test(TypeError, value);
    // ToPrimitive
    testPrimitiveWrappers(value, "number", function(value) {
      test(TypeError, value);
    });
  }

  // ToNumber: Symbol -> TypeError
  testPrimitiveValue(Symbol("1"));

  if (typeof BigInt !== "undefined") {
    // ToNumber: BigInt -> TypeError
    testPrimitiveValue(BigInt(0));
  }

  // ToPrimitive
  testNotCoercibleToPrimitive("number", test);
}

function testNotCoercibleToPrimitive(hint, test) {
  function MyError() {}

  // ToPrimitive: input[@@toPrimitive] is not callable (and non-null)
  test(TypeError, {[Symbol.toPrimitive]: 1});
  test(TypeError, {[Symbol.toPrimitive]: {}});

  // ToPrimitive: input[@@toPrimitive] returns object
  test(TypeError, {[Symbol.toPrimitive]: function() { return Object(1); }});
  test(TypeError, {[Symbol.toPrimitive]: function() { return {}; }});

  // ToPrimitive: input[@@toPrimitive] throws
  test(MyError, {[Symbol.toPrimitive]: function() { throw new MyError(); }});

  // OrdinaryToPrimitive: method throws
  testCoercibleToPrimitiveWithMethod(hint, function() {
    throw new MyError();
  }, function(value) {
    test(MyError, value);
  });

  // OrdinaryToPrimitive: both methods are unsuitable
  function testUnsuitableMethod(method) {
    test(TypeError, {valueOf:method, toString:method});
  }
  // not callable:
  testUnsuitableMethod(null);
  testUnsuitableMethod(1);
  testUnsuitableMethod({});
  // returns object:
  testUnsuitableMethod(function() { return Object(1); });
  testUnsuitableMethod(function() { return {}; });
}

function testCoercibleToString(test) {
  function testPrimitiveValue(value, expectedString) {
    test(value, expectedString);
    // ToPrimitive
    testPrimitiveWrappers(value, "string", function(value) {
      test(value, expectedString);
    });
  }

  testPrimitiveValue(undefined, "undefined");
  testPrimitiveValue(null, "null");
  testPrimitiveValue(true, "true");
  testPrimitiveValue(false, "false");
  testPrimitiveValue(0, "0");
  testPrimitiveValue(-0, "0");
  testPrimitiveValue(Infinity, "Infinity");
  testPrimitiveValue(-Infinity, "-Infinity");
  testPrimitiveValue(123.456, "123.456");
  testPrimitiveValue(-123.456, "-123.456");
  testPrimitiveValue("", "");
  testPrimitiveValue("foo", "foo");

  if (typeof BigInt !== "undefined") {
    // BigInt -> TypeError
    testPrimitiveValue(BigInt(0), "0");
  }

  // toString of a few objects
  test([], "");
  test(["foo", "bar"], "foo,bar");
  test({}, "[object Object]");
}

function testNotCoercibleToString(test) {
  function testPrimitiveValue(value) {
    test(TypeError, value);
    // ToPrimitive
    testPrimitiveWrappers(value, "string", function(value) {
      test(TypeError, value);
    });
  }

  // Symbol -> TypeError
  testPrimitiveValue(Symbol("1"));

  // ToPrimitive
  testNotCoercibleToPrimitive("string", test);
}

function testCoercibleToBooleanTrue(test) {
  test(true);
  test(1);
  test("string");
  test(Symbol("1"));
  test({});
}

function testCoercibleToBooleanFalse(test) {
  test(undefined);
  test(null);
  test(false);
  test(0);
  test(-0);
  test(NaN);
  test("");
}

function testCoercibleToBigIntZero(test) {
  function testPrimitiveValue(value) {
    test(value);
    // ToPrimitive
    testPrimitiveWrappers(value, "number", test);
  }

  testCoercibleToBigIntFromBigInt(BigInt(0), test);
  testPrimitiveValue(-BigInt(0));
  testPrimitiveValue("-0");
  testPrimitiveValue(false);
  testPrimitiveValue("");
  testPrimitiveValue("   ");

  // toString() returns ""
  test([]);

  // toString() returns "0"
  test([0]);
}

function testCoercibleToBigIntOne(test) {
  function testPrimitiveValue(value) {
    test(value);
    // ToPrimitive
    testPrimitiveWrappers(value, "number", test);
  }

  testCoercibleToBigIntFromBigInt(BigInt(1), test);
  testPrimitiveValue(true);

  // toString() returns "1"
  test([1]);
}

function testCoercibleToBigIntFromBigInt(nominalBigInt, test) {
  function testPrimitiveValue(value) {
    test(value);
    // ToPrimitive
    testPrimitiveWrappers(value, "number", test);
  }

  testPrimitiveValue(nominalBigInt);
  testPrimitiveValue(nominalBigInt.toString());
  testPrimitiveValue("0b" + nominalBigInt.toString(2));
  testPrimitiveValue("0o" + nominalBigInt.toString(8));
  testPrimitiveValue("0x" + nominalBigInt.toString(16));
  testPrimitiveValue("   " + nominalBigInt.toString() + "   ");

  // toString() returns the decimal string representation
  test([nominalBigInt]);
  test([nominalBigInt.toString()]);
}

function testNotCoercibleToBigInt(test) {
  function testPrimitiveValue(error, value) {
    test(error, value);
    // ToPrimitive
    testPrimitiveWrappers(value, "number", function(value) {
      test(error, value);
    });
  }

  // Undefined, Null, Number, Symbol -> TypeError
  testPrimitiveValue(TypeError, undefined);
  testPrimitiveValue(TypeError, null);
  testPrimitiveValue(TypeError, 0);
  testPrimitiveValue(TypeError, NaN);
  testPrimitiveValue(TypeError, Infinity);
  testPrimitiveValue(TypeError, Symbol("1"));

  // when a String parses to NaN -> SyntaxError
  function testStringValue(string) {
    testPrimitiveValue(SyntaxError, string);
    testPrimitiveValue(SyntaxError, "   " + string);
    testPrimitiveValue(SyntaxError, string + "   ");
    testPrimitiveValue(SyntaxError, "   " + string + "   ");
  }
  testStringValue("a");
  testStringValue("0b2");
  testStringValue("0o8");
  testStringValue("0xg");
  testStringValue("1n");
}
// Copyright (C) 2018 the V8 project authors. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
description: |
    An Array of all representable Well-Known Intrinsic Objects
---*/

const WellKnownIntrinsicObjects = [
  {
    intrinsicName: "%Array%",
    globalNameOrSource: "Array"
  },
  {
    intrinsicName: "%ArrayBuffer%",
    globalNameOrSource: "ArrayBuffer"
  },
  {
    intrinsicName: "%ArrayBufferPrototype%",
    globalNameOrSource: "ArrayBuffer.prototype"
  },
  {
    intrinsicName: "%ArrayIteratorPrototype%",
    globalNameOrSource: "Object.getPrototypeOf([][Symbol.iterator]())"
  },
  {
    intrinsicName: "%ArrayPrototype%",
    globalNameOrSource: "Array.prototype"
  },
  {
    intrinsicName: "%ArrayProto_entries%",
    globalNameOrSource: "Array.prototype.entries"
  },
  {
    intrinsicName: "%ArrayProto_forEach%",
    globalNameOrSource: "Array.prototype.forEach"
  },
  {
    intrinsicName: "%ArrayProto_keys%",
    globalNameOrSource: "Array.prototype.keys"
  },
  {
    intrinsicName: "%ArrayProto_values%",
    globalNameOrSource: "Array.prototype.values"
  },
  {
    intrinsicName: "%AsyncFromSyncIteratorPrototype%",
    globalNameOrSource: "undefined"
  },
  {
    intrinsicName: "%AsyncFunction%",
    globalNameOrSource: "(async function() {}).constructor"
  },
  {
    intrinsicName: "%AsyncFunctionPrototype%",
    globalNameOrSource: "(async function() {}).constructor.prototype"
  },
  {
    intrinsicName: "%AsyncGenerator%",
    globalNameOrSource: "Object.getPrototypeOf((async function * () {})())"
  },
  {
    intrinsicName: "%AsyncGeneratorFunction%",
    globalNameOrSource: "Object.getPrototypeOf(async function * () {})"
  },
  {
    intrinsicName: "%AsyncGeneratorPrototype%",
    globalNameOrSource: "Object.getPrototypeOf(async function * () {}).prototype"
  },
  {
    intrinsicName: "%AsyncIteratorPrototype%",
    globalNameOrSource: "((async function * () {})())[Symbol.asyncIterator]()"
  },
  {
    intrinsicName: "%Atomics%",
    globalNameOrSource: "Atomics"
  },
  {
    intrinsicName: "%Boolean%",
    globalNameOrSource: "Boolean"
  },
  {
    intrinsicName: "%BooleanPrototype%",
    globalNameOrSource: "Boolean.prototype"
  },
  {
    intrinsicName: "%DataView%",
    globalNameOrSource: "DataView"
  },
  {
    intrinsicName: "%DataViewPrototype%",
    globalNameOrSource: "DataView.prototype"
  },
  {
    intrinsicName: "%Date%",
    globalNameOrSource: "Date"
  },
  {
    intrinsicName: "%DatePrototype%",
    globalNameOrSource: "Date.prototype"
  },
  {
    intrinsicName: "%decodeURI%",
    globalNameOrSource: "decodeURI"
  },
  {
    intrinsicName: "%decodeURIComponent%",
    globalNameOrSource: "decodeURIComponent"
  },
  {
    intrinsicName: "%encodeURI%",
    globalNameOrSource: "encodeURI"
  },
  {
    intrinsicName: "%encodeURIComponent%",
    globalNameOrSource: "encodeURIComponent"
  },
  {
    intrinsicName: "%Error%",
    globalNameOrSource: "Error"
  },
  {
    intrinsicName: "%ErrorPrototype%",
    globalNameOrSource: "Error.prototype"
  },
  {
    intrinsicName: "%eval%",
    globalNameOrSource: "eval"
  },
  {
    intrinsicName: "%EvalError%",
    globalNameOrSource: "EvalError"
  },
  {
    intrinsicName: "%EvalErrorPrototype%",
    globalNameOrSource: "EvalError.prototype"
  },
  {
    intrinsicName: "%Float32Array%",
    globalNameOrSource: "Float32Array"
  },
  {
    intrinsicName: "%Float32ArrayPrototype%",
    globalNameOrSource: "Float32Array.prototype"
  },
  {
    intrinsicName: "%Float64Array%",
    globalNameOrSource: "Float64Array"
  },
  {
    intrinsicName: "%Float64ArrayPrototype%",
    globalNameOrSource: "Float64Array.prototype"
  },
  {
    intrinsicName: "%Function%",
    globalNameOrSource: "Function"
  },
  {
    intrinsicName: "%FunctionPrototype%",
    globalNameOrSource: "Function.prototype"
  },
  {
    intrinsicName: "%Generator%",
    globalNameOrSource: "Object.getPrototypeOf((function * () {})())"
  },
  {
    intrinsicName: "%GeneratorFunction%",
    globalNameOrSource: "Object.getPrototypeOf(function * () {})"
  },
  {
    intrinsicName: "%GeneratorPrototype%",
    globalNameOrSource: "Object.getPrototypeOf(function * () {}).prototype"
  },
  {
    intrinsicName: "%Int8Array%",
    globalNameOrSource: "Int8Array"
  },
  {
    intrinsicName: "%Int8ArrayPrototype%",
    globalNameOrSource: "Int8Array.prototype"
  },
  {
    intrinsicName: "%Int16Array%",
    globalNameOrSource: "Int16Array"
  },
  {
    intrinsicName: "%Int16ArrayPrototype%",
    globalNameOrSource: "Int16Array.prototype"
  },
  {
    intrinsicName: "%Int32Array%",
    globalNameOrSource: "Int32Array"
  },
  {
    intrinsicName: "%Int32ArrayPrototype%",
    globalNameOrSource: "Int32Array.prototype"
  },
  {
    intrinsicName: "%isFinite%",
    globalNameOrSource: "isFinite"
  },
  {
    intrinsicName: "%isNaN%",
    globalNameOrSource: "isNaN"
  },
  {
    intrinsicName: "%IteratorPrototype%",
    globalNameOrSource: "Object.getPrototypeOf(Object.getPrototypeOf([][Symbol.iterator]()))"
  },
  {
    intrinsicName: "%JSON%",
    globalNameOrSource: "JSON"
  },
  {
    intrinsicName: "%JSONParse%",
    globalNameOrSource: "JSON.parse"
  },
  {
    intrinsicName: "%Map%",
    globalNameOrSource: "Map"
  },
  {
    intrinsicName: "%MapIteratorPrototype%",
    globalNameOrSource: "Object.getPrototypeOf(new Map()[Symbol.iterator]())"
  },
  {
    intrinsicName: "%MapPrototype%",
    globalNameOrSource: "Map.prototype"
  },
  {
    intrinsicName: "%Math%",
    globalNameOrSource: "Math"
  },
  {
    intrinsicName: "%Number%",
    globalNameOrSource: "Number"
  },
  {
    intrinsicName: "%NumberPrototype%",
    globalNameOrSource: "Number.prototype"
  },
  {
    intrinsicName: "%Object%",
    globalNameOrSource: "Object"
  },
  {
    intrinsicName: "%ObjectPrototype%",
    globalNameOrSource: "Object.prototype"
  },
  {
    intrinsicName: "%ObjProto_toString%",
    globalNameOrSource: "Object.prototype.toString"
  },
  {
    intrinsicName: "%ObjProto_valueOf%",
    globalNameOrSource: "Object.prototype.valueOf"
  },
  {
    intrinsicName: "%parseFloat%",
    globalNameOrSource: "parseFloat"
  },
  {
    intrinsicName: "%parseInt%",
    globalNameOrSource: "parseInt"
  },
  {
    intrinsicName: "%Promise%",
    globalNameOrSource: "Promise"
  },
  {
    intrinsicName: "%PromisePrototype%",
    globalNameOrSource: "Promise.prototype"
  },
  {
    intrinsicName: "%PromiseProto_then%",
    globalNameOrSource: "Promise.prototype.then"
  },
  {
    intrinsicName: "%Promise_all%",
    globalNameOrSource: "Promise.all"
  },
  {
    intrinsicName: "%Promise_reject%",
    globalNameOrSource: "Promise.reject"
  },
  {
    intrinsicName: "%Promise_resolve%",
    globalNameOrSource: "Promise.resolve"
  },
  {
    intrinsicName: "%Proxy%",
    globalNameOrSource: "Proxy"
  },
  {
    intrinsicName: "%RangeError%",
    globalNameOrSource: "RangeError"
  },
  {
    intrinsicName: "%RangeErrorPrototype%",
    globalNameOrSource: "RangeError.prototype"
  },
  {
    intrinsicName: "%ReferenceError%",
    globalNameOrSource: "ReferenceError"
  },
  {
    intrinsicName: "%ReferenceErrorPrototype%",
    globalNameOrSource: "ReferenceError.prototype"
  },
  {
    intrinsicName: "%Reflect%",
    globalNameOrSource: "Reflect"
  },
  {
    intrinsicName: "%RegExp%",
    globalNameOrSource: "RegExp"
  },
  {
    intrinsicName: "%RegExpPrototype%",
    globalNameOrSource: "RegExp.prototype"
  },
  {
    intrinsicName: "%Set%",
    globalNameOrSource: "Set"
  },
  {
    intrinsicName: "%SetIteratorPrototype%",
    globalNameOrSource: "Object.getPrototypeOf(new Set()[Symbol.iterator]())"
  },
  {
    intrinsicName: "%SetPrototype%",
    globalNameOrSource: "Set.prototype"
  },
  {
    intrinsicName: "%SharedArrayBuffer%",
    globalNameOrSource: "SharedArrayBuffer"
  },
  {
    intrinsicName: "%SharedArrayBufferPrototype%",
    globalNameOrSource: "SharedArrayBuffer.prototype"
  },
  {
    intrinsicName: "%String%",
    globalNameOrSource: "String"
  },
  {
    intrinsicName: "%StringIteratorPrototype%",
    globalNameOrSource: "Object.getPrototypeOf(new String()[Symbol.iterator]())"
  },
  {
    intrinsicName: "%StringPrototype%",
    globalNameOrSource: "String.prototype"
  },
  {
    intrinsicName: "%Symbol%",
    globalNameOrSource: "Symbol"
  },
  {
    intrinsicName: "%SymbolPrototype%",
    globalNameOrSource: "Symbol.prototype"
  },
  {
    intrinsicName: "%SyntaxError%",
    globalNameOrSource: "SyntaxError"
  },
  {
    intrinsicName: "%SyntaxErrorPrototype%",
    globalNameOrSource: "SyntaxError.prototype"
  },
  {
    intrinsicName: "%ThrowTypeError%",
    globalNameOrSource: "(function() { 'use strict'; return Object.getOwnPropertyDescriptor(arguments, 'callee').get })()"
  },
  {
    intrinsicName: "%TypedArray%",
    globalNameOrSource: "Object.getPrototypeOf(Uint8Array)"
  },
  {
    intrinsicName: "%TypedArrayPrototype%",
    globalNameOrSource: "Object.getPrototypeOf(Uint8Array).prototype"
  },
  {
    intrinsicName: "%TypeError%",
    globalNameOrSource: "TypeError"
  },
  {
    intrinsicName: "%TypeErrorPrototype%",
    globalNameOrSource: "TypeError.prototype"
  },
  {
    intrinsicName: "%Uint8Array%",
    globalNameOrSource: "Uint8Array"
  },
  {
    intrinsicName: "%Uint8ArrayPrototype%",
    globalNameOrSource: "Uint8Array.prototype"
  },
  {
    intrinsicName: "%Uint8ClampedArray%",
    globalNameOrSource: "Uint8ClampedArray"
  },
  {
    intrinsicName: "%Uint8ClampedArrayPrototype%",
    globalNameOrSource: "Uint8ClampedArray.prototype"
  },
  {
    intrinsicName: "%Uint16Array%",
    globalNameOrSource: "Uint16Array"
  },
  {
    intrinsicName: "%Uint16ArrayPrototype%",
    globalNameOrSource: "Uint16Array.prototype"
  },
  {
    intrinsicName: "%Uint32Array%",
    globalNameOrSource: "Uint32Array"
  },
  {
    intrinsicName: "%Uint32ArrayPrototype%",
    globalNameOrSource: "Uint32Array.prototype"
  },
  {
    intrinsicName: "%URIError%",
    globalNameOrSource: "URIError"
  },
  {
    intrinsicName: "%URIErrorPrototype%",
    globalNameOrSource: "URIError.prototype"
  },
  {
    intrinsicName: "%WeakMap%",
    globalNameOrSource: "WeakMap"
  },
  {
    intrinsicName: "%WeakMapPrototype%",
    globalNameOrSource: "WeakMap.prototype"
  },
  {
    intrinsicName: "%WeakSet%",
    globalNameOrSource: "WeakSet"
  },
  {
    intrinsicName: "%WeakSetPrototype%",
    globalNameOrSource: "WeakSet.prototype"
  }
];


WellKnownIntrinsicObjects.forEach(wkio => {
  var actual;

  try {
    actual = new Function("return " + wkio.globalNameOrSource)();
  } catch (exception) {
    // Nothing to do here.
  }

  wkio.reference = actual;
});
