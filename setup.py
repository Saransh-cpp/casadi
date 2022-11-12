from setuptools import setup, Extension
from glob import glob


example_module = Extension('_casadi',
                           sources=['swig/casadi_wrap.cxx'],
                           depends=['casadi/casadi.hpp'],
                           include_dirs=['./casadi', "./swig"],
                           swig_opts=['-c++', '-python', '-py3'],
)

setup(
   name = 'casadi',
   version = '0.1',
   author      = "SWIG Docs",
   description = """Simple swig example from docs""",
   ext_modules = [example_module],
   py_modules = ["casadi"],
   headers=['casadi/casadi.hpp']
)
