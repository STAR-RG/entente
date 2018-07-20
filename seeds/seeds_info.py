import os, glob

def scanfolder(root_path, _format='*.js'):
    ignore_files = ['assert.js', 'shell.js', 'utils.js', 'run.js']
    total = []
    for path, dirs, files in os.walk(root_path):
        for d in dirs:
            for f in glob.iglob(os.path.join(path, d, _format)):
                if os.path.basename(f) not in ignore_files:
                    total.append(f)
    return total

pwd = os.path.dirname(os.path.realpath(__file__))

v8_path = os.path.join(pwd, 'v8')
mozilla_path = os.path.join(pwd, 'mozilla')
test262_path = os.path.join(pwd, 'test262')
jsi_path = os.path.join(pwd, 'JSI')
jerryjs_path = os.path.join(pwd, 'JerryJS')
tinyjs_path = os.path.join(pwd, 'TinyJS')
webkitjs_path = os.path.join(pwd, 'WebKit')
duktape_path = os.path.join(pwd, 'DukTape')

tests_test262 = scanfolder(test262_path)
tests_mozilla = scanfolder(mozilla_path)
tests_jerryjs = scanfolder(jerryjs_path)
tests_webkit = scanfolder(webkitjs_path)
tests_duktape = scanfolder(duktape_path)
tests_jsi = scanfolder(jsi_path)
tests_v8 = scanfolder(v8_path)
tests_tinyjs = scanfolder(tinyjs_path)

total = len(tests_v8 + tests_mozilla + tests_test262 + tests_jsi + tests_jerryjs + tests_tinyjs + tests_webkit + tests_duktape)

with open('README.md', 'w') as doc:
    doc.write('# SEED INFO\n')
    doc.write('## Number of seeds: {}\n'.format(total))
    doc.write('## Test262: {}\n'.format(len(tests_test262)))
    doc.write('## Mozilla: {}\n'.format(len(tests_mozilla)))
    doc.write('## JerryJS: {}\n'.format(len(tests_jerryjs)))
    doc.write('## WebKit: {}\n'.format(len(tests_webkit)))
    doc.write('## Duktape: {}\n'.format(len(tests_duktape)))
    doc.write('## JSI: {}\n'.format(len(tests_jsi)))
    doc.write('## V8: {}\n'.format(len(tests_v8)))
    doc.write('## TinyJS: {}\n'.format(len(tests_tinyjs)))
