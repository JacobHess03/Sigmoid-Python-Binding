Modulo Python ad alte prestazioni per il calcolo della funzione sigmoid, implementato in C++ e integrato in Python tramite pybind11.
# Requisiti

    Python ≥ 3.6

    pybind11 installato (pip install pybind11)

    Un compilatore C++ compatibile con C++17 (MSVC su Windows, g++ su Linux/macOS)

# Struttura del progetto

    sigmoid_project/
    ├── build
    ├── sigmoid/
    │   └── __pycache__
        └── __init__.py
        └── cpp_sigmoid.pyd
        └── cpp_sigmoid.cpp        # Codice C++ con la funzione sigmoid
    │
    ├── cpp_sigmoid.cp310-win_amd64.pyd
    ├── setup.py                   # Script di build Python per pybind11
    ├── test.py                    # Script Python per testare il modulo

# Compilazione

Apri il terminale nella directory del progetto (dove si trova setup.py) e lancia:

    python setup.py build_ext --inplace

Questo genererà un file .pyd (su Windows) o .so (su Linux/macOS) direttamente nella cartella corrente, ad esempio:

    cpp_sigmoid.cp310-win_amd64.pyd

Può anche comparire dentro la cartella sigmoid/ se specificato nel modulo.
# Test

Puoi testare il modulo con lo script test.py:

    test.py
    
    import cpp_sigmoid  # oppure from sigmoid import cpp_sigmoid se è in sottocartella
    import numpy as np

    x = np.array([0.0, 1.0, 2.0])
    y = cpp_sigmoid.sigmoid(x)
    print("Output:", y)

Lancialo con:

    python test.py

Assicurati che il file .pyd sia nella stessa directory di test.py o che il modulo sia correttamente installato nel tuo ambiente.
# Note

    Il nome del modulo deve combaciare con quello definito nel file C++:

    PYBIND11_MODULE(cpp_sigmoid, m)

Se vedi errori su Python.h o pybind11/pybind11.h, verifica che pybind11 sia installato:

    pip install pybind11

Puoi trovare il path degli header con:

    import pybind11
    print(pybind11.get_include())
