# encoding: utf-8
"""
@author: lmh
@software: PyCharm
@file: setup.py
@time: 2020/4/14 13:47
"""
from setuptools import setup, find_packages

setup(
    name = "lmhtools",
    version = "0.0.1",
    keywords = ("pip", "lmh","lmhtools",'liumenghua'),
    description = "lmhtools",
    long_description = "lmhtools",
    license = "MIT Licence",

    url = "https://github.com/mengnan254/lmhtools",
    author = "lmh",
    author_email = "297279618@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["PyExecJS==1.5.1","requests==2.23.0"]
)
