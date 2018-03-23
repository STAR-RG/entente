from regression_tests import *
import hashlib

def test_ec6():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    #path_name = os.path.join(constants.seeds_dir, 'removeme')
    hashmap = {}
    hits = 0
    numfiles = 0
    numwarnings = 0
    with open('short_diff_report_test_ec6.txt', 'w') as short_file, open('long_diff_report_test_ec6.txt', 'w') as long_file:
        for file_name in os.listdir(path_name):
            res = multicall.callAll(os.path.join(path_name, file_name))
            numfiles += 1
            if res.is_interesting(): # discrepancy if we find diverging responses
                numwarnings += 1
                hashcode = res.hash()
                if hashcode in hashmap:
                    hits += 1
                    tests = hashmap[hashcode]
                else:    
                    hashmap[hashcode] = tests = set()
                tests.add(res)
                long_file.write(str(res))

        # generating log
        short_file.write('number of files: {}\n'.format(numfiles))
        short_file.write('number of warnings: {}\n'.format(numwarnings))
        short_file.write('number of cache hits: {}\n'.format(hits))
        short_file.write('number of buckets: {}\n'.format(len(hashmap)))
        #pylint: disable=W0612
        bucket_num = 0
        for key, val_set in hashmap.items():
            bucket_num += 1
            short_file.write('\n>>>>> files in bucket #{}:\n'.format(bucket_num))
            for res in val_set:
                short_file.write(' ' + res.path_name + "\n" )
            short_file.write('\npattern:\n')
            res = next(iter(val_set))
            short_file.write(res.str_canonical())