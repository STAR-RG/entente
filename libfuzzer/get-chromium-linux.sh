set -e -x

WORKSPACE="${PWD}"

# Install depot_tools
if [[ ! -e ./depot_tools ]]; then
    git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git ./depot_tools
    export PATH="$PWD/depot_tools:$PATH"
fi

gclient

echo "Fetching chromium..."
if [[ ! -e ./chromium ]]; then
    mkdir chromium && cd chromium
    fetch --nohooks chromium
    # Run the hooks
    cd src && gclient runhooks
fi

echo "Pull updates..."
cd ${WORKSPACE}/chromium/src
gclient sync

# optional args
# is_asan=true	enables Address Sanitizer to catch problems like buffer overruns.
# is_msan=true	enables Memory Sanitizer to catch problems like uninitialized reads[*].
# is_ubsan_security=true	enables Undefined Behavior Sanitizer to catch[*] undefined behavior like integer overflow.
echo "Activating libfuzzer with AddressSanitizer"
gn gen out/libfuzzer '--args=use_libfuzzer=true is_asan=true is_debug=false enable_nacl=false' --check

# echo "Activating libfuzzer with MemorySanitizer"
# gn gen out/libfuzzer '--args=use_libfuzzer=true is_asan=true is_debug=false enable_nacl=false' --check

# echo "Activating libfuzzer with UndefinedBehaviourSanitizer"
# gn gen out/libfuzzer '--args=use_libfuzzer=true is_asan=true is_debug=false enable_nacl=false' --check
