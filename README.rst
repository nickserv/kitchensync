Kitchen Sync
============
.. image:: https://travis-ci.org/nickmccurdy/kitchensync.svg?branch=master
    :target: https://travis-ci.org/nickmccurdy/kitchensync
An aggregated package manager for installing packages globally.

This is currently a prototype implemented as a Python package for versions 2.7 and 3.5. Mac and Windows should be supported in theory, but they haven't been tested yet.

Concept
-------
Kitchen Sync essentially acts as a proxy for installing lists of packages with different package managers. It is designed for easily installing commonly used software tools and platforms across multiple development machines, and should not be used to install dependencies of specific projects.

Kitchen Sync uses a central configuration of package lists that can be shared across machines to maintain similar installations. You can configure Kitchen Sync by creating a directory of text files, where each file is named after a package manager and contains a list of packages you want installed by it. Kitchen Sync then installs all packages with the appropriate package manager. There will also be tools to "sync" lists of packages that are already installed globally back to these text files. Since these lists are simple text files, they can be used with any existing version control systems or syncing tools.

What Stow and Homesick do for managing config files from centralized locations, Kitchen Sync aims to do for package installation. As a result, these tools should work well together, and you can save your package configs in the same repository as your other config files. This is especially useful if you use text editors, IDEs, or shells that rely on many external commands that need to be installed globally with different package managers.

Goals
-----
- Support multiple package managers out of the box while remaining extensible enough to support more.
- Store all configuration in a single directory of plain text files.
- Should not have too many dependencies, since it may be used to install language runtimes.
- Easy installation on Unix/Linux, with at least basic Windows support.
- Ease development of personal config file repositories by managing their global dependencies.

Testing
-------
1. Make sure you're using a Unix/Linux system with Python and an up to date version of pip installed.
2. ``pip install .[test]``
3. ``cram tests``
