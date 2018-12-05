#!/usr/bin/env python

from distutils.core import setup,Extension,os
from os.path import expanduser
import string
HOME = expanduser("~")
CRF_PATH = HOME + '/local/CRF++'
INCLUDE_PATH = CRF_PATH + '/include'
LIB_PATH = CRF_PATH + '/lib'
setup(name = "mecab-python",
      py_modules=["CRFPP"],
      ext_modules = [Extension("_CRFPP",
                               ["CRFPP_wrap.cxx",],
                               include_dirs = [INCLUDE_PATH],
                               library_dirs = [LIB_PATH],
                               extra_compile_args=['-mmacosx-version-min=10.9'],
                               extra_link_args=['-stdlib=libc++'],
                               libraries=["crfpp", "pthread"])
                     ])
