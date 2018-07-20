/* -*- indent-tabs-mode: nil; js-indent-level: 2 -*-
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

// NOTE: If you're adding new test harness functionality -- first, should you
//       at all?  Most stuff is better in specific tests, or in nested shell.js
//       or browser.js.  Second, supposing you should, please add it to this
//       IIFE for better modularity/resilience against tests that must do
//       particularly bizarre things that might break the harness.

(function(global) {
  "use strict";

  /**********************************************************************
   * CACHED PRIMORDIAL FUNCTIONALITY (before a test might overwrite it) *
   **********************************************************************/

  var undefined; // sigh

  var Error = global.Error;
  var Function = global.Function;
  var Number = global.Number;
  var RegExp = global.RegExp;
  var String = global.String;
  var Symbol = global.Symbol;
  var TypeError = global.TypeError;

  var ArrayIsArray = global.Array.isArray;
  var MathAbs = global.Math.abs;
  var ObjectCreate = global.Object.create;
  var ObjectDefineProperty = global.Object.defineProperty;
  var ReflectApply = global.Reflect.apply;
  var RegExpPrototypeExec = global.RegExp.prototype.exec;
  var StringPrototypeCharCodeAt = global.String.prototype.charCodeAt;
  var StringPrototypeIndexOf = global.String.prototype.indexOf;
  var StringPrototypeSubstring = global.String.prototype.substring;

  var runningInBrowser = typeof global.window !== "undefined";
  if (runningInBrowser) {
    // Certain cached functionality only exists (and is only needed) when
    // running in the browser.  Segregate that caching here.

    var SpecialPowersSetGCZeal =
      global.SpecialPowers ? global.SpecialPowers.setGCZeal : undefined;
  }

  var evaluate = global.evaluate;
  var options = global.options;

  /****************************
   * GENERAL HELPER FUNCTIONS *
   ****************************/

  // We *cannot* use Array.prototype.push for this, because that function sets
  // the new trailing element, which could invoke a setter (left by a test) on
  // Array.prototype or Object.prototype.
  function ArrayPush(arr, val) {
    assertEq(ArrayIsArray(arr), true,
             "ArrayPush must only be used on actual arrays");

    var desc = ObjectCreate(null);
    desc.value = val;
    desc.enumerable = true;
    desc.configurable = true;
    desc.writable = true;
    ObjectDefineProperty(arr, arr.length, desc);
  }

  function StringCharCodeAt(str, index) {
    return ReflectApply(StringPrototypeCharCodeAt, str, [index]);
  }

  function StringSplit(str, delimiter) {
    assertEq(typeof str === "string" && typeof delimiter === "string", true,
             "StringSplit must be called with two string arguments");
    assertEq(delimiter.length > 0, true,
             "StringSplit doesn't support an empty delimiter string");

    var parts = [];
    var last = 0;
    while (true) {
      var i = ReflectApply(StringPrototypeIndexOf, str, [delimiter, last]);
      if (i < 0) {
        if (last < str.length)
          ArrayPush(parts, ReflectApply(StringPrototypeSubstring, str, [last]));
        return parts;
      }

      ArrayPush(parts, ReflectApply(StringPrototypeSubstring, str, [last, i]));
      last = i + delimiter.length;
    }
  }

  function shellOptionsClear() {
    assertEq(runningInBrowser, false, "Only called when running in the shell.");

    // Return early if no options are set.
    var currentOptions = options ? options() : "";
    if (currentOptions === "")
      return;

    // Turn off current settings.
    var optionNames = StringSplit(currentOptions, ",");
    for (var i = 0; i < optionNames.length; i++) {
      options(optionNames[i]);
    }
  }

  /****************************
   * TESTING FUNCTION EXPORTS *
   ****************************/

  function SameValue(v1, v2) {
    // We could |return Object.is(v1, v2);|, but that's less portable.
    if (v1 === 0 && v2 === 0)
      return 1 / v1 === 1 / v2;
    if (v1 !== v1 && v2 !== v2)
      return true;
    return v1 === v2;
  }

  var assertEq = global.assertEq;
  if (typeof assertEq !== "function") {
    assertEq = function assertEq(actual, expected, message) {
      if (!SameValue(actual, expected)) {
        throw new TypeError(`Assertion failed: got "${actual}", expected "${expected}"` +
                            (message ? ": " + message : ""));
      }
    };
    global.assertEq = assertEq;
  }

  // jsfuzz fix: add assertion function
  var assert = global.assert;
  if (typeof assert !== "function") {
    assert = function assert(condition) {
      if (!(condition)) {
        throw new Error("Test failed");
      }
    };
    global.assert = assert;
  }
  // end jsfuzz fix

  function assertEqArray(actual, expected) {
    var len = actual.length;
    assertEq(len, expected.length, "mismatching array lengths");

    var i = 0;
    try {
      for (; i < len; i++)
        assertEq(actual[i], expected[i], "mismatch at element " + i);
    } catch (e) {
      throw new Error(`Exception thrown at index ${i}: ${e}`);
    }
  }
  global.assertEqArray = assertEqArray;

  function assertThrows(f) {
    var ok = false;
    try {
      f();
    } catch (exc) {
      ok = true;
    }
    if (!ok)
      throw new Error(`Assertion failed: ${f} did not throw as expected`);
  }
  global.assertThrows = assertThrows;

  function assertThrowsInstanceOf(f, ctor, msg) {
    var fullmsg;
    try {
      f();
    } catch (exc) {
      if (exc instanceof ctor)
        return;
      fullmsg = `Assertion failed: expected exception ${ctor.name}, got ${exc}`;
    }

    if (fullmsg === undefined)
      fullmsg = `Assertion failed: expected exception ${ctor.name}, no exception thrown`;
    if (msg !== undefined)
      fullmsg += " - " + msg;

    throw new Error(fullmsg);
  }
  global.assertThrowsInstanceOf = assertThrowsInstanceOf;

  /****************************
   * UTILITY FUNCTION EXPORTS *
   ****************************/

  var dump = global.dump;
  if (typeof global.dump === "function") {
    // A presumptively-functional |dump| exists, so no need to do anything.
  } else {
    // We don't have |dump|.  Try to simulate the desired effect another way.
    if (runningInBrowser) {
      // We can't actually print to the console: |global.print| invokes browser
      // printing functionality here (it's overwritten just below), and
      // |global.dump| isn't a function that'll dump to the console (presumably
      // because the preference to enable |dump| wasn't set).  Just make it a
      // no-op.
      dump = function() {};
    } else {
      // |print| prints to stdout: make |dump| do likewise.
      dump = global.print;
    }
    global.dump = dump;
  }

  var print;
  if (runningInBrowser) {
    // We're executing in a browser.  Using |global.print| would invoke browser
    // printing functionality: not what tests want!  Instead, use a print
    // function that syncs up with the test harness and console.
    print = function print() {
      var s = "TEST-INFO | ";
      for (var i = 0; i < arguments.length; i++)
        s += String(arguments[i]) + " ";

      // Dump the string to the console for developers and the harness.
      dump(s + "\n");

      // AddPrintOutput doesn't require HTML special characters be escaped.
      global.AddPrintOutput(s);
    };

    global.print = print;
  } else {
    // We're executing in a shell, and |global.print| is the desired function.
    print = global.print;
  }

  var gczeal = global.gczeal;
  if (typeof gczeal !== "function") {
    if (typeof SpecialPowersSetGCZeal === "function") {
      gczeal = function gczeal(z) {
        SpecialPowersSetGCZeal(z);
      };
    } else {
      gczeal = function() {}; // no-op if not available
    }

    global.gczeal = gczeal;
  }

  // Evaluates the given source code as global script code. browser.js provides
  // a different implementation for this function.
  var evaluateScript = global.evaluateScript;
  if (typeof evaluate === "function" && typeof evaluateScript !== "function") {
    evaluateScript = function evaluateScript(code) {
      evaluate(String(code));
    };

    global.evaluateScript = evaluateScript;
  }

  function toPrinted(value) {
    value = String(value);

    var digits = "0123456789ABCDEF";
    var result = "";
    for (var i = 0; i < value.length; i++) {
      var ch = StringCharCodeAt(value, i);
      if (ch === 0x5C && i + 1 < value.length) {
        var d = value[i + 1];
        if (d === "n") {
          result += "NL";
          i++;
        } else if (d === "r") {
          result += "CR";
          i++;
        } else {
          result += "\\";
        }
      } else if (ch === 0x0A) {
        result += "NL";
      } else if (ch < 0x20 || ch > 0x7E) {
        var a = digits[ch & 0xf];
        ch >>= 4;
        var b = digits[ch & 0xf];
        ch >>= 4;

        if (ch) {
          var c = digits[ch & 0xf];
          ch >>= 4;
          var d = digits[ch & 0xf];

          result += "\\u" + d + c + b + a;
        } else {
          result += "\\x" + b + a;
        }
      } else {
        result += value[i];
      }
    }

    return result;
  }

  /*
   * An xorshift pseudo-random number generator see:
   * https://en.wikipedia.org/wiki/Xorshift#xorshift.2A
   * This generator will always produce a value, n, where
   * 0 <= n <= 255
   */
  function *XorShiftGenerator(seed, size) {
      let x = seed;
      for (let i = 0; i < size; i++) {
          x ^= x >> 12;
          x ^= x << 25;
          x ^= x >> 27;
          yield x % 256;
      }
  }
  global.XorShiftGenerator = XorShiftGenerator;

  /*************************************************************************
   * HARNESS-CENTRIC EXPORTS (we should generally work to eliminate these) *
   *************************************************************************/

  var PASSED = " PASSED! ";
  var FAILED = " FAILED! ";

  /*
   * Same as `new TestCase(description, expect, actual)`, except it doesn't
   * return the newly created test case object.
   */
  function AddTestCase(description, expect, actual) {
    new TestCase(description, expect, actual);
  }
  global.AddTestCase = AddTestCase;

  var testCasesArray = [];

  function TestCase(d, e, a, r) {
    this.description = d;
    this.expect = e;
    this.actual = a;
    this.passed = getTestCaseResult(e, a);
    this.reason = typeof r !== 'undefined' ? String(r) : '';

    ArrayPush(testCasesArray, this);
  }
  global.TestCase = TestCase;

  TestCase.prototype = ObjectCreate(null);
  TestCase.prototype.testPassed = (function TestCase_testPassed() { return this.passed; });
  TestCase.prototype.testFailed = (function TestCase_testFailed() { return !this.passed; });
  TestCase.prototype.testDescription = (function TestCase_testDescription() { return this.description + ' ' + this.reason; });

  function getTestCaseResult(expected, actual) {
    if (typeof expected !== typeof actual)
      return false;
    if (typeof expected !== 'number')
      // Note that many tests depend on the use of '==' here, not '==='.
      return actual == expected;

    // Distinguish NaN from other values.  Using x !== x comparisons here
    // works even if tests redefine isNaN.
    if (actual !== actual)
      return expected !== expected;
    if (expected !== expected)
      return false;

    // Tolerate a certain degree of error.
    if (actual !== expected)
      return MathAbs(actual - expected) <= 1E-10;

    // Here would be a good place to distinguish 0 and -0, if we wanted
    // to.  However, doing so would introduce a number of failures in
    // areas where they don't seem important.  For example, the WeekDay
    // function in ECMA-262 returns -0 for Sundays before the epoch, but
    // the Date functions in SpiderMonkey specified in terms of WeekDay
    // often don't.  This seems unimportant.
    return true;
  }

  function reportTestCaseResult(description, expected, actual, output) {
    var testcase = new TestCase(description, expected, actual, output);

    // if running under reftest, let it handle result reporting.
    if (!runningInBrowser) {
      if (testcase.passed) {
        // print(PASSED + description);
      } else {
        reportFailure(description + " : " + output);
      }
    }
  }

  function getTestCases() {
    return testCasesArray;
  }
  global.getTestCases = getTestCases;

  /*
   * The test driver searches for such a phrase in the test output.
   * If such phrase exists, it will set n as the expected exit code.
   */
  function expectExitCode(n) {
    print('--- NOTE: IN THIS TESTCASE, WE EXPECT EXIT CODE ' + n + ' ---');
  }
  global.expectExitCode = expectExitCode;

  /*
   * Statuses current section of a test
   */
  function inSection(x) {
    return "Section " + x + " of test - ";
  }
  global.inSection = inSection;

  /*
   * Report a failure in the 'accepted' manner
   */
  function reportFailure(msg) {
    msg = String(msg);
    var lines = StringSplit(msg, "\n");

    for (var i = 0; i < lines.length; i++)
      print(FAILED + " " + lines[i]);
  }
  global.reportFailure = reportFailure;

  /*
   * Print a non-failure message.
   */
  function printStatus(msg) {
    // *** AVOID UNNECESSARY PRINTS ***
    // msg = String(msg);
    // var lines = StringSplit(msg, "\n");
    // for (var i = 0; i < lines.length; i++)
    //   print("STATUS: " + lines[i]);
  }
  global.printStatus = printStatus;

  /*
  * Print a bugnumber message.
  */
  function printBugNumber(num) {
    // print('BUGNUMBER: ' + num); *** AVOID UNNECESSARY PRINTS ***
  }
  global.printBugNumber = printBugNumber;

  /*
   * Compare expected result to actual result, if they differ (in value and/or
   * type) report a failure.  If description is provided, include it in the
   * failure report.
   */
  function reportCompare(expected, actual, description) {
    var expected_t = typeof expected;
    var actual_t = typeof actual;
    var output = "";

    if (typeof description === "undefined")
      description = "";

    if (expected_t !== actual_t)
      output += `Type mismatch, expected type ${expected_t}, actual type ${actual_t} `;

    if (expected != actual)
      output += `Expected value '${toPrinted(expected)}', Actual value '${toPrinted(actual)}' `;

    reportTestCaseResult(description, expected, actual, output);
  }
  global.reportCompare = reportCompare;

  /*
   * Attempt to match a regular expression describing the result to
   * the actual result, if they differ (in value and/or
   * type) report a failure.  If description is provided, include it in the
   * failure report.
   */
  function reportMatch(expectedRegExp, actual, description) {
    var expected_t = "string";
    var actual_t = typeof actual;
    var output = "";

    if (typeof description === "undefined")
      description = "";

    if (expected_t !== actual_t)
      output += `Type mismatch, expected type ${expected_t}, actual type ${actual_t} `;

    var matches = ReflectApply(RegExpPrototypeExec, expectedRegExp, [actual]) !== null;
    if (!matches) {
      output +=
        `Expected match to '${toPrinted(expectedRegExp)}', Actual value '${toPrinted(actual)}' `;
    }

    reportTestCaseResult(description, true, matches, output);
  }
  global.reportMatch = reportMatch;

  function compareSource(expect, actual, summary) {
    // compare source
    var expectP = String(expect);
    var actualP = String(actual);

    print('expect:\n' + expectP);
    print('actual:\n' + actualP);

    reportCompare(expectP, actualP, summary);

    // actual must be compilable if expect is?
    try {
      var expectCompile = 'No Error';
      var actualCompile;

      Function(expect);
      try {
        Function(actual);
        actualCompile = 'No Error';
      } catch(ex1) {
        actualCompile = ex1 + '';
      }
      reportCompare(expectCompile, actualCompile,
                    summary + ': compile actual');
    } catch(ex) {
    }
  }
  global.compareSource = compareSource;

  // ***** NEED TO COMMENT THIS FUNCTION TO RUN CORRECTLY ON CHAKRA ENGINE *****
  // function test() {
  //   var testCases = getTestCases();
  //   for (var i = 0; i < testCases.length; i++) {
  //     var testCase = testCases[i];
  //     testCase.reason += testCase.passed ? "" : "wrong value ";

  //     // if running under reftest, let it handle result reporting.
  //     if (!runningInBrowser) {
  //       var message = `${testCase.description} = ${testCase.actual} expected: ${testCase.expect}`;
  //       print((testCase.passed ? PASSED : FAILED) + message);
  //     }
  //   }
  // }
  // global.test = test;

  // This function uses the shell's print function. When running tests in the
  // browser, browser.js overrides this function to write to the page.
  function writeHeaderToLog(string) {
    // print(string);
  }
  global.writeHeaderToLog = writeHeaderToLog;

  /************************************
   * PROMISE TESTING FUNCTION EXPORTS *
   ************************************/

  function getPromiseResult(promise) {
    var result, error, caught = false;
    promise.then(r => { result = r; },
                 e => { caught = true; error = e; });
    drainJobQueue();
    if (caught)
      throw error;
    return result;
  }
  global.getPromiseResult = getPromiseResult;

  function assertEventuallyEq(promise, expected) {
    assertEq(getPromiseResult(promise), expected);
  }
  global.assertEventuallyEq = assertEventuallyEq;

  function assertEventuallyThrows(promise, expectedErrorType) {
    assertThrowsInstanceOf(() => getPromiseResult(promise), expectedErrorType);
  };
  global.assertEventuallyThrows = assertEventuallyThrows;

  function assertEventuallyDeepEq(promise, expected) {
    assertDeepEq(getPromiseResult(promise), expected);
  };
  global.assertEventuallyDeepEq = assertEventuallyDeepEq;

  /*******************************************
   * RUN ONCE CODE TO SETUP ADDITIONAL STATE *
   *******************************************/

  // Clear all options before running any tests. browser.js performs this
  // set-up as part of its jsTestDriverBrowserInit function.
  if (!runningInBrowser)
    shellOptionsClear();
})(this);

