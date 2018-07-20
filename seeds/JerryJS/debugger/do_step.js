// Copyright JS Foundation and other contributors, http://js.foundation
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

function f1()
{
  function g()
  {
    return 6;
  }

  var i = g();
  if (i !== 6) {
  	throw new Error("Test fail")
  }
  g();
}

function f2()
{
  f1();
  return 7;
}

if(f1() !== undefined) {
	throw new Error("Test fail")
}
if(f2() !== 7) {
	throw new Error("Test fail")
}