# JSFuzz
### Requirements
- Linux
- Python3.6
- [tox virtualenv](https://tox.readthedocs.io/en/latest/)
- [eslint](https://eslint.org/)

### Installation
1. Clone this repository
2. Download the compressed JS Engines file ([instructions here](https://github.com/damorim/jsfuzz/blob/master/js_engines/README_download_executables)) and extract it in `js_engines` folder
3. Open a terminal window, go to project folder and run: `$> sudo ln -s $(pwd)/js_engines/radamsa /usr/bin/radamsa` to create a simbolic link for `radamsa` binary

### Running
- Open a terminal window, go to project folder and run: `$> tox`
