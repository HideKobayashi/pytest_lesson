# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tasks',
    version='0.1.0',
    description='Sample package for learning pytest',
    long_description=readme,
    author='Hideyuki KOBAYASHI',
    author_email='kobayashi.hideyuki@leadinge.co.jp',
    url='https://github.com/HideKobayashi/pytest_lesson',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

