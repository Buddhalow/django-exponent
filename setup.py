#!/usr/bin/env python
# flake8: noqa

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test
import os


here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here,  'README.rst'))
long_description = f.read().strip()
f.close()

setup(
    name='django-exponent',
    version='0.2.8',
    author='Alexander Forselius',
    author_email='alexander.forselius@buddhalow.com',
    url='http://github.com/Buddhalow/django-exponent',
    description='Django app wrapper for exponent-sdk-server',
    packages=find_packages(),
    long_description=long_description,
    keywords='django expo exponent exponent-sdk-server-python exponent-sdk react-native',
    zip_safe=False,
    install_requires=[
        'Django>=1.8.0',
        'django-common-helpers>=0.6.4',
        'exponent-server-sdk-python==0.2.0',
        'django-oauth-toolkit==1.0.0'
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)