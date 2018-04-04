import utils.constants as constants
import subprocess


def run_linter(file_path):
    result = None
    try:
        subprocess.check_output(["eslint", "-c", constants.eslint_config, file_path])
    except subprocess.CalledProcessError as e:
        result = e.output
    return result
