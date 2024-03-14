import numpy as np

def loss_func(y_true, y_pred):
    return np.mean(np.power(y_true-y_pred, 2))

def loss_func_derivative(y_true, y_pred):
    return 2*(y_pred-y_true)/y_true.size