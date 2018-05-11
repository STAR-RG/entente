/* Copyright JS Foundation and other contributors, http://js.foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

var a = Promise.resolve('a');
var b = Promise.resolve('b');
var c = Promise.reject('c');

Promise.all([a, b, 1]).then(function(x)
{
  if(! (x[0] === 'a')) throw new Error("Test failed");
  if(! (x[1] === 'b')) throw new Error("Test failed");
  if(! (x[2] === 1)) throw new Error("Test failed");
}, function(x)
{
  if(! (false)) throw new Error("Test failed"); // should not run here.
});

Promise.all([a, b, c, 1]).then(function(x)
{
  if(! (false)) throw new Error("Test failed"); // should not run here.
}, function(x)
{
  if(! (x === 'c')) throw new Error("Test failed");
});

Promise.all([]).then(function(x)
{
  if(! (x.length === 0)) throw new Error("Test failed");
}, function(x)
{
  if(! (false)) throw new Error("Test failed"); // should not run here.
});

Promise.all(a).then(function(x)
{
  if(! (false)) throw new Error("Test failed"); // should not run here.
}, function(x)
{
  if(!(x.name === "TypeError")) throw new Error("Test failed");
});
