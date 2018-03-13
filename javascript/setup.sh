#!/bin/bash

## type 'source setup' on the command line to expose the command names
## for the following javascript engines

## change this directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
JS_DIR=${SCRIPT_DIR}/../javascript

RHINO_PATH="${JS_DIR}/rhino/buildGradle/libs/rhino-1.7.9-SNAPSHOT.jar"
JAVA_SCRIPT_CORE_PATH="${JS_DIR}/WebKit/WebKitBuild/Release/bin"
CHAKRA_PATH="${JS_DIR}/ChakraCore/out/Release"
SPIDER_MONKEY="${JS_DIR}/gecko-dev/js/src/build_OPT.OBJ/dist/bin"
V8="${JS_DIR}/v8/out.gn/x64.release/"

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${JAVA_SCRIPT_CORE_PATH}/../lib

alias rhino='function _rhino(){ java -jar ${RHINO_PATH} $1 ; }; _rhino'
alias jscore='function _jscore(){ ${JAVA_SCRIPT_CORE_PATH}/jsc $1 ; }; _jscore'
alias chakra='function _chaKra(){ ${CHACRA_PATH}/ch $1 ; }; _chakra'
alias smonkey='function _spidermonkey(){ ${SPIDER_MONKEY}/js $1 ; }; _spidermonkey'
alias v8='function _v8(){ ${V8}/d8 $1 ; }; _v8'
