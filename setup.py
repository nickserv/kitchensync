import setuptools

setuptools.setup(
    name='kitchensync',
    packages=['kitchensync'],
    extras_require={'test': 'cram'},
    entry_points={'console_scripts': 'kitchen=kitchensync:main'}
)