var DESCRIPTION;
/* -*- indent-tabs-mode: nil; js-indent-level: 2 -*- */

/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function(global) {

  /*
   * completesNormally(CODE) returns true if evaluating CODE (as eval
   * code) completes normally (rather than throwing an exception).
   */
  global.completesNormally = function completesNormally(code) {
    try {
      eval(code);
      return true;
    } catch (exception) {
      return false;
    }
  }

  /*
   * raisesException(EXCEPTION)(CODE) returns true if evaluating CODE (as
   * eval code) throws an exception object that is an instance of EXCEPTION,
   * and returns false if it throws any other error or evaluates
   * successfully. For example: raises(TypeError)("0()") == true.
   */
  global.raisesException = function raisesException(exception) {
    return function (code) {
      try {
	eval(code);
	return false;
      } catch (actual) {
	return actual instanceof exception;
      }
    };
  };

  /*
   * Return true if A is equal to B, where equality on arrays and objects
   * means that they have the same set of enumerable properties, the values
   * of each property are deep_equal, and their 'length' properties are
   * equal. Equality on other types is ==.
   */
    global.deepEqual = function deepEqual(a, b) {
    if (typeof a != typeof b)
      return false;

    if (typeof a == 'object') {
      var props = {};
      // For every property of a, does b have that property with an equal value?
      for (var prop in a) {
        if (!deepEqual(a[prop], b[prop]))
          return false;
        props[prop] = true;
      }
      // Are all of b's properties present on a?
      for (var prop in b)
        if (!props[prop])
          return false;
      // length isn't enumerable, but we want to check it, too.
      return a.length == b.length;
    }

    if (a === b) {
      // Distinguish 0 from -0, even though they are ===.
      return a !== 0 || 1/a === 1/b;
    }

    // Treat NaNs as equal, even though NaN !== NaN.
    // NaNs are the only non-reflexive values, i.e., if a !== a, then a is a NaN.
    // isNaN is broken: it converts its argument to number, so isNaN("foo") => true
    return a !== a && b !== b;
  }

  /** Make an iterator with a return method. */
  global.makeIterator = function makeIterator(overrides) {
    var throwMethod;
    if (overrides && overrides.throw)
      throwMethod = overrides.throw;
    var iterator = {
      throw: throwMethod,
      next: function(x) {
        if (overrides && overrides.next)
          return overrides.next(x);
        return { done: false };
      },
      return: function(x) {
        if (overrides && overrides.ret)
          return overrides.ret(x);
        return { done: true };
      }
    };

    return function() { return iterator; };
  };

  /** Yield every permutation of the elements in some array. */
  global.Permutations = function* Permutations(items) {
    if (items.length == 0) {
      yield [];
    } else {
      items = items.slice(0);
      for (let i = 0; i < items.length; i++) {
        let swap = items[0];
        items[0] = items[i];
        items[i] = swap;
        for (let e of Permutations(items.slice(1, items.length)))
          yield [items[0]].concat(e);
      }
    }
  };

  global.assertThrowsValue = function assertThrowsValue(f, val, msg) {
    var fullmsg;
    try {
      f();
    } catch (exc) {
      if ((exc === val) === (val === val) && (val !== 0 || 1 / exc === 1 / val))
        return;
      fullmsg = "Assertion failed: expected exception " + val + ", got " + exc;
    }
    if (fullmsg === undefined)
      fullmsg = "Assertion failed: expected exception " + val + ", no exception thrown";
    if (msg !== undefined)
      fullmsg += " - " + msg;
    throw new Error(fullmsg);
  };

  global.assertThrowsInstanceOf = function assertThrowsInstanceOf(f, ctor, msg) {
    var fullmsg;
    try {
      f();
    } catch (exc) {
      if (exc instanceof ctor)
        return;
      fullmsg = `Assertion failed: expected exception ${ctor.name}, got ${exc}`;
    }

    if (fullmsg === undefined)
      fullmsg = `Assertion failed: expected exception ${ctor.name}, no exception thrown`;
    if (msg !== undefined)
      fullmsg += " - " + msg;

    throw new Error(fullmsg);
  };

  global.uneval = (function(){throw Error("JSFUZZ ERROR: Unsupported function (uneval)")}); 

  global.assertDeepEq = (function(){
    var call = Function.prototype.call,
      Array_isArray = Array.isArray,
      Map_ = Map,
      Error_ = Error,
      Symbol_ = Symbol,
      Map_has = call.bind(Map.prototype.has),
      Map_get = call.bind(Map.prototype.get),
      Map_set = call.bind(Map.prototype.set),
      Object_toString = call.bind(Object.prototype.toString),
      Function_toString = call.bind(Function.prototype.toString),
      Object_getPrototypeOf = Object.getPrototypeOf,
      Object_hasOwnProperty = call.bind(Object.prototype.hasOwnProperty),
      Object_getOwnPropertyDescriptor = Object.getOwnPropertyDescriptor,
      Object_isExtensible = Object.isExtensible,
      Object_getOwnPropertyNames = Object.getOwnPropertyNames,
      uneval_ = (function(){throw Error("JSFUZZ ERROR: Unsupported function (uneval)")}); //uneval;

    // Return true iff ES6 Type(v) isn't Object.
    // Note that `typeof document.all === "undefined"`.
    function isPrimitive(v) {
      return (v === null ||
          v === undefined ||
          typeof v === "boolean" ||
          typeof v === "number" ||
          typeof v === "string" ||
          typeof v === "symbol");
    }

    function assertSameValue(a, b, msg) {
      try {
        assertEq(a, b);
      } catch (exc) {
        throw Error_(exc.message + (msg ? " " + msg : ""));
      }
    }

    function assertSameClass(a, b, msg) {
      var ac = Object_toString(a), bc = Object_toString(b);
      assertSameValue(ac, bc, msg);
      switch (ac) {
      case "[object Function]":
        if (typeof isProxy !== "undefined" && !isProxy(a) && !isProxy(b))
          assertSameValue(Function_toString(a), Function_toString(b), msg);
      }
    }

    function at(prevmsg, segment) {
      return prevmsg ? prevmsg + segment : "at _" + segment;
    }

    // Assert that the arguments a and b are thoroughly structurally equivalent.
    //
    // For the sake of speed, we cut a corner:
    //    var x = {}, y = {}, ax = [x];
    //    assertDeepEq([ax, x], [ax, y]);  // passes (?!)
    //
    // Technically this should fail, since the two object graphs are different.
    // (The graph of [ax, y] contains one more object than the graph of [ax, x].)
    //
    // To get technically correct behavior, pass {strictEquivalence: true}.
    // This is slower because we have to walk the entire graph, and Object.prototype
    // is big.
    //
    return function assertDeepEq(a, b, options) {
      var strictEquivalence = options ? options.strictEquivalence : false;

      function assertSameProto(a, b, msg) {
        check(Object_getPrototypeOf(a), Object_getPrototypeOf(b), at(msg, ".__proto__"));
      }

      function failPropList(na, nb, msg) {
        throw Error_("got own properties " + uneval_(na) + ", expected " + uneval_(nb) +
               (msg ? " " + msg : ""));
      }

      function assertSameProps(a, b, msg) {
        var na = Object_getOwnPropertyNames(a),
          nb = Object_getOwnPropertyNames(b);
        if (na.length !== nb.length)
          failPropList(na, nb, msg);

        // Ignore differences in whether Array elements are stored densely.
        if (Array_isArray(a)) {
          na.sort();
          nb.sort();
        }

        for (var i = 0; i < na.length; i++) {
          var name = na[i];
          if (name !== nb[i])
            failPropList(na, nb, msg);
          var da = Object_getOwnPropertyDescriptor(a, name),
            db = Object_getOwnPropertyDescriptor(b, name);
          var pmsg = at(msg, /^[_$A-Za-z0-9]+$/.test(name)
                     ? /0|[1-9][0-9]*/.test(name) ? "[" + name + "]" : "." + name
                     : "[" + uneval_(name) + "]");
          assertSameValue(da.configurable, db.configurable, at(pmsg, ".[[Configurable]]"));
          assertSameValue(da.enumerable, db.enumerable, at(pmsg, ".[[Enumerable]]"));
          if (Object_hasOwnProperty(da, "value")) {
            if (!Object_hasOwnProperty(db, "value"))
              throw Error_("got data property, expected accessor property" + pmsg);
            check(da.value, db.value, pmsg);
          } else {
            if (Object_hasOwnProperty(db, "value"))
              throw Error_("got accessor property, expected data property" + pmsg);
            check(da.get, db.get, at(pmsg, ".[[Get]]"));
            check(da.set, db.set, at(pmsg, ".[[Set]]"));
          }
        }
      };

      var ab = new Map_();
      var bpath = new Map_();

      function check(a, b, path) {
        if (typeof a === "symbol") {
          // Symbols are primitives, but they have identity.
          // Symbol("x") !== Symbol("x") but
          // assertDeepEq(Symbol("x"), Symbol("x")) should pass.
          if (typeof b !== "symbol") {
            throw Error_("got " + uneval_(a) + ", expected " + uneval_(b) + " " + path);
          } else if (uneval_(a) !== uneval_(b)) {
            // We lamely use uneval_ to distinguish well-known symbols
            // from user-created symbols. The standard doesn't offer
            // a convenient way to do it.
            throw Error_("got " + uneval_(a) + ", expected " + uneval_(b) + " " + path);
          } else if (Map_has(ab, a)) {
            assertSameValue(Map_get(ab, a), b, path);
          } else if (Map_has(bpath, b)) {
            var bPrevPath = Map_get(bpath, b) || "_";
            throw Error_("got distinct symbols " + at(path, "") + " and " +
                   at(bPrevPath, "") + ", expected the same symbol both places");
          } else {
            Map_set(ab, a, b);
            Map_set(bpath, b, path);
          }
        } else if (isPrimitive(a)) {
          assertSameValue(a, b, path);
        } else if (isPrimitive(b)) {
          throw Error_("got " + Object_toString(a) + ", expected " + uneval_(b) + " " + path);
        } else if (Map_has(ab, a)) {
          assertSameValue(Map_get(ab, a), b, path);
        } else if (Map_has(bpath, b)) {
          var bPrevPath = Map_get(bpath, b) || "_";
          throw Error_("got distinct objects " + at(path, "") + " and " + at(bPrevPath, "") +
                 ", expected the same object both places");
        } else {
          Map_set(ab, a, b);
          Map_set(bpath, b, path);
          if (a !== b || strictEquivalence) {
            assertSameClass(a, b, path);
            assertSameProto(a, b, path);
            assertSameProps(a, b, path);
            assertSameValue(Object_isExtensible(a),
                    Object_isExtensible(b),
                    at(path, ".[[Extensible]]"));
          }
        }
      }

      check(a, b, "");
    };
  })();

})(this);
function runNormalizeTest(test) {
  function codePointsToString(points) {
    return points.map(x => String.fromCodePoint(x)).join("");
  }
  function stringify(points) {
    return points.map(x => x.toString(16)).join();
  }

  var source = codePointsToString(test.source);
  var NFC = codePointsToString(test.NFC);
  var NFD = codePointsToString(test.NFD);
  var NFKC = codePointsToString(test.NFKC);
  var NFKD = codePointsToString(test.NFKD);
  var sourceStr = stringify(test.source);
  var nfcStr = stringify(test.NFC);
  var nfdStr = stringify(test.NFD);
  var nfkcStr = stringify(test.NFKC);
  var nfkdStr = stringify(test.NFKD);

  /* NFC */
  assertEq(source.normalize(), NFC, "NFC of " + sourceStr);
  assertEq(NFC.normalize(), NFC, "NFC of " + nfcStr);
  assertEq(NFD.normalize(), NFC, "NFC of " + nfdStr);
  assertEq(NFKC.normalize(), NFKC, "NFC of " + nfkcStr);
  assertEq(NFKD.normalize(), NFKC, "NFC of " + nfkdStr);

  assertEq(source.normalize(undefined), NFC, "NFC of " + sourceStr);
  assertEq(NFC.normalize(undefined), NFC, "NFC of " + nfcStr);
  assertEq(NFD.normalize(undefined), NFC, "NFC of " + nfdStr);
  assertEq(NFKC.normalize(undefined), NFKC, "NFC of " + nfkcStr);
  assertEq(NFKD.normalize(undefined), NFKC, "NFC of " + nfkdStr);

  assertEq(source.normalize("NFC"), NFC, "NFC of " + sourceStr);
  assertEq(NFC.normalize("NFC"), NFC, "NFC of " + nfcStr);
  assertEq(NFD.normalize("NFC"), NFC, "NFC of " + nfdStr);
  assertEq(NFKC.normalize("NFC"), NFKC, "NFC of " + nfkcStr);
  assertEq(NFKD.normalize("NFC"), NFKC, "NFC of " + nfkdStr);

  /* NFD */
  assertEq(source.normalize("NFD"), NFD, "NFD of " + sourceStr);
  assertEq(NFC.normalize("NFD"), NFD, "NFD of " + nfcStr);
  assertEq(NFD.normalize("NFD"), NFD, "NFD of " + nfdStr);
  assertEq(NFKC.normalize("NFD"), NFKD, "NFD of " + nfkcStr);
  assertEq(NFKD.normalize("NFD"), NFKD, "NFD of " + nfkdStr);

  /* NFKC */
  assertEq(source.normalize("NFKC"), NFKC, "NFKC of " + sourceStr);
  assertEq(NFC.normalize("NFKC"), NFKC, "NFKC of " + nfcStr);
  assertEq(NFD.normalize("NFKC"), NFKC, "NFKC of " + nfdStr);
  assertEq(NFKC.normalize("NFKC"), NFKC, "NFKC of " + nfkcStr);
  assertEq(NFKD.normalize("NFKC"), NFKC, "NFKC of " + nfkdStr);

  /* NFKD */
  assertEq(source.normalize("NFKD"), NFKD, "NFKD of " + sourceStr);
  assertEq(NFC.normalize("NFKD"), NFKD, "NFKD of " + nfcStr);
  assertEq(NFD.normalize("NFKD"), NFKD, "NFKD of " + nfdStr);
  assertEq(NFKC.normalize("NFKD"), NFKD, "NFKD of " + nfkcStr);
  assertEq(NFKD.normalize("NFKD"), NFKD, "NFKD of " + nfkdStr);
}
/* -*- indent-tabs-mode: nil; js-indent-level: 2 -*- */

/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function(global) {

  /*
   * Return true if both of these return true:
   * - LENIENT_PRED applied to CODE
   * - STRICT_PRED applied to CODE with a use strict directive added to the front
   *
   * Run STRICT_PRED first, for testing code that affects the global environment
   * in loose mode, but fails in strict mode.
   */
  global.testLenientAndStrict = function testLenientAndStrict(code, lenient_pred, strict_pred) {
    return (strict_pred("'use strict'; " + code) && 
            lenient_pred(code));
  }

  /*
   * parsesSuccessfully(CODE) returns true if CODE parses as function
   * code without an error.
   */
  global.parsesSuccessfully = function parsesSuccessfully(code) {
    try {
      Function(code);
      return true;
    } catch (exception) {
      return false;
    }
  };

  /*
   * parseRaisesException(EXCEPTION)(CODE) returns true if parsing CODE
   * as function code raises EXCEPTION.
   */
  global.parseRaisesException = function parseRaisesException(exception) {
    return function (code) {
      try {
        Function(code);
        return false;
      } catch (actual) {
        return exception.prototype.isPrototypeOf(actual);
      }
    };
  };

  /*
   * returns(VALUE)(CODE) returns true if evaluating CODE (as eval code)
   * completes normally (rather than throwing an exception), yielding a value
   * strictly equal to VALUE.
   */
  global.returns = function returns(value) {
    return function(code) {
      try {
        return eval(code) === value;
      } catch (exception) {
        return false;
      }
    }
  }

})(this);
function hasPipeline() {
    try {
        Function('a |> a');
    } catch (e) {
        return false;
    }

    return true;
}


function runtest(main) {
    try {
        main();
        if (typeof reportCompare === 'function')
            reportCompare(true, true);
    } catch (exc) {
        print(exc.stack);
        throw exc;
    }
}
// Checks that |a_orig| and |b_orig| are:
//   1. Both instances of |type|, and
//   2. Are structurally equivalent (as dictated by the structure of |type|).
function assertTypedEqual(type, a_orig, b_orig) {
  try {
    recur(type, a_orig, b_orig);
  } catch (e) {
    print("failure during "+
          "assertTypedEqual("+type.toSource()+", "+a_orig.toSource()+", "+b_orig.toSource()+")");
    throw e;
  }

  function recur(type, a, b) {
    if (type instanceof ArrayType) {
      assertEq(a.length, type.length);
      assertEq(b.length, type.length);
      for (var i = 0; i < type.length; i++)
        recur(type.elementType, a[i], b[i]);
      } else if (type instanceof StructType) {
        var fieldNames = Object.getOwnPropertyNames(type.fieldTypes);
        for (var i = 0; i < fieldNames.length; i++) {
          var fieldName = fieldNames[i];
          recur(type.fieldTypes[fieldName], a[fieldName], b[fieldName]);
        }
      } else {
        assertEq(a, b);
      }
  }
}
function makeFloat(sign, exp, mantissa) {
    assertEq(sign, sign & 0x1);
    assertEq(exp, exp & 0xFF);
    assertEq(mantissa, mantissa & 0x7FFFFF);

    var i32 = new Int32Array(1);
    var f32 = new Float32Array(i32.buffer);

    i32[0] = (sign << 31) | (exp << 23) | mantissa;
    return f32[0];
}

function makeDouble(sign, exp, mantissa) {
    assertEq(sign, sign & 0x1);
    assertEq(exp, exp & 0x7FF);

    // Can't use bitwise operations on mantissa, as it might be a double
    assertEq(mantissa <= 0xfffffffffffff, true);
    var highBits = (mantissa / Math.pow(2, 32)) | 0;
    var lowBits = mantissa - highBits * Math.pow(2, 32);

    var i32 = new Int32Array(2);
    var f64 = new Float64Array(i32.buffer);

    // Note that this assumes little-endian order, which is the case on tier-1
    // platforms.
    i32[0] = lowBits;
    i32[1] = (sign << 31) | (exp << 20) | highBits;
    return f64[0];
}

function GetType(v) {
    switch (Object.getPrototypeOf(v)) {
        case SIMD.Int8x16.prototype:   return SIMD.Int8x16;
        case SIMD.Int16x8.prototype:   return SIMD.Int16x8;
        case SIMD.Int32x4.prototype:   return SIMD.Int32x4;
        case SIMD.Uint8x16.prototype:  return SIMD.Uint8x16;
        case SIMD.Uint16x8.prototype:  return SIMD.Uint16x8;
        case SIMD.Uint32x4.prototype:  return SIMD.Uint32x4;
        case SIMD.Float32x4.prototype: return SIMD.Float32x4;
        case SIMD.Float64x2.prototype: return SIMD.Float64x2;
        case SIMD.Bool8x16.prototype:  return SIMD.Bool8x16;
        case SIMD.Bool16x8.prototype:  return SIMD.Bool16x8;
        case SIMD.Bool32x4.prototype:  return SIMD.Bool32x4;
        case SIMD.Bool64x2.prototype:  return SIMD.Bool64x2;
    }
}

