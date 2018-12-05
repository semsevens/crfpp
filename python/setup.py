#!/usr/bin/env python

from distutils.core import setup,Extension,os
from os.path import expanduser
import string
import platform

IS_MAC = 'Darwin' in platform.platform()
HOME = expanduser("~")
CRF_PATH = HOME + '/local/CRF++'
INCLUDE_PATH = CRF_PATH + '/include'
LIB_PATH = CRF_PATH + '/lib'

extra_compile_args = []
extra_link_args=[]
if IS_MAC:
    extra_compile_args.append('-mmacosx-version-min=10.9')
    extra_link_args.append('-stdlib=libc++')

setup(name = "mecab-python",
      py_modules=["CRFPP"],
      ext_modules = [Extension("_CRFPP",
                               ["CRFPP_wrap.cxx",],
                               include_dirs = [INCLUDE_PATH],
                               library_dirs = [LIB_PATH],
                               extra_compile_args = extra_compile_args,
                               extra_link_args = extra_link_args,
                               libraries=["crfpp", "pthread"])
                     ])
