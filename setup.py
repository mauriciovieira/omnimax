from setuptools import setup

setup(
    name='omnimax',
    version='0.0.1',
    author='Max Lincoln',
    author_email='max@devopsy.com',
    packages=['omnimax', 'omnimax.sdk'],
    scripts=['bin/omnimax-cli.py'],
    #url='http://pypi.python.org/pypi/Omnimax/',
    license='LICENSE.txt',
    description='An all-in-one test, documentation/sample code, and kata framework',
    long_description=open('README.md').read(),
    # setup_requires=['nose>=1.0'],
    install_requires=['distribute', 'behave', 'pyyaml', 'Mako'],
    # tests_require=['pyfakefs', 'nose', 'mock']
)
