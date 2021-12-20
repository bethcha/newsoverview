from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='newsoverview',
    version='0.0.3',
    packages=['newsoverview'],
    url='https://github.com/bethcha/newsoverview',
    license='MIT',
    author='Bethan',
    author_email='89695634+bethcha@users.noreply.github.com',
    description='News at a glance',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['pygooglenews', 'deep-translator']
)