function assertEqFloat64x2(v, arr) {
    try {
        assertEq(SIMD.Float64x2.extractLane(v, 0), arr[0]);
        assertEq(SIMD.Float64x2.extractLane(v, 1), arr[1]);
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqBool64x2(v, arr) {
    try {
        assertEq(SIMD.Bool64x2.extractLane(v, 0), arr[0]);
        assertEq(SIMD.Bool64x2.extractLane(v, 1), arr[1]);
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqX2(v, arr) {
    var Type = GetType(v);
    if (Type === SIMD.Float64x2) assertEqFloat64x2(v, arr);
    else if (Type === SIMD.Bool64x2) assertEqBool64x2(v, arr);
    else throw new TypeError("Unknown SIMD kind.");
}

function assertEqInt32x4(v, arr) {
    try {
        for (var i = 0; i < 4; i++)
            assertEq(SIMD.Int32x4.extractLane(v, i), arr[i]);
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqUint32x4(v, arr) {
    try {
        for (var i = 0; i < 4; i++)
            assertEq(SIMD.Uint32x4.extractLane(v, i), arr[i]);
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqFloat32x4(v, arr) {
    try {
        for (var i = 0; i < 4; i++)
            assertEq(SIMD.Float32x4.extractLane(v, i), arr[i]);
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqBool32x4(v, arr) {
    try {
        for (var i = 0; i < 4; i++)
            assertEq(SIMD.Bool32x4.extractLane(v, i), arr[i]);
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqX4(v, arr) {
    var Type = GetType(v);
    if (Type === SIMD.Int32x4) assertEqInt32x4(v, arr);
    else if (Type === SIMD.Uint32x4) assertEqUint32x4(v, arr);
    else if (Type === SIMD.Float32x4) assertEqFloat32x4(v, arr);
    else if (Type === SIMD.Bool32x4) assertEqBool32x4(v, arr);
    else throw new TypeError("Unknown SIMD kind.");
}

function assertEqInt16x8(v, arr) {
    try {
        for (var i = 0; i < 8; i++)
            assertEq(SIMD.Int16x8.extractLane(v, i), arr[i]);
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqUint16x8(v, arr) {
    try {
        for (var i = 0; i < 8; i++)
            assertEq(SIMD.Uint16x8.extractLane(v, i), arr[i]);
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqBool16x8(v, arr) {
    try {
        for (var i = 0; i < 8; i++){
            assertEq(SIMD.Bool16x8.extractLane(v, i), arr[i]);
        }
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqX8(v, arr) {
    var Type = GetType(v);
    if (Type === SIMD.Int16x8) assertEqInt16x8(v, arr);
    else if (Type === SIMD.Uint16x8) assertEqUint16x8(v, arr);
    else if (Type === SIMD.Bool16x8) assertEqBool16x8(v, arr);
    else throw new TypeError("Unknown x8 vector.");
}

function assertEqInt8x16(v, arr) {
    try {
        for (var i = 0; i < 16; i++)
            assertEq(SIMD.Int8x16.extractLane(v, i), arr[i]);
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqUint8x16(v, arr) {
    try {
        for (var i = 0; i < 16; i++)
            assertEq(SIMD.Uint8x16.extractLane(v, i), arr[i]);
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqBool8x16(v, arr) {
    try {
        for (var i = 0; i < 16; i++)
            assertEq(SIMD.Bool8x16.extractLane(v, i), arr[i]);
    } catch (e) {
        print("stack trace:", e.stack);
        throw e;
    }
}

function assertEqX16(v, arr) {
    var Type = GetType(v);
    if (Type === SIMD.Int8x16) assertEqInt8x16(v, arr);
    else if (Type === SIMD.Uint8x16) assertEqUint8x16(v, arr);
    else if (Type === SIMD.Bool8x16) assertEqBool8x16(v, arr);
    else throw new TypeError("Unknown x16 vector.");
}

function simdLength(v) {
    var pt = Object.getPrototypeOf(v);
    if (pt == SIMD.Int8x16.prototype || pt == SIMD.Uint8x16.prototype ||
            pt === SIMD.Bool8x16.prototype)
        return 16;
    if (pt == SIMD.Int16x8.prototype || pt == SIMD.Uint16x8.prototype ||
            pt === SIMD.Bool16x8.prototype)
        return 8;
    if (pt === SIMD.Int32x4.prototype || pt === SIMD.Uint32x4.prototype ||
            pt === SIMD.Float32x4.prototype || pt === SIMD.Bool32x4.prototype)
        return 4;
    if (pt === SIMD.Float64x2.prototype || pt == SIMD.Bool64x2.prototype)
        return 2;
    throw new TypeError("Unknown SIMD kind.");
}

function simdLengthType(t) {
    if (t == SIMD.Int8x16 || t == SIMD.Uint8x16 || t == SIMD.Bool8x16)
        return 16;
    else if (t == SIMD.Int16x8 || t == SIMD.Uint16x8 || t == SIMD.Bool16x8)
        return 8;
    else if (t == SIMD.Int32x4 || t == SIMD.Uint32x4 || t == SIMD.Float32x4 || t == SIMD.Bool32x4)
        return 4;
    else if (t == SIMD.Float64x2 || t == SIMD.Bool64x2)
        return 2;
    else
        throw new TypeError("Unknown SIMD kind.");
}

function getAssertFuncFromLength(l) {
    if (l == 2)
        return assertEqX2;
    else if (l == 4)
        return assertEqX4;
    else if (l == 8)
        return assertEqX8;
    else if (l == 16)
        return assertEqX16;
    else
        throw new TypeError("Unknown SIMD kind.");
}

function assertEqVec(v, arr) {
    var Type = GetType(v);
    if (Type === SIMD.Int8x16) assertEqInt8x16(v, arr);
    else if (Type === SIMD.Int16x8) assertEqInt16x8(v, arr);
    else if (Type === SIMD.Int32x4) assertEqInt32x4(v, arr);
    else if (Type === SIMD.Uint8x16) assertEqUint8x16(v, arr);
    else if (Type === SIMD.Uint16x8) assertEqUint16x8(v, arr);
    else if (Type === SIMD.Uint32x4) assertEqUint32x4(v, arr);
    else if (Type === SIMD.Float32x4) assertEqFloat32x4(v, arr);
    else if (Type === SIMD.Float64x2) assertEqFloat64x2(v, arr);
    else if (Type === SIMD.Bool8x16) assertEqBool8x16(v, arr);
    else if (Type === SIMD.Bool16x8) assertEqBool16x8(v, arr);
    else if (Type === SIMD.Bool32x4) assertEqBool32x4(v, arr);
    else if (Type === SIMD.Bool64x2) assertEqBool64x2(v, arr);
    else throw new TypeError("Unknown SIMD Kind");
}

function simdToArray(v) {
    var Type = GetType(v);

    function indexes(n) {
        var arr = [];
        for (var i = 0; i < n; i++) arr.push(i);
        return arr;
    }

    if (Type === SIMD.Bool8x16) {
        return indexes(16).map((i) => SIMD.Bool8x16.extractLane(v, i));
    }

    if (Type === SIMD.Bool16x8) {
        return indexes(8).map((i) => SIMD.Bool16x8.extractLane(v, i));
    }

    if (Type === SIMD.Bool32x4) {
        return indexes(4).map((i) => SIMD.Bool32x4.extractLane(v, i));
    }

    if (Type === SIMD.Bool64x2) {
        return indexes(2).map((i) => SIMD.Bool64x2.extractLane(v, i));
    }

    if (Type === SIMD.Int8x16) {
        return indexes(16).map((i) => SIMD.Int8x16.extractLane(v, i));
    }

    if (Type === SIMD.Int16x8) {
        return indexes(8).map((i) => SIMD.Int16x8.extractLane(v, i));
    }

    if (Type === SIMD.Int32x4) {
        return indexes(4).map((i) => SIMD.Int32x4.extractLane(v, i));
    }

    if (Type === SIMD.Uint8x16) {
        return indexes(16).map((i) => SIMD.Uint8x16.extractLane(v, i));
    }

    if (Type === SIMD.Uint16x8) {
        return indexes(8).map((i) => SIMD.Uint16x8.extractLane(v, i));
    }

    if (Type === SIMD.Uint32x4) {
        return indexes(4).map((i) => SIMD.Uint32x4.extractLane(v, i));
    }

    if (Type === SIMD.Float32x4) {
        return indexes(4).map((i) => SIMD.Float32x4.extractLane(v, i));
    }

    if (Type === SIMD.Float64x2) {
        return indexes(2).map((i) => SIMD.Float64x2.extractLane(v, i));
    }

    throw new TypeError("Unknown SIMD Kind");
}

const INT8_MAX = Math.pow(2, 7) -1;
const INT8_MIN = -Math.pow(2, 7);
assertEq((INT8_MAX + 1) << 24 >> 24, INT8_MIN);
const INT16_MAX = Math.pow(2, 15) - 1;
const INT16_MIN = -Math.pow(2, 15);
assertEq((INT16_MAX + 1) << 16 >> 16, INT16_MIN);
const INT32_MAX = Math.pow(2, 31) - 1;
const INT32_MIN = -Math.pow(2, 31);
assertEq(INT32_MAX + 1 | 0, INT32_MIN);

const UINT8_MAX = Math.pow(2, 8) - 1;
const UINT16_MAX = Math.pow(2, 16) - 1;
const UINT32_MAX = Math.pow(2, 32) - 1;

function testUnaryFunc(v, simdFunc, func) {
    var varr = simdToArray(v);

    var observed = simdToArray(simdFunc(v));
    var expected = varr.map(function(v, i) { return func(varr[i]); });

    for (var i = 0; i < observed.length; i++)
        assertEq(observed[i], expected[i]);
}

function testBinaryFunc(v, w, simdFunc, func) {
    var varr = simdToArray(v);
    var warr = simdToArray(w);

    var observed = simdToArray(simdFunc(v, w));
    var expected = varr.map(function(v, i) { return func(varr[i], warr[i]); });

    for (var i = 0; i < observed.length; i++)
        assertEq(observed[i], expected[i]);
}

function testBinaryCompare(v, w, simdFunc, func, outType) {
    var varr = simdToArray(v);
    var warr = simdToArray(w);

    var inLanes = simdLength(v);
    var observed = simdToArray(simdFunc(v, w));
    var outTypeLen = simdLengthType(outType);
    assertEq(observed.length, outTypeLen);
    for (var i = 0; i < outTypeLen; i++) {
        var j = ((i * inLanes) / outTypeLen) | 0;
        assertEq(observed[i], func(varr[j], warr[j]));
    }
}

function testBinaryScalarFunc(v, scalar, simdFunc, func) {
    var varr = simdToArray(v);

    var observed = simdToArray(simdFunc(v, scalar));
    var expected = varr.map(function(v, i) { return func(varr[i], scalar); });

    for (var i = 0; i < observed.length; i++)
        assertEq(observed[i], expected[i]);
}

// Our array for Int32x4 and Float32x4 will have 16 elements
const SIZE_8_ARRAY = 64;
const SIZE_16_ARRAY = 32;
const SIZE_32_ARRAY = 16;
const SIZE_64_ARRAY = 8;

const SIZE_BYTES = SIZE_32_ARRAY * 4;

function MakeComparator(kind, arr, shared) {
    var bpe = arr.BYTES_PER_ELEMENT;
    var uint8 = (bpe != 1) ? new Uint8Array(arr.buffer) : arr;

    // Size in bytes of a single element in the SIMD vector.
    var sizeOfLaneElem;
    // Typed array constructor corresponding to the SIMD kind.
    var typedArrayCtor;
    switch (kind) {
      case 'Int8x16':
        sizeOfLaneElem = 1;
        typedArrayCtor = Int8Array;
        break;
      case 'Int16x8':
        sizeOfLaneElem = 2;
        typedArrayCtor = Int16Array;
        break;
      case 'Int32x4':
        sizeOfLaneElem = 4;
        typedArrayCtor = Int32Array;
        break;
      case 'Uint8x16':
        sizeOfLaneElem = 1;
        typedArrayCtor = Uint8Array;
        break;
      case 'Uint16x8':
        sizeOfLaneElem = 2;
        typedArrayCtor = Uint16Array;
        break;
      case 'Uint32x4':
        sizeOfLaneElem = 4;
        typedArrayCtor = Uint32Array;
        break;
      case 'Float32x4':
        sizeOfLaneElem = 4;
        typedArrayCtor = Float32Array;
        break;
      case 'Float64x2':
        sizeOfLaneElem = 8;
        typedArrayCtor = Float64Array;
        break;
      default:
        assertEq(true, false, "unknown SIMD kind");
    }
    var lanes = 16 / sizeOfLaneElem;
    // Reads (numElemToRead * sizeOfLaneElem) bytes in arr, and reinterprets
    // these bytes as a typed array equivalent to the typed SIMD vector.
    var slice = function(start, numElemToRead) {
        // Read enough bytes
        var startBytes = start * bpe;
        var endBytes = startBytes + numElemToRead * sizeOfLaneElem;
        var asArray = Array.prototype.slice.call(uint8, startBytes, endBytes);

        // If length is less than SIZE_BYTES bytes, fill with 0.
        // This is needed for load1, load2, load3 which do only partial
        // reads.
        for (var i = asArray.length; i < SIZE_BYTES; i++) asArray[i] = 0;
        assertEq(asArray.length, SIZE_BYTES);

        return new typedArrayCtor(new Uint8Array(asArray).buffer);
    }

    var assertFunc = getAssertFuncFromLength(lanes);
    var type = SIMD[kind];
    return {
        load1: function(index) {
            if (lanes >= 8) // Int8x16 and Int16x8 only support load, no load1/load2/etc.
                return
            var v = type.load1(arr, index);
            assertFunc(v, slice(index, 1));
        },

        load2: function(index) {
            if (lanes !== 4)
                return;
            var v = type.load2(arr, index);
            assertFunc(v, slice(index, 2));
        },

       load3: function(index) {
           if (lanes !== 4)
               return;
           var v = type.load3(arr, index);
           assertFunc(v, slice(index, 3));
        },

        load: function(index) {
           var v = type.load(arr, index);
           assertFunc(v, slice(index, lanes));
        }
    }
}

function testLoad(kind, TA) {
    var lanes = TA.length / 4;
    for (var i = TA.length; i--;)
        TA[i] = i;

    for (var ta of [
                    new Uint8Array(TA.buffer),
                    new Int8Array(TA.buffer),
                    new Uint16Array(TA.buffer),
                    new Int16Array(TA.buffer),
                    new Uint32Array(TA.buffer),
                    new Int32Array(TA.buffer),
                    new Float32Array(TA.buffer),
                    new Float64Array(TA.buffer)
                   ])
    {
        // Invalid args
        assertThrowsInstanceOf(() => SIMD[kind].load(), TypeError);
        assertThrowsInstanceOf(() => SIMD[kind].load(ta), TypeError);
        assertThrowsInstanceOf(() => SIMD[kind].load("hello", 0), TypeError);
        // Indexes must be integers, there is no rounding.
        assertThrowsInstanceOf(() => SIMD[kind].load(ta, 1.5), RangeError);
        assertThrowsInstanceOf(() => SIMD[kind].load(ta, -1), RangeError);
        assertThrowsInstanceOf(() => SIMD[kind].load(ta, "hello"), RangeError);
        assertThrowsInstanceOf(() => SIMD[kind].load(ta, NaN), RangeError);
        // Try to trip up the bounds checking. Int32 is enough for everybody.
        assertThrowsInstanceOf(() => SIMD[kind].load(ta, 0x100000000), RangeError);
        assertThrowsInstanceOf(() => SIMD[kind].load(ta, 0x80000000), RangeError);
        assertThrowsInstanceOf(() => SIMD[kind].load(ta, 0x40000000), RangeError);
        assertThrowsInstanceOf(() => SIMD[kind].load(ta, 0x20000000), RangeError);
        assertThrowsInstanceOf(() => SIMD[kind].load(ta, (1<<30) * (1<<23) - 1), RangeError);
        assertThrowsInstanceOf(() => SIMD[kind].load(ta, (1<<30) * (1<<23)), RangeError);

        // Valid and invalid reads
        var C = MakeComparator(kind, ta);
        var bpe = ta.BYTES_PER_ELEMENT;

        var lastValidArgLoad1   = (SIZE_BYTES - (16 / lanes))  / bpe | 0;
        var lastValidArgLoad2   = (SIZE_BYTES - 8)  / bpe | 0;
        var lastValidArgLoad3   = (SIZE_BYTES - 12) / bpe | 0;
        var lastValidArgLoad    = (SIZE_BYTES - 16) / bpe | 0;

        C.load(0);
        C.load(1);
        C.load(2);
        C.load(3);
        C.load(lastValidArgLoad);

        C.load1(0);
        C.load1(1);
        C.load1(2);
        C.load1(3);
        C.load1(lastValidArgLoad1);

        C.load2(0);
        C.load2(1);
        C.load2(2);
        C.load2(3);
        C.load2(lastValidArgLoad2);

        C.load3(0);
        C.load3(1);
        C.load3(2);
        C.load3(3);
        C.load3(lastValidArgLoad3);

        assertThrowsInstanceOf(() => SIMD[kind].load(ta, lastValidArgLoad + 1), RangeError);
        if (lanes <= 4) {
            assertThrowsInstanceOf(() => SIMD[kind].load1(ta, lastValidArgLoad1 + 1), RangeError);
        }
        if (lanes == 4) {
            assertThrowsInstanceOf(() => SIMD[kind].load2(ta, lastValidArgLoad2 + 1), RangeError);
            assertThrowsInstanceOf(() => SIMD[kind].load3(ta, lastValidArgLoad3 + 1), RangeError);
        }

        // Indexes are coerced with ToNumber. Try some strings that
        // CanonicalNumericIndexString() would reject.
        C.load("1.0e0");
        C.load(" 2");
    }

    if (lanes == 4) {
        // Test ToNumber behavior.
        var obj = {
            valueOf: function() { return 12 }
        }
        var v = SIMD[kind].load(TA, obj);
        assertEqX4(v, [12, 13, 14, 15]);
    }

    var obj = {
        valueOf: function() { throw new TypeError("i ain't a number"); }
    }
    assertThrowsInstanceOf(() => SIMD[kind].load(TA, obj), TypeError);
}

var Helpers = {
    testLoad,
    MakeComparator
};
// List of a few values that are not objects.
var SOME_PRIMITIVE_VALUES = [
    undefined, null,
    false,
    -Infinity, -1.6e99, -1, -0, 0, Math.pow(2, -1074), 1, 4294967295,
    Number.MAX_SAFE_INTEGER, Number.MAX_SAFE_INTEGER + 1, 1.6e99, Infinity, NaN,
    "", "Phaedo",
    Symbol(), Symbol("iterator"), Symbol.for("iterator"), Symbol.iterator
];

var BUGNUMBER;
var summary;


/*
 * Date functions used by tests in Date suite
 *
 */
var msPerDay =   86400000;
var msPerHour =   3600000; // 1000 * 60 * 60
var TZ_DIFF = getTimeZoneDiff();  // offset of tester's timezone from UTC
var TZ_ADJUST = TZ_DIFF * msPerHour;
var TIME_2000  = 946684800000;
var TIME_1900  = -2208988800000;
var UTC_29_FEB_2000 = TIME_2000 + 31*msPerDay + 28*msPerDay;
var UTC_1_JAN_2005 = TIME_2000 + TimeInYear(2000) + TimeInYear(2001) +
  TimeInYear(2002) + TimeInYear(2003) + TimeInYear(2004);
var now = new Date();
var TIME_NOW = now.valueOf();  //valueOf() is to accurate to the millisecond
                               //Date.parse() is accurate only to the second

/*
 * Originally, the test suite used a hard-coded value TZ_DIFF = -8.
 * But that was only valid for testers in the Pacific Standard Time Zone!
 * We calculate the proper number dynamically for any tester. We just
 * have to be careful not to use a date subject to Daylight Savings Time...
 */
function getTimeZoneDiff()
{
  return -((new Date(2000, 1, 1)).getTimezoneOffset())/60;
}

function DaysInYear( y ) {
  if ( y % 4 != 0 ) {
    return 365;
  }
  if ( (y % 4 == 0) && (y % 100 != 0) ) {
    return 366;
  }
  if ( (y % 100 == 0) && (y % 400 != 0) ) {
    return 365;
  }
  if ( (y % 400 == 0) ){
    return 366;
  } else {
    return "ERROR: DaysInYear(" + y + ") case not covered";
  }
}

function TimeInYear( y ) {
  return ( DaysInYear(y) * msPerDay );
}

function runDSTOffsetCachingTestsFraction(part, parts)
{
  BUGNUMBER = 563938;
  summary = 'Cache DST offsets to improve SunSpider score';

  // print(BUGNUMBER + ": " + summary);

  var MAX_UNIX_TIMET = 2145859200;
  var RANGE_EXPANSION_AMOUNT = 30 * 24 * 60 * 60;

  /**
   * Computes the time zone offset in minutes at the given timestamp.
   */
  function tzOffsetFromUnixTimestamp(timestamp)
  {
    var d = new Date(NaN);
    d.setTime(timestamp); // local slot = NaN, UTC slot = timestamp
    return d.getTimezoneOffset(); // get UTC, calculate local => diff in minutes
  }

  /**
   * Clear the DST offset cache, leaving it initialized to include a timestamp
   * completely unlike the provided one (i.e. one very, very far away in time
   * from it).  Thus an immediately following lookup for the provided timestamp
   * will cache-miss and compute a clean value.
   */
  function clearDSTOffsetCache(undesiredTimestamp)
  {
    var opposite = (undesiredTimestamp + MAX_UNIX_TIMET / 2) % MAX_UNIX_TIMET;

    // Generic purge to known, but not necessarily desired, state
    tzOffsetFromUnixTimestamp(0);
    tzOffsetFromUnixTimestamp(MAX_UNIX_TIMET);

    // Purge to desired state.  Cycle 2x in case opposite or undesiredTimestamp
    // is close to 0 or MAX_UNIX_TIMET.
    tzOffsetFromUnixTimestamp(opposite);
    tzOffsetFromUnixTimestamp(undesiredTimestamp);
    tzOffsetFromUnixTimestamp(opposite);
    tzOffsetFromUnixTimestamp(undesiredTimestamp);
  }

  function computeCanonicalTZOffset(timestamp)
  {
    clearDSTOffsetCache(timestamp);
    return tzOffsetFromUnixTimestamp(timestamp);
  }

  var TEST_TIMESTAMPS_SECONDS =
    [
     // Special-ish timestamps
     0,
     RANGE_EXPANSION_AMOUNT,
     MAX_UNIX_TIMET,
    ];

  var ONE_DAY = 24 * 60 * 60;
  var EIGHTY_THREE_HOURS = 83 * 60 * 60;
  var NINETY_EIGHT_HOURS = 98 * 60 * 60;
  function nextIncrement(i)
  {
    return i === EIGHTY_THREE_HOURS ? NINETY_EIGHT_HOURS : EIGHTY_THREE_HOURS;
  }

  // Now add a long sequence of non-special timestamps, from a fixed range, that
  // overlaps a DST change by "a bit" on each side.  67 days should be enough
  // displacement that we can occasionally exercise the implementation's
  // thirty-day expansion and the DST-offset-change logic.  Use two different
  // increments just to be safe and catch something a single increment might not.
  var DST_CHANGE_DATE = 1268553600; // March 14, 2010
  for (var t = DST_CHANGE_DATE - 67 * ONE_DAY,
           i = nextIncrement(NINETY_EIGHT_HOURS),
           end = DST_CHANGE_DATE + 67 * ONE_DAY;
       t < end;
       i = nextIncrement(i), t += i)
  {
    TEST_TIMESTAMPS_SECONDS.push(t);
  }

  var TEST_TIMESTAMPS =
    TEST_TIMESTAMPS_SECONDS.map(function(v) { return v * 1000; });

  /**************
   * BEGIN TEST *
   **************/

  // Compute the correct time zone offsets for all timestamps to be tested.
  var CORRECT_TZOFFSETS = TEST_TIMESTAMPS.map(computeCanonicalTZOffset);

  // Intentionally and knowingly invoking every single logic path in the cache
  // isn't easy for a human to get right (and know he's gotten it right), so
  // let's do it the easy way: exhaustively try all possible four-date sequences
  // selecting from our array of possible timestamps.

  var sz = TEST_TIMESTAMPS.length;
  var start = Math.floor((part - 1) / parts * sz);
  var end = Math.floor(part / parts * sz);

  print("Exhaustively testing timestamps " +
        "[" + start + ", " + end + ") of " + sz + "...");

  try
  {
    for (var i = start; i < end; i++)
    {
      // print("Testing timestamp " + i + "...");

      var t1 = TEST_TIMESTAMPS[i];
      for (var j = 0; j < sz; j++)
      {
        var t2 = TEST_TIMESTAMPS[j];
        for (var k = 0; k < sz; k++)
        {
          var t3 = TEST_TIMESTAMPS[k];
          for (var w = 0; w < sz; w++)
          {
            var t4 = TEST_TIMESTAMPS[w];

            clearDSTOffsetCache(t1);

            var tzo1 = tzOffsetFromUnixTimestamp(t1);
            var tzo2 = tzOffsetFromUnixTimestamp(t2);
            var tzo3 = tzOffsetFromUnixTimestamp(t3);
            var tzo4 = tzOffsetFromUnixTimestamp(t4);

            assertEq(tzo1, CORRECT_TZOFFSETS[i]);
            assertEq(tzo2, CORRECT_TZOFFSETS[j]);
            assertEq(tzo3, CORRECT_TZOFFSETS[k]);
            assertEq(tzo4, CORRECT_TZOFFSETS[w]);
          }
        }
      }
    }
  }
  catch (e)
  {
    assertEq(true, false,
             "Error when testing with timestamps " +
             i + ", " + j + ", " + k + ", " + w +
             " (" + t1 + ", " + t2 + ", " + t3 + ", " + t4 + ")!");
  }

  reportCompare(true, true);
  // print("All tests passed!");
}
function assertThrownErrorContains(thunk, substr) {
    try {
        thunk();
    } catch (e) {
        if (e.message.indexOf(substr) !== -1)
            return;
        throw new Error("Expected error containing " + substr + ", got " + e);
    }
    throw new Error("Expected error containing " + substr + ", no exception thrown");
}
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

function assertFalse(a) { assertEq(a, false) }
function assertTrue(a) { assertEq(a, true) }
function assertNotEq(found, not_expected) { assertEq(Object.is(found, not_expected), false) }
function assertIteratorResult(result, value, done) {
    assertDeepEq(result.value, value);
    assertEq(result.done, done);
}
function assertIteratorNext(iter, value) {
    assertIteratorResult(iter.next(), value, false);
}
function assertIteratorDone(iter, value) {
    assertIteratorResult(iter.next(), value, true);
}
// The nearest representable values to +1.0.
const ONE_PLUS_EPSILON = 1 + Math.pow(2, -52);  // 0.9999999999999999
const ONE_MINUS_EPSILON = 1 - Math.pow(2, -53);  // 1.0000000000000002

{
    const fail = function (msg) {
        var exc = new Error(msg);
        try {
            // Try to improve on exc.fileName and .lineNumber; leave exc.stack
            // alone. We skip two frames: fail() and its caller, an assertX()
            // function.
            var frames = exc.stack.trim().split("\n");
            if (frames.length > 2) {
                var m = /@([^@:]*):([0-9]+)$/.exec(frames[2]);
                if (m) {
                    exc.fileName = m[1];
                    exc.lineNumber = +m[2];
                }
            }
        } catch (ignore) { throw ignore;}
        throw exc;
    };

    let ENDIAN;  // 0 for little-endian, 1 for big-endian.

    // Return the difference between the IEEE 754 bit-patterns for a and b.
    //
    // This is meaningful when a and b are both finite and have the same
    // sign. Then the following hold:
    //
    //   * If a === b, then diff(a, b) === 0.
    //
    //   * If a !== b, then diff(a, b) === 1 + the number of representable values
    //                                         between a and b.
    //
    const f = new Float64Array([0, 0]);
    const u = new Uint32Array(f.buffer);
    const diff = function (a, b) {
        f[0] = a;
        f[1] = b;
        //print(u[1].toString(16) + u[0].toString(16) + " " + u[3].toString(16) + u[2].toString(16));
        return Math.abs((u[3-ENDIAN] - u[1-ENDIAN]) * 0x100000000 + u[2+ENDIAN] - u[0+ENDIAN]);
    };

    // Set ENDIAN to the platform's endianness.
    ENDIAN = 0;  // try little-endian first
    if (diff(2, 4) === 0x100000)  // exact wrong answer we'll get on a big-endian platform
        ENDIAN = 1;
    assertEq(diff(2,4), 0x10000000000000);
    assertEq(diff(0, Number.MIN_VALUE), 1);
    assertEq(diff(1, ONE_PLUS_EPSILON), 1);
    assertEq(diff(1, ONE_MINUS_EPSILON), 1);

    var assertNear = function assertNear(a, b, tolerance=1) {
        if (!Number.isFinite(b)) {
            fail("second argument to assertNear (expected value) must be a finite number");
        } else if (Number.isNaN(a)) {
            fail("got NaN, expected a number near " + b);
        } else if (!Number.isFinite(a)) {
            if (b * Math.sign(a) < Number.MAX_VALUE)
                fail("got " + a + ", expected a number near " + b);
        } else {
            // When the two arguments do not have the same sign bit, diff()
            // returns some huge number. So if b is positive or negative 0,
            // make target the zero that has the same sign bit as a.
            var target = b === 0 ? a * 0 : b;
            var err = diff(a, target);
            if (err > tolerance) {
                fail("got " + a + ", expected a number near " + b +
                     " (relative error: " + err + ")");
            }
        }
    };
}
function testJSON(str, expectSyntaxError)
{
  // Leading and trailing whitespace never affect parsing, so test the string
  // multiple times with and without whitespace around it as it's easy and can
  // potentially detect bugs.

  // Try the provided string
  try
  {
    JSON.parse(str);
    reportCompare(false, expectSyntaxError,
                  "string <" + str + "> " +
                  "should" + (expectSyntaxError ? "n't" : "") + " " +
                  "have parsed as JSON");
  }
  catch (e)
  {
    if (!(e instanceof SyntaxError))
    {
      reportCompare(true, false,
                    "parsing string <" + str + "> threw a non-SyntaxError " +
                    "exception: " + e);
    }
    else
    {
      reportCompare(true, expectSyntaxError,
                    "string <" + str + "> " +
                    "should" + (expectSyntaxError ? "n't" : "") + " " +
                    "have parsed as JSON, exception: " + e);
    }
  }

  // Now try the provided string with trailing whitespace
  try
  {
    JSON.parse(str + " ");
    reportCompare(false, expectSyntaxError,
                  "string <" + str + " > " +
                  "should" + (expectSyntaxError ? "n't" : "") + " " +
                  "have parsed as JSON");
  }
  catch (e)
  {
    if (!(e instanceof SyntaxError))
    {
      reportCompare(true, false,
                    "parsing string <" + str + " > threw a non-SyntaxError " +
                    "exception: " + e);
    }
    else
    {
      reportCompare(true, expectSyntaxError,
                    "string <" + str + " > " +
                    "should" + (expectSyntaxError ? "n't" : "") + " " +
                    "have parsed as JSON, exception: " + e);
    }
  }

  // Now try the provided string with leading whitespace
  try
  {
    JSON.parse(" " + str);
    reportCompare(false, expectSyntaxError,
                  "string < " + str + "> " +
                  "should" + (expectSyntaxError ? "n't" : "") + " " +
                  "have parsed as JSON");
  }
  catch (e)
  {
    if (!(e instanceof SyntaxError))
    {
      reportCompare(true, false,
                    "parsing string < " + str + "> threw a non-SyntaxError " +
                    "exception: " + e);
    }
    else
    {
      reportCompare(true, expectSyntaxError,
                    "string < " + str + "> " +
                    "should" + (expectSyntaxError ? "n't" : "") + " " +
                    "have parsed as JSON, exception: " + e);
    }
  }

  // Now try the provided string with whitespace surrounding it
  try
  {
    JSON.parse(" " + str + " ");
    reportCompare(false, expectSyntaxError,
                  "string < " + str + " > " +
                  "should" + (expectSyntaxError ? "n't" : "") + " " +
                  "have parsed as JSON");
  }
  catch (e)
  {
    if (!(e instanceof SyntaxError))
    {
      reportCompare(true, false,
                    "parsing string < " + str + " > threw a non-SyntaxError " +
                    "exception: " + e);
    }
    else
    {
      reportCompare(true, expectSyntaxError,
                    "string < " + str + " > " +
                    "should" + (expectSyntaxError ? "n't" : "") + " " +
                    "have parsed as JSON, exception: " + e);
    }
  }
}
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function(global) {
    function func() {
    }
    class C {
        foo() {
        }
        static foo() {
        }
    }

    function test_one(pattern, val, opt) {
        var stmts = [];
        var i = 0;
        var c;

        stmts.push(`var ${pattern} = ${val};`);

        for (var stmt of stmts) {
            if (!opt.no_plain) {
                eval(`
${stmt}
`);
            }

            if (!opt.no_func) {
                eval(`
function f${i}() {
  ${stmt}
}
f${i}();
`);
                i++;

                eval(`
var f${i} = function foo() {
  ${stmt}
};
f${i}();
`);
                i++;

                eval(`
var f${i} = () => {
  ${stmt}
};
f${i}();
`);
                i++;
            }

            if (!opt.no_gen) {
                eval(`
function* g${i}() {
  ${stmt}
}
[...g${i}()];
`);
                i++;

                eval(`
var g${i} = function* foo() {
  ${stmt}
};
[...g${i}()];
`);
                i++;
            }

            if (!opt.no_ctor) {
                eval(`
class D${i} {
  constructor() {
    ${stmt}
  }
}
new D${i}();
`);
                i++;
            }

            if (!opt.no_derived_ctor) {
                if (opt.no_pre_super) {
                    eval(`
class D${i} extends C {
  constructor() {
    ${stmt}
    try { super(); } catch (e) {}
  }
}
new D${i}();
`);
                    i++;
                } else {
                    eval(`
class D${i} extends C {
  constructor() {
    super();
    ${stmt}
  }
}
new D${i}();
`);
                    i++;
                }
            }

            if (!opt.no_method) {
                eval(`
class D${i} extends C {
  method() {
    ${stmt}
  }
  static staticMethod() {
    ${stmt}
  }
}
new D${i}().method();
D${i}.staticMethod();
`);
                i++;
            }
        }

        if (!opt.no_func_arg) {
            eval(`
function f${i}(${pattern}) {}
f${i}(${val});
`);
            i++;

            eval(`
var f${i} = function foo(${pattern}) {};
f${i}(${val});
`);
            i++;

            eval(`
var f${i} = (${pattern}) => {};
f${i}(${val});
`);
            i++;
        }

        if (!opt.no_gen_arg) {
            eval(`
function* g${i}(${pattern}) {}
[...g${i}(${val})];
`);
            i++;

            eval(`
var g${i} = function* foo(${pattern}) {};
[...g${i}(${val})];
`);
            i++;
        }
    }

    function test(expr, opt={}) {
        var pattern = `[a=${expr}, ...c]`;
        test_one(pattern, "[]", opt);
        test_one(pattern, "[1]", opt);

        pattern = `[,a=${expr}]`;
        test_one(pattern, "[]", opt);
        test_one(pattern, "[1]", opt);
        test_one(pattern, "[1, 2]", opt);

        pattern = `[{x: [a=${expr}]}]`;
        test_one(pattern, "[{x: [1]}]", opt);

        pattern = `[x=[a=${expr}]=[]]`;
        test_one(pattern, "[]", opt);
        test_one(pattern, "[1]", opt);

        pattern = `[x=[a=${expr}]=[1]]`;
        test_one(pattern, "[]", opt);
        test_one(pattern, "[1]", opt);
    }

    global.testDestructuringArrayDefault = test;
})(this);

(function(global) {
  /*
   * Date: 07 February 2001
   *
   * Functionality common to Array testing -
   */
  //-----------------------------------------------------------------------------


  var CHAR_LBRACKET = '[';
  var CHAR_RBRACKET = ']';
  var CHAR_QT_DBL = '"';
  var CHAR_QT = "'";
  var CHAR_NL = '\n';
  var CHAR_COMMA = ',';
  var CHAR_SPACE = ' ';
  var TYPE_STRING = typeof 'abc';


  /*
   * If available, arr.toSource() gives more detail than arr.toString()
   *
   * var arr = Array(1,2,'3');
   *
   * arr.toSource()
   * [1, 2, "3"]
   *
   * arr.toString()
   * 1,2,3
   *
   * But toSource() doesn't exist in Rhino, so use our own imitation, below -
   *
   */
  function formatArray(arr)
  {
    try
    {
      return arr.toSource();
    }
    catch(e)
    {
      return toSource(arr);
    }
  }

  global.formatArray = formatArray;

  /*
   * Imitate SpiderMonkey's arr.toSource() method:
   *
   * a) Double-quote each array element that is of string type
   * b) Represent |undefined| and |null| by empty strings
   * c) Delimit elements by a comma + single space
   * d) Do not add delimiter at the end UNLESS the last element is |undefined|
   * e) Add square brackets to the beginning and end of the string
   */
  function toSource(arr)
  {
    var delim = CHAR_COMMA + CHAR_SPACE;
    var elt = '';
    var ret = '';
    var len = arr.length;

    for (i=0; i<len; i++)
    {
      elt = arr[i];

      switch(true)
      {
	case (typeof elt === TYPE_STRING) :
	ret += doubleQuote(elt);
	break;

	case (elt === undefined || elt === null) :
	break; // add nothing but the delimiter, below -

	default:
	ret += elt.toString();
      }

      if ((i < len-1) || (elt === undefined))
	ret += delim;
    }

    return  CHAR_LBRACKET + ret + CHAR_RBRACKET;
  }

  global.toSource = toSource;

  function doubleQuote(text)
  {
    return CHAR_QT_DBL + text + CHAR_QT_DBL;
  }


  function singleQuote(text)
  {
    return CHAR_QT + text + CHAR_QT;
  }

})(this);
(function(global) {
    "use strict";

    const {
        Float32Array, Float64Array, Object, Reflect, SharedArrayBuffer, WeakMap,
        assertEq
    } = global;
    const {
        apply: Reflect_apply,
        construct: Reflect_construct,
    } = Reflect;
    const {
        get: WeakMap_prototype_get,
        has: WeakMap_prototype_has,
    } = WeakMap.prototype;

    const sharedConstructors = new WeakMap();

    // Synthesize a constructor for a shared memory array from the constructor
    // for unshared memory. This has "good enough" fidelity for many uses. In
    // cases where it's not good enough, call isSharedConstructor for local
    // workarounds.
    function sharedConstructor(baseConstructor) {
        // Create SharedTypedArray as a subclass of %TypedArray%, following the
        // built-in %TypedArray% subclasses.
        class SharedTypedArray extends Object.getPrototypeOf(baseConstructor) {
            constructor(...args) {
                var array = Reflect_construct(baseConstructor, args);
                var {buffer, byteOffset, length} = array;
                var sharedBuffer = new SharedArrayBuffer(buffer.byteLength);
                var sharedArray = Reflect_construct(baseConstructor,
                                                    [sharedBuffer, byteOffset, length],
                                                    new.target);
                for (var i = 0; i < length; i++)
                    sharedArray[i] = array[i];
                assertEq(sharedArray.buffer, sharedBuffer);
                return sharedArray;
            }
        }

        // 22.2.5.1 TypedArray.BYTES_PER_ELEMENT
        Object.defineProperty(SharedTypedArray, "BYTES_PER_ELEMENT",
                              {__proto__: null, value: baseConstructor.BYTES_PER_ELEMENT});

        // 22.2.6.1 TypedArray.prototype.BYTES_PER_ELEMENT
        Object.defineProperty(SharedTypedArray.prototype, "BYTES_PER_ELEMENT",
                              {__proto__: null, value: baseConstructor.BYTES_PER_ELEMENT});

        // Share the same name with the base constructor to avoid calling
        // isSharedConstructor() in multiple places.
        Object.defineProperty(SharedTypedArray, "name",
                              {__proto__: null, value: baseConstructor.name});

        sharedConstructors.set(SharedTypedArray, baseConstructor);

        return SharedTypedArray;
    }

    /**
     * All TypedArray constructors for unshared memory.
     */
    const typedArrayConstructors = Object.freeze([
        Int8Array,
        Uint8Array,
        Uint8ClampedArray,
        Int16Array,
        Uint16Array,
        Int32Array,
        Uint32Array,
        Float32Array,
        Float64Array,
    ]);

    /**
     * All TypedArray constructors for shared memory.
     */
    const sharedTypedArrayConstructors = Object.freeze(
        typeof SharedArrayBuffer === "function"
        ? typedArrayConstructors.map(sharedConstructor)
        : []
    );

    /**
     * All TypedArray constructors for unshared and shared memory.
     */
    const anyTypedArrayConstructors = Object.freeze([
        ...typedArrayConstructors, ...sharedTypedArrayConstructors,
    ]);

    /**
     * Returns `true` if `constructor` is a TypedArray constructor for shared
     * memory.
     */
    function isSharedConstructor(constructor) {
        return Reflect_apply(WeakMap_prototype_has, sharedConstructors, [constructor]);
    }

    /**
     * Returns `true` if `constructor` is a TypedArray constructor for shared
     * or unshared memory, with an underlying element type of either Float32 or
     * Float64.
     */
    function isFloatConstructor(constructor) {
        if (isSharedConstructor(constructor))
            constructor = Reflect_apply(WeakMap_prototype_get, sharedConstructors, [constructor]);
        return constructor == Float32Array || constructor == Float64Array;
    }

    global.typedArrayConstructors = typedArrayConstructors;
    global.sharedTypedArrayConstructors = sharedTypedArrayConstructors;
    global.anyTypedArrayConstructors = anyTypedArrayConstructors;
    global.isSharedConstructor = isSharedConstructor;
    global.isFloatConstructor = isFloatConstructor;
})(this);
/* -*- tab-width: 2; indent-tabs-mode: nil; js-indent-level: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

/*
 * Date: 07 February 2001
 *
 * Functionality common to RegExp testing -
 */
//-----------------------------------------------------------------------------

(function(global) {

  var MSG_PATTERN = '\nregexp = ';
  var MSG_STRING = '\nstring = ';
  var MSG_EXPECT = '\nExpect: ';
  var MSG_ACTUAL = '\nActual: ';
  var ERR_LENGTH = '\nERROR !!! match arrays have different lengths:';
  var ERR_MATCH = '\nERROR !!! regexp failed to give expected match array:';
  var ERR_NO_MATCH = '\nERROR !!! regexp FAILED to match anything !!!';
  var ERR_UNEXP_MATCH = '\nERROR !!! regexp MATCHED when we expected it to fail !!!';
  var CHAR_LBRACKET = '[';
  var CHAR_RBRACKET = ']';
  var CHAR_QT_DBL = '"';
  var CHAR_QT = "'";
  var CHAR_NL = '\n';
  var CHAR_COMMA = ',';
  var CHAR_SPACE = ' ';
  var TYPE_STRING = typeof 'abc';



  global.testRegExp = function testRegExp(statuses, patterns, strings, actualmatches, expectedmatches)
  {
    var status = '';
    var pattern = new RegExp();
    var string = '';
    var actualmatch = new Array();
    var expectedmatch = new Array();
    var state = '';
    var lActual = -1;
    var lExpect = -1;


    for (var i=0; i != patterns.length; i++)
    {
      status = statuses[i];
      pattern = patterns[i];
      string = strings[i];
      actualmatch=actualmatches[i];
      expectedmatch=expectedmatches[i];
      state = getState(status, pattern, string);

      description = status;

      if(actualmatch)
      {
        actual = formatArray(actualmatch);
        if(expectedmatch)
        {
          // expectedmatch and actualmatch are arrays -
          lExpect = expectedmatch.length;
          lActual = actualmatch.length;

          var expected = formatArray(expectedmatch);

          if (lActual != lExpect)
          {
            reportCompare(lExpect, lActual,
                          state + ERR_LENGTH +
                          MSG_EXPECT + expected +
                          MSG_ACTUAL + actual +
                          CHAR_NL
	                       );
            continue;
          }

          // OK, the arrays have same length -
          if (expected != actual)
          {
            reportCompare(expected, actual,
                          state + ERR_MATCH +
                          MSG_EXPECT + expected +
                          MSG_ACTUAL + actual +
                          CHAR_NL
	                       );
          }
          else
          {
            reportCompare(expected, actual, state)
	        }

        }
        else //expectedmatch is null - that is, we did not expect a match -
        {
          expected = expectedmatch;
          reportCompare(expected, actual,
                        state + ERR_UNEXP_MATCH +
                        MSG_EXPECT + expectedmatch +
                        MSG_ACTUAL + actual +
                        CHAR_NL
	                     );
        }

      }
      else // actualmatch is null
      {
        if (expectedmatch)
        {
          actual = actualmatch;
          reportCompare(expected, actual,
                        state + ERR_NO_MATCH +
                        MSG_EXPECT + expectedmatch +
                        MSG_ACTUAL + actualmatch +
                        CHAR_NL
	                     );
        }
        else // we did not expect a match
        {
          // Being ultra-cautious. Presumably expectedmatch===actualmatch===null
          expected = expectedmatch;
          actual   = actualmatch;
          reportCompare (expectedmatch, actualmatch, state);
        }
      }
    }
  }

  function getState(status, pattern, string)
  {
    /*
     * Escape \n's, etc. to make them LITERAL in the presentation string.
     * We don't have to worry about this in |pattern|; such escaping is
     * done automatically by pattern.toString(), invoked implicitly below.
     *
     * One would like to simply do: string = string.replace(/(\s)/g, '\$1').
     * However, the backreference $1 is not a literal string value,
     * so this method doesn't work.
     *
     * Also tried string = string.replace(/(\s)/g, escape('$1'));
     * but this just inserts the escape of the literal '$1', i.e. '%241'.
     */
    string = string.replace(/\n/g, '\\n');
    string = string.replace(/\r/g, '\\r');
    string = string.replace(/\t/g, '\\t');
    string = string.replace(/\v/g, '\\v');
    string = string.replace(/\f/g, '\\f');

    return (status + MSG_PATTERN + pattern + MSG_STRING + singleQuote(string));
  }



  /*
   * If available, arr.toSource() gives more detail than arr.toString()
   *
   * var arr = Array(1,2,'3');
   *
   * arr.toSource()
   * [1, 2, "3"]
   *
   * arr.toString()
   * 1,2,3
   *
   * But toSource() doesn't exist in Rhino, so use our own imitation, below -
   *
   */
  function formatArray(arr)
  {
    try
    {
      return arr.toSource();
    }
    catch(e)
    {
      return toSource(arr);
    }
  }


  /*
   * Imitate SpiderMonkey's arr.toSource() method:
   *
   * a) Double-quote each array element that is of string type
   * b) Represent |undefined| and |null| by empty strings
   * c) Delimit elements by a comma + single space
   * d) Do not add delimiter at the end UNLESS the last element is |undefined|
   * e) Add square brackets to the beginning and end of the string
   */
  function toSource(arr)
  {
    var delim = CHAR_COMMA + CHAR_SPACE;
    var elt = '';
    var ret = '';
    var len = arr.length;

    for (i=0; i<len; i++)
    {
      elt = arr[i];

      switch(true)
      {
        case (typeof elt === TYPE_STRING) :
        ret += doubleQuote(elt);
        break;

        case (elt === undefined || elt === null) :
        break; // add nothing but the delimiter, below -

        default:
        ret += elt.toString();
      }

      if ((i < len-1) || (elt === undefined))
        ret += delim;
    }

    return  CHAR_LBRACKET + ret + CHAR_RBRACKET;
  }


  function doubleQuote(text)
  {
    return CHAR_QT_DBL + text + CHAR_QT_DBL;
  }


  function singleQuote(text)
  {
    return CHAR_QT + text + CHAR_QT;
  }

  global.makeExpectedMatch = function makeExpectedMatch(arr, index, input) {
    var expectedMatch = {
      index: index,
      input: input,
      length: arr.length,
    };

    for (var i = 0; i < arr.length; ++i)
      expectedMatch[i] = arr[i];

    return expectedMatch;
  }

  global.checkRegExpMatch = function checkRegExpMatch(actual, expected) {
    assertEq(actual.length, expected.length);
    for (var i = 0; i < actual.length; ++i)
      assertEq(actual[i], expected[i]);

    assertEq(actual.index, expected.index);
    assertEq(actual.input, expected.input);
  }

})(this);
/* -*- indent-tabs-mode: nil; js-indent-level: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

/*
 * Date: 14 Mar 2001
 *
 * SUMMARY: Utility functions for testing objects -
 *
 * Suppose obj is an instance of a native type, e.g. Number.
 * Then obj.toString() invokes Number.prototype.toString().
 * We would also like to access Object.prototype.toString().
 *
 * The difference is this: suppose obj = new Number(7).
 * Invoking Number.prototype.toString() on this just returns 7.
 * Object.prototype.toString() on this returns '[object Number]'.
 *
 * The getJSClass() function returns 'Number', the [[Class]] property of obj.
 * See ECMA-262 Edition 3,  13-Oct-1999,  Section 8.6.2 
 */
//-----------------------------------------------------------------------------


var cnNoObject = 'Unexpected Error!!! Parameter to this function must be an object';
var cnNoClass = 'Unexpected Error!!! Cannot find Class property';
var cnObjectToString = Object.prototype.toString;
var GLOBAL = 'global';


// checks that it's safe to call findType()
function getJSClass(obj)
{
  if (isObject(obj))
    return findClass(findType(obj));
  return cnNoObject;
}


function findType(obj)
{
  return cnObjectToString.apply(obj);
}


// given '[object Number]',  return 'Number'
function findClass(sType)
{
  var re =  /^\[.*\s+(\w+)\s*\]$/;
  var a = sType.match(re);
 
  if (a && a[1])
    return a[1];
  return cnNoClass;
}


function isObject(obj)
{
  return obj instanceof Object;
}

/* -*- tab-width: 2; indent-tabs-mode: nil; js-indent-level: 2 -*- */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */


(function(global) {
  /*
   * Date: 07 February 2001
   *
   * Functionality common to RegExp testing -
   */
  //-----------------------------------------------------------------------------

  var MSG_PATTERN = '\nregexp = ';
  var MSG_STRING = '\nstring = ';
  var MSG_EXPECT = '\nExpect: ';
  var MSG_ACTUAL = '\nActual: ';
  var ERR_LENGTH = '\nERROR !!! match arrays have different lengths:';
  var ERR_MATCH = '\nERROR !!! regexp failed to give expected match array:';
  var ERR_NO_MATCH = '\nERROR !!! regexp FAILED to match anything !!!';
  var ERR_UNEXP_MATCH = '\nERROR !!! regexp MATCHED when we expected it to fail !!!';
  var CHAR_LBRACKET = '[';
  var CHAR_RBRACKET = ']';
  var CHAR_QT_DBL = '"';
  var CHAR_QT = "'";
  var CHAR_NL = '\n';
  var CHAR_COMMA = ',';
  var CHAR_SPACE = ' ';
  var TYPE_STRING = typeof 'abc';



  function testRegExp(statuses, patterns, strings, actualmatches, expectedmatches)
  {
    var status = '';
    var pattern = new RegExp();
    var string = '';
    var actualmatch = new Array();
    var expectedmatch = new Array();
    var state = '';
    var lActual = -1;
    var lExpect = -1;


    for (var i=0; i != patterns.length; i++)
    {
      status = statuses[i];
      pattern = patterns[i];
      string = strings[i];
      actualmatch=actualmatches[i];
      expectedmatch=expectedmatches[i];
      state = getState(status, pattern, string);

      description = status;

      if(actualmatch)
      {
        actual = formatArray(actualmatch);
        if(expectedmatch)
        {
          // expectedmatch and actualmatch are arrays -
          lExpect = expectedmatch.length;
          lActual = actualmatch.length;

          var expected = formatArray(expectedmatch);

          if (lActual != lExpect)
          {
            reportCompare(lExpect, lActual,
                          state + ERR_LENGTH +
                          MSG_EXPECT + expected +
                          MSG_ACTUAL + actual +
                          CHAR_NL
	                       );
            continue;
          }

          // OK, the arrays have same length -
          if (expected != actual)
          {
            reportCompare(expected, actual,
                          state + ERR_MATCH +
                          MSG_EXPECT + expected +
                          MSG_ACTUAL + actual +
                          CHAR_NL
	                       );
          }
          else
          {
            reportCompare(expected, actual, state)
	        }

        }
        else //expectedmatch is null - that is, we did not expect a match -
        {
          expected = expectedmatch;
          reportCompare(expected, actual,
                        state + ERR_UNEXP_MATCH +
                        MSG_EXPECT + expectedmatch +
                        MSG_ACTUAL + actual +
                        CHAR_NL
	                     );
        }

      }
      else // actualmatch is null
      {
        if (expectedmatch)
        {
          actual = actualmatch;
          reportCompare(expected, actual,
                        state + ERR_NO_MATCH +
                        MSG_EXPECT + expectedmatch +
                        MSG_ACTUAL + actualmatch +
                        CHAR_NL
	                     );
        }
        else // we did not expect a match
        {
          // Being ultra-cautious. Presumably expectedmatch===actualmatch===null
          expected = expectedmatch;
          actual   = actualmatch;
          reportCompare (expectedmatch, actualmatch, state);
        }
      }
    }
  }

  global.testRegExp = testRegExp;

  function getState(status, pattern, string)
  {
    /*
     * Escape \n's, etc. to make them LITERAL in the presentation string.
     * We don't have to worry about this in |pattern|; such escaping is
     * done automatically by pattern.toString(), invoked implicitly below.
     *
     * One would like to simply do: string = string.replace(/(\s)/g, '\$1').
     * However, the backreference $1 is not a literal string value,
     * so this method doesn't work.
     *
     * Also tried string = string.replace(/(\s)/g, escape('$1'));
     * but this just inserts the escape of the literal '$1', i.e. '%241'.
     */
    string = string.replace(/\n/g, '\\n');
    string = string.replace(/\r/g, '\\r');
    string = string.replace(/\t/g, '\\t');
    string = string.replace(/\v/g, '\\v');
    string = string.replace(/\f/g, '\\f');

    return (status + MSG_PATTERN + pattern + MSG_STRING + singleQuote(string));
  }


  /*
   * If available, arr.toSource() gives more detail than arr.toString()
   *
   * var arr = Array(1,2,'3');
   *
   * arr.toSource()
   * [1, 2, "3"]
   *
   * arr.toString()
   * 1,2,3
   *
   * But toSource() doesn't exist in Rhino, so use our own imitation, below -
   *
   */
  function formatArray(arr)
  {
    try
    {
      return arr.toSource();
    }
    catch(e)
    {
      return toSource(arr);
    }
  }


  /*
   * Imitate SpiderMonkey's arr.toSource() method:
   *
   * a) Double-quote each array element that is of string type
   * b) Represent |undefined| and |null| by empty strings
   * c) Delimit elements by a comma + single space
   * d) Do not add delimiter at the end UNLESS the last element is |undefined|
   * e) Add square brackets to the beginning and end of the string
   */
  function toSource(arr)
  {
    var delim = CHAR_COMMA + CHAR_SPACE;
    var elt = '';
    var ret = '';
    var len = arr.length;

    for (i=0; i<len; i++)
    {
      elt = arr[i];

      switch(true)
      {
        case (typeof elt === TYPE_STRING) :
        ret += doubleQuote(elt);
        break;

        case (elt === undefined || elt === null) :
        break; // add nothing but the delimiter, below -

        default:
        ret += elt.toString();
      }

      if ((i < len-1) || (elt === undefined))
        ret += delim;
    }

    return  CHAR_LBRACKET + ret + CHAR_RBRACKET;
  }


  function doubleQuote(text)
  {
    return CHAR_QT_DBL + text + CHAR_QT_DBL;
  }


  function singleQuote(text)
  {
    return CHAR_QT + text + CHAR_QT;
 }

})(this);


(function(global) {

  // The Worker constructor can take a relative URL, but different test runners
  // run in different enough environments that it doesn't all just automatically
  // work. For the shell, we use just a filename; for the browser, see browser.js.
  var workerDir = '';

  // Assert that cloning b does the right thing as far as we can tell.
  // Caveat: getters in b must produce the same value each time they're
  // called. We may call them several times.
  //
  // If desc is provided, then the very first thing we do to b is clone it.
  // (The self-modifying object test counts on this.)
  //
  function clone_object_check(b, desc) {
    function classOf(obj) {
      return Object.prototype.toString.call(obj);
    }

    function ownProperties(obj) {
      return Object.getOwnPropertyNames(obj).
        map(function (p) { return [p, Object.getOwnPropertyDescriptor(obj, p)]; });
    }

    function isCloneable(pair) {
      return typeof pair[0] === 'string' && pair[1].enumerable;
    }

    function notIndex(p) {
      var u = p >>> 0;
      return !("" + u == p && u != 0xffffffff);
    }

    function assertIsCloneOf(a, b, path) {
      assertEq(a === b, false);

      var ca = classOf(a);
      assertEq(ca, classOf(b), path);

      assertEq(Object.getPrototypeOf(a),
               ca == "[object Object]" ? Object.prototype : Array.prototype,
               path);

      // 'b', the original object, may have non-enumerable or XMLName
      // properties; ignore them.  'a', the clone, should not have any
      // non-enumerable properties (except .length, if it's an Array) or
      // XMLName properties.
      var pb = ownProperties(b).filter(isCloneable);
      var pa = ownProperties(a);
      for (var i = 0; i < pa.length; i++) {
        assertEq(typeof pa[i][0], "string", "clone should not have E4X properties " + path);
        if (!pa[i][1].enumerable) {
          if (Array.isArray(a) && pa[i][0] == "length") {
            // remove it so that the comparisons below will work
            pa.splice(i, 1);
            i--;
          } else {
            throw new Error("non-enumerable clone property " + uneval(pa[i][0]) + " " + path);
          }
        }
      }

      // Check that, apart from properties whose names are array indexes, 
      // the enumerable properties appear in the same order.
      var aNames = pa.map(function (pair) { return pair[1]; }).filter(notIndex);
      var bNames = pa.map(function (pair) { return pair[1]; }).filter(notIndex);
      assertEq(aNames.join(","), bNames.join(","), path);

      // Check that the lists are the same when including array indexes.
      function byName(a, b) { a = a[0]; b = b[0]; return a < b ? -1 : a === b ? 0 : 1; }
      pa.sort(byName);
      pb.sort(byName);
      assertEq(pa.length, pb.length, "should see the same number of properties " + path);
      for (var i = 0; i < pa.length; i++) {
        var aName = pa[i][0];
        var bName = pb[i][0];
        assertEq(aName, bName, path);

        var path2 = path + "." + aName;
        var da = pa[i][1];
        var db = pb[i][1];
        assertEq(da.configurable, true, path2);
        assertEq(da.writable, true, path2);
        assertEq("value" in da, true, path2);
        var va = da.value;
        var vb = b[pb[i][0]];
        if (typeof va === "object" && va !== null)
          queue.push([va, vb, path2]);
        else
          assertEq(va, vb, path2);
      }
    }

    var banner = "while testing clone of " + (desc || uneval(b));
    var a = deserialize(serialize(b));
    var queue = [[a, b, banner]];
    while (queue.length) {
      var triple = queue.shift();
      assertIsCloneOf(triple[0], triple[1], triple[2]);
    }

    return a; // for further testing
  }
  global.clone_object_check = clone_object_check;

})(this);
