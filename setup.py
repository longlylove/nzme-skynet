# coding=utf-8
"""
Setup package to install Skynet - NZME Test Automation Library dependencies
"""

import os
import codecs
import re

from setuptools import setup, find_packages

def readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='nzme-skynet',
    version=find_version('nzme_skynet/__init__.py'),
    author='Milind Thakur',
    author_email='milind.thakur@nzme.co.nz',
    maintainer='milind.thakur@nzme.co.nz',
    url='https://bitbucket.org/grabone/Skynet.git',
    description="NZME Test Automation Library",
    license='',
    long_description=readme('README.md'),

    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    test_suite='nzme_skynet.test',
    install_requires=[
        'behave>=1.2.5',
        'pytest>=2.9.2',
        'pytest-xdist>=1.14',
        'requests>=2.10.0',
        'sauceclient>=0.2.1',
        'selenium==2.53.6',
        'chromedriver_installer>=0.0.4'
    ],
    classifiers=[
        "Development Status :: ",
        "Environment :: Web Environment",
        "Intended Audience :: Developers, Testers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Framework :: Selenium"
    ],
    zip_safe=True
)