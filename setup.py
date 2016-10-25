import setuptools

setuptools.setup(
    name='kitchensync',
    packages=['kitchensync'],
    entry_points={'console_scripts': 'kitchen=kitchensync:main'}
)
