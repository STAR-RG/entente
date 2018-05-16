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

var uint8 = new Uint8Array(4);

// 22.2.3.22
if(!(uint8.set.length === 1)) throw new Error("Test failed");

try
{
  uint8.set([1], -1);
  if(!(false)) throw new Error("Test failed");
} catch (e)
{
  if(!(e instanceof RangeError)) throw new Error("Test failed");
}

try
{
  uint8.set([1], - (Math.pow(2, 32) + 1));
  if(!(false)) throw new Error("Test failed");
} catch (e)
{
  if(!(e instanceof RangeError)) throw new Error("Test failed");
}

try
{
  uint8.set([1], -Infinity);
  if(!(false)) throw new Error("Test failed");
} catch (e)
{
  if(!(e instanceof RangeError)) throw new Error("Test failed");
}

try
{
  uint8.set([1], Infinity);
  if(!(false)) throw new Error("Test failed");
} catch (e)
{
  if(!(e instanceof RangeError)) throw new Error("Test failed");
}

try
{
  uint8.set([1], (Math.pow(2, 32) + 1));
  if(!(false)) throw new Error("Test failed");
} catch (e)
{
  if(!(e instanceof RangeError)) throw new Error("Test failed");
}

try
{
  // 22.2.3.22.1 step 20
  uint8.set([17, 18, 19], 2);
  if(!(false)) throw new Error("Test failed");
} catch (e)
{
  if(!(e instanceof RangeError)) throw new Error("Test failed");
}
