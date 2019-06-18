# Instructions on how to use the differential testing infrastructure

### Requirements
- Linux
- Python3.6
- [tox virtualenv](https://tox.readthedocs.io/en/latest/)
- ECMAScript host [eshost](https://github.com/bterlson/eshost-cli)
- JavaScript (engine) Version Updater [jsvu](https://github.com/GoogleChromeLabs/jsvu)

### Installation
1. Clone this repository
2. Download the compressed JS Engines file ([instructions here](https://github.com/damorim/jsfuzz/blob/master/js_engines/README_download_executables)) and extract it in `js_engines` folder
3. Extract quickfuzz.zip in `js_engines` folder
4. Open a terminal window, go to project folder and run these steps to create a simbolic link for radamsa and quickfuzz:
   1. $> sudo ln -s $(pwd)/js_engines/radamsa /usr/bin/radamsa
   2. $> sudo ln -s $(pwd)/js_engines/QuickFuzz /usr/bin/quickfuzz

### Running
- Open a terminal window, go to project folder and run: `$> tox`

### Docker
1. Download and extract the js engines (see js_engines/README files)
2. Build the image (`docker build -t jsfuzz .`)
3. Run the container (`docker run -t --rm -v /path/to/jsfuzz/repo:/jsfuzz jsfuzz`
4. See the output + logs
