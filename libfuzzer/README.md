## FAQ LibFuzzer + Chromium (V8)

### Installation
[Follow the Linux build instructions page](https://chromium.googlesource.com/chromium/src/+/master/docs/linux_build_instructions.md#Install)

### How to use LibFuzzer in Chromium

The steps can be found on [Getting Started with libFuzzer in Chromium](https://chromium.googlesource.com/chromium/src/+/master/testing/libfuzzer/getting_started.md)

In overall, we need to follow these steps:
1. Choose a file (3rd party, src/* or something else) to fuzzing test
2. Write a fuzz target in the same directory of the file choosen
```
// my_fuzzer.cc
#include <stddef.h>
#include <stdint.h>
extern "C" int LLVMFuzzerTestOneInput(const uint8_t* data, size_t size) {
  // put your fuzzing code here and use data+size as input.
  return 0;
}
```
3. Define the test in BUILD.gn:
```
import("//testing/libfuzzer/fuzzer_test.gni")
fuzzer_test("my_fuzzer") {
  sources = [ "my_fuzzer.cc" ]
  deps = [ ... ]
}
```
3. Build using ninja and run it:
```
$> ninja -C out/libfuzzer my_fuzz
./out/libfuzzer/my_fuzz
```
