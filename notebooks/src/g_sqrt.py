import numpy as np

def g_sqrt(x, a, h, k):
    x = np.abs(x-h)
    return a*np.sqrt(x)+k
