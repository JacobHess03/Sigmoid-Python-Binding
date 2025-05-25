#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <cmath>

namespace py = pybind11;

py::array_t<double> sigmoid_numpy(py::array_t<double> input) {
    auto buf = input.request();
    auto ptr = static_cast<double *>(buf.ptr);
    size_t n = buf.size;
    

    py::array_t<double> result(buf.size);
    auto r = result.mutable_unchecked<1>();

    for (size_t i = 0; i < n; i++) {
        r(i) = 1.0 / (1.0 + std::exp(-ptr[i]));
    }

    return result;
}

PYBIND11_MODULE(cpp_sigmoid, m) {
    m.def("sigmoid", &sigmoid_numpy, "Sigmoid function in C++");
}
