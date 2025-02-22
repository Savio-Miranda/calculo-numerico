import numpy as np

from ajuste_de_curva.gauss_newton import gauss_newton
from plot.plot import plot


### EXEMPLO DE USO ###
def funcao_modelo(x, alpha1, alpha2):
    return alpha1 * np.exp(-alpha2 * x)


def f(x):
    return funcao_modelo(x, coefs[0], coefs[1])


# Dados de entrada
X = np.array([-1, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1])
Y = np.array([36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246])

# Chutes iniciais para os coeficientes (α₁, α₂)
chutes_iniciais = [1, 1]

# Resolver o sistema usando o método de Gauss-Newton
coefs = gauss_newton(chutes_iniciais, X, Y, funcao_modelo, max_iter=100)

plot(X, Y, f, -2, 2, "Gauss-Newton")
