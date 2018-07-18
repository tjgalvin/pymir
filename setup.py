from setuptools import setup, find_packages

setup(
    name='pymir',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Simple class to run Miriad tasks',
    long_description=open('README.md').read(),
    url='https://github.com/tjgalvin/pymir',
    author='Tim Galvin',
    author_email='fake@fake.com'
)
