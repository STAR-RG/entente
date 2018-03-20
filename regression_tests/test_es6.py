from regression_tests import *

def test_ec6():
    counters = {}
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    with open('diff_report_test_ec6.txt', 'w') as file:
        buffer = []
        for file_name in os.listdir(path_name):
            res = multicall.callAll(os.path.join(path_name, file_name))
            # discrepancy if we find diverging responses
            if res.should_report():
                res.update_counters(counters)
                buffer.append(str(res))           
        file.write('**** summary ****\n')
        file.write(counters)
        file.write("\n")
        file.write(''.join(buffer))
