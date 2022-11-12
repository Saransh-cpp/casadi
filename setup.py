from setuptools import setup, Extension
from glob import glob


example_module = Extension('_casadi',
                           sources=['swig/casadi_wrap.cpp', 'swig/casadi_wrap.cxx'],
                           depends=['casadi/casadi.hpp', 'swig/casadi.h'],
                           # include_dirs=[glob('./casadi/*')],
                              # swig_opts=['-c++', '-python', '-py3'],
)

setup(
   name = 'casadi',
   version = '0.1',
   author      = "SWIG Docs",
   description = """Simple swig example from docs""",
   ext_modules = [example_module],
   py_modules = ["casadi"],
   headers=['casadi/core/casadi_interrupt.hpp', 'casadi/casadi.hpp', 'swig/casadi_wrap.h']
)
