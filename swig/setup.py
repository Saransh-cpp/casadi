from setuptools import setup, Extension


example_module = Extension('_casadi',
                           sources=['casadi_wrap.cxx'],
                           # include_dirs=['../casadi']
                           )

setup (name = 'casadi',
       version = '0.1',
       author      = "Casadi",
       description = """Casadi""",
       ext_modules = [example_module],
       py_modules = ["casadi"],
       headers=['../casadi/core/casadi_interrupt.hpp', '../casadi/casadi.hpp', '../casadi/casadi_c.h']
       )
