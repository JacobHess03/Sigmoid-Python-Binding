High-performance Python module for calculating the sigmoid function, implemented in C++ and integrated into Python via pybind11.
# Requirements

    Python ≥ 3.6
    pybind11 installed (pip install pybind11)
    A C++17 compatible compiler (MSVC on Windows, g++ on Linux/macOS)

# Project Structure

    sigmoid_project/
    ├── build/
    ├── sigmoid/
    │   ├── __pycache__/
    │   ├── __init__.py
    │   └── cpp_sigmoid.pyd   # Compiled C++ module (Windows)
    │   └── cpp_sigmoid.cpp   # C++ code with the sigmoid function
    ├── cpp_sigmoid.cp310-win_amd64.pyd  # Example of compiled module outside `sigmoid/`
    ├── setup.py              # Python build script for pybind11
    └── test.py               # Python script to test the module

# Compilation

Open your terminal in the project directory (where setup.py is located) and run:

    Bash

    python setup.py build_ext --inplace

This will generate a .pyd file (on Windows) or .so file (on Linux/macOS) directly in the current folder, for example:

    cpp_sigmoid.cp310-win_amd64.pyd

It might also appear inside the sigmoid/ folder if specified in the module.
Testing

You can test the module with the test.py script:
Python

    import cpp_sigmoid  # or from sigmoid import cpp_sigmoid if in a subfolder
    import numpy as np
    
    x = np.array([0.0, 1.0, 2.0])
    y = cpp_sigmoid.sigmoid(x)
    print("Output:", y)

Run it with:

    Bash

    python test.py

Ensure the .pyd file is in the same directory as test.py or that the module is correctly installed in your environment.
Notes

    The module name must match the one defined in the C++ file:
    C++

    PYBIND11_MODULE(cpp_sigmoid, m)

If you see errors related to Python.h or pybind11/pybind11.h, verify that pybind11 is installed:

    Bash
    
    pip install pybind11

You can find the header path with:
Python

    import pybind11
    print(pybind11.get_include())

# Results

    Python time: 0.017642736434936523
    C++ time: 0.00238037109375
    Results close: True

*Author: Giacomo Visciotti*

