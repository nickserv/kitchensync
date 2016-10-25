import glob
import os
import sys


def install_command(file):
    manager = os.path.splitext(os.path.basename(file))[0]
    options = ['--global'] if manager == 'npm' else []
    packages = open(file).read().split()
    return [manager, 'install'] + options + packages


def install_commands(directory):
    files = glob.glob(os.path.join(directory, '*.txt'))
    return map(install_command, files)


def main():
    directory = sys.argv[1] if len(sys.argv) == 2 else 'packages'
    install_command_strings = map(' '.join, install_commands(directory))
    print('\n'.join(install_command_strings))
