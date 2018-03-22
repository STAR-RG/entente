from regression_tests import *
import hashlib

def test_ec6():
    counters = {}
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    #path_name = os.path.join(constants.seeds_dir, 'removeme')
    hashmap = {}
    hits = 0
    numfiles = 0
    numwarnings = 0
    with open('diff_report_test_ec6.txt', 'w') as file:
        for file_name in os.listdir(path_name):
            res = multicall.callAll(os.path.join(path_name, file_name))
            numfiles += 1
            if res.is_locally_interesting(): # discrepancy if we find diverging responses
                numwarnings += 1
                hashcode = res.hash()
                if hashcode in hashmap:
                    hits += 1
                    tests = hashmap[hashcode]
                else:    
                    hashmap[hashcode] = tests = set()
                tests.add(res)
                res.update_counters(counters)

        # generating log
        file.write('number of files: {}\n'.format(numfiles))
        file.write('number of warnings: {}\n'.format(numwarnings))
        file.write('number of cache hits: {}\n'.format(hits))
        file.write('number of buckets: {}\n'.format(len(hashmap)))
        #pylint: disable=W0612
        bucket_num = 0
        for key, val_set in hashmap.items():
            bucket_num += 1
            file.write('\n>>>>> files in bucket #{}:\n'.format(bucket_num))
            for res in val_set:
                file.write(' ' + res.path_name + "\n" )
            file.write('\npattern:\n')
            res = next(iter(val_set))
            file.write(res.str_canonical())