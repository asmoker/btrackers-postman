#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by asmoker on 04/11/2017.

import os

from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


requires = read('requirements.txt').split('\n')

setup(
    name='btrackers-postman',
    version='1.0.0',
    packages=['btp', 'btp.util'],
    url='https://github.com/asmoker/btrackers-postman',
    license='Apache-2.0',
    author='asmoker',
    author_email='blog.smoker.cc@gmail.com',
    description='BitTorrent Trackers Postman, fetch BitTorrent Trackers URL list from '
                'https://github.com/ngosang/trackerslist and post to your aria2 server via jsonrpc.',
    keywords='BitTorrent Trackers aria2 trackerslist jsonrpc update post postman',
    long_description=read('README'),
    install_requires=requires,
    entry_points={
        'console_scripts': ['btp=btp.run:main'],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
    ]
)
