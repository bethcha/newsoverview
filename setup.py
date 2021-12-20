from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='newsoverview',
    version='0.2',
    packages=['newsoverview'],
    url='https://github.com/bethcha/newsoverview',
    license='MIT',
    author='Bethan',
    author_email='89695634+bethcha@users.noreply.github.com',
    description='News at a glance',
    long_description=long_description,
    install_requires=['pygooglenews', 'deep-translator']
)
