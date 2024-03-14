import numpy as np

def tg(x):
    return np.tanh(x)

def tg_derivative(x):
    return 1-np.tanh(x)**2