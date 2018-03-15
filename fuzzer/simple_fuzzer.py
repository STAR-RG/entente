import jsparser
import multicall
import tempfile
import constants
import os

def fuzz_it(filename):
    with open(filename, 'r') as myfile:
        data = myfile.read()
        #ast = jsparser.parse_and_rewrite(data)
        mod_data = data
        with tempfile.NamedTemporaryFile(delete=False) as fp:
            fp.write(mod_data)
            print(fp.name)
            multicall.callAll(fp.name)

if __name__ == "__main__":
    filename = os.path.join(constants.seeds_dir, 'max.js')
    fuzz_it(filename)