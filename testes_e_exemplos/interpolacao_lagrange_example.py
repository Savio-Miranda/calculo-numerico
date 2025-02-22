import numpy as np
import matplotlib.pyplot as plt

from interpolacao.lagrange import lagrange
from plot.plot import plot


### EXEMPLO DE USO ###
def f(x):
    return lagrange(X, Y, x)


X = [1, 2, 3]
Y = [0, 1, 4]


plot(X, Y, f, 0, 4, "Lagrange")
