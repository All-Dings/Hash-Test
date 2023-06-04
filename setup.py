from distutils.core import setup, Extension
setup(name='Dings_Lib_C', version='1.0',  \
      ext_modules=[Extension('Dings_Lib_C', ['Dings_Lib_C.c'])])
