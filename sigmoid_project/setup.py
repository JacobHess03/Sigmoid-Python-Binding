from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension("cpp_sigmoid",
                      ["sigmoid/cpp_sigmoid.cpp"])
]

setup(
    name="cpp_sigmoid",
    version="0.1",
    author="Tuonome",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
