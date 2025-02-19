import math
import numpy as np
from ajuste_de_curva.minimos_quadrados_nao_linear import minimos_quadrados_nao_lineares
from solucoes_matriciais.eliminacao_gauss import gauss
from ajuste_de_curva.plot import plot

euler = np.exp(1)
sin = lambda x: math.sin(x)
cos = lambda x: math.cos(x)
ln = lambda x: math.log(x)
log = lambda x, b: math.log(x, b)

A = []
b = []
f = lambda x: ...
derivative = lambda x: ...


# Lista de funções base para um ajuste quadrático (y = a + bx + cx²)
list_of_g_functions = [lambda x: 1,
                       lambda x: x,
                       lambda x: x**2,
                       lambda x: math.exp(0.1 * x)]

def f(x):
    return coefs[0] + coefs[1] * x + coefs[2] * (x**2) + coefs[3] * np.exp(0.1 * x)

# Listas de valores de x e y
X = [-5, -3, -1, 0, 1, 3, 5]
Y = [0.5130, 0.9780, 2.4933, 6, 10.5532, 22.7546, 44.2080]


coefs = minimos_quadrados_nao_lineares(X, Y, list_of_g_functions, gauss)
plot(coefs, X, Y, f)
