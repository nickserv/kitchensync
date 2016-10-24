# Kitchen Sync
[![Build Status](https://travis-ci.org/nickmccurdy/kitchensync.svg?branch=master)](https://travis-ci.org/nickmccurdy/kitchensync)

An aggregated package manager for installing packages globally.

This is currently a prototype implemented as a bash script. I might port it to another scripting language for better Windows support.

## Concept
Kitchen Sync makes it easier to install globally used packages from a cental configuration that you can sync between machines. What Stow or Homesick does for managing dotfiles, Kitchen Sync aims to do for package installation. You can configure it by creating a directory of text files, where each file is named after a package manager and contains a list of packages you want installed by it. Kitchen Sync then installs all packages with the appropriate package manager. There will also be tools to "sync" lists of packages that are already installed globally back to these text files.

Note that this tool is designed for setting up user software and development tools, and not for installing the dependencies of specific projects. Kitchen Sync should work nicely with config managers like Stow and Homesick.

## Testing
1. Make sure you're using a Unix/Linux system with Python installed.
2. `pip install -r requirements.txt`
3. `cram kitchen.t`
