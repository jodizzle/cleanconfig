#!/usr/bin/env python


from setuptools import setup, find_packages


setup(
    name='powerconfig',
    version='0.1.0',
    description='Flexible configuration for Python projects.',
    author='David McClure',
    author_email='dclure@mit.edu',
    url='https://github.com/davidmcclure/powerconfig',
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'anyconfig',
        'voluptuous',
        'PyYAML',
    ],
)
