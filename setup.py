from setuptools import setup, Extension


example_module = Extension('_casadi',
                           sources=['swig/casadi_wrap.cxx'], include_dirs=['./casadi/*']
                           )

setup (name = 'casadi',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [example_module],
       py_modules = ["casadi"],
    #    headers=['casadi/core/casadi_interrupt.hpp', 'casadi/casadi.hpp']
       )