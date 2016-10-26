import glob
import os
import sys


def install_command(path):
    manager = os.path.splitext(os.path.basename(path))[0]
    options = ['--global'] if manager == 'npm' else []
    with open(path) as f:
        packages = f.read().split()
    return [manager, 'install'] + options + packages


def install_commands(directory):
    paths = glob.glob('{}/*.txt'.format(directory))
    return list(map(install_command, paths))


def main():
    directory = sys.argv[1] if len(sys.argv) == 2 else 'packages'
    install_command_strings = map(' '.join, install_commands(directory))
    print('\n'.join(install_command_strings))
