# -*- coding: utf-8 -*-

import os
from setuptools import setup
from setuptools import find_packages

version = '0.2.4'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'deform_bootstrap', 'test_deform_bootstrap.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.deform_bootstrap',
    version=version,
    description="Fanstatic packaging of test_deform_bootstrap",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/disko/js.deform_bootstrap',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=[
        'deform_bootstrap',
        'js.bootstrap',
        'js.chosen',
        'js.deform',
        'fanstatic',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'deform_bootstrap = js.deform_bootstrap:library',
            ],
        },
    )
