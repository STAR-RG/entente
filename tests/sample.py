import os

pattern = '/home/damorim/projects/jsfuzz/seeds/v8.test.benchmarks.data'
l = [os.path.join(dp, f) for dp, dn, fn in os.walk(pattern) for f in fn if f.endswith(".js")]
