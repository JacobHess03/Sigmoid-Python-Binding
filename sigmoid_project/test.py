import numpy as np
import time
from sigmoid import sigmoid

def sigmoid_py(x):
    return 1 / (1 + np.exp(-x))

x = np.random.randn(1_000_000)

# Python version
start = time.time()
sig_py = sigmoid_py(x)
print("Python time:", time.time() - start)

# C++ version
start = time.time()
sig_cpp = sigmoid(x)
print("C++ time:", time.time() - start)

print("Results close:", np.allclose(sig_py, sig_cpp))
