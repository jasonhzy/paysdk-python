# -*- utf-8 -*-
"""
    setup script.
    :created by jasonhu on 2018/07/04.
    :copyright (c) 2018 Jason Hu.
    :license: MIT, see LICENSE for more details.
"""
from setuptools import setup
# from distutils.core import setup

setup(
    name='paysdk',
    keywords=['paysdk', 'python'],
    description="paysdk, make payment simpler",
    long_description=open('paysdk/readme').read(),
    version='1.0.6',
    author='jasonhzy',
    author_email='jasonhzy@yeah.net',
    url='https://jasonhzy.github.io',
    download_url='https://github.com/jasonhzy/paysdk-python',
    license='MIT License',
    install_requires=['flask'],
    zip_safe=False,
    platforms='2.7, 3.4, 3.5, 3.6',
    classifiers=[
        # "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        'Topic :: Software Development :: Libraries'
    ]
)
