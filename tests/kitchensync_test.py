import kitchensync
import os
import unittest

PACKAGES_PATH = os.path.join(os.path.dirname(__file__), 'packages')
GEM_LIST_PATH = os.path.join(PACKAGES_PATH, 'gem.txt')


class KitchenSyncTest(unittest.TestCase):
    def test_install_command(self):
        self.assertEqual(kitchensync.install_command(GEM_LIST_PATH),
                         ['gem', 'install', 'bundler', 'rails'])

    def test_install_commands(self):
        self.assertEqual(kitchensync.install_commands(PACKAGES_PATH), [
            ['gem', 'install', 'bundler', 'rails'],
            ['npm', 'install', '--global', 'grunt-cli', 'mocha'],
            ['pacman', '-S', 'python']
        ])

    @unittest.skip('pending')
    def test_main(self):
        pass
