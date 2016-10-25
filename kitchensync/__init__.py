import glob
import os
import sys


def command_for_manager(manager):
    install_command = ['install']
    if manager == 'npm':
        install_command = ['install', '--global']
    return [manager] + install_command


def main():
    directory = sys.argv[1] if len(sys.argv) == 2 else 'packages'
    for file in glob.glob(os.path.join(directory, '*.txt')):
        basename = os.path.basename(file)
        manager = os.path.splitext(basename)[0]
        packages = open(file).read().split()
        print(' '.join(command_for_manager(manager) + packages))
