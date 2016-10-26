import setuptools

setuptools.setup(
    name='kitchensync',
    version='0.1',
    description='An aggregated package manager for installing packages '
                'globally.',
    long_description=open('README.rst').read(),
    url='https://github.com/nickmccurdy/kitchensync',
    author='Nick McCurdy',
    author_email='thenickperson@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
        'Topic :: System',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities'
    ],
    keywords='installation package management',
    py_modules=['kitchensync'],
    # install_requires=[''],
    extras_require={'test': 'cram'},
    entry_points={'console_scripts': 'kitchen=kitchensync:main'},
    test_suite="tests",
    zip_safe=False
)
