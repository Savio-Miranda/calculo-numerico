import numpy as np

from solucoes_matriciais.fatoracao_lu import resolver_sistema_lu
from ajuste_de_curva.linearizar import ajustar_valores
from ajuste_de_curva.minimos_quadrados_nao_linear import minimos_quadrados_nao_lineares
from plot.plot import plot


### EXEMPLO DE USO ###
def funcao_modelo(x, alpha1, alpha2):
    return alpha2*np.exp(alpha1*x)

def f(x):
    return funcao_modelo(x, coefs[0], coefs[1])


# Dados de entrada
X = np.array([-1, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1])
Y = np.array([36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246])
Y_ajustado = Y.copy()
Y_ajustado = ajustar_valores(Y_ajustado, lambda y: np.log(y))


g_list = [lambda x: np.exp(x), lambda x: 1]

coefs = minimos_quadrados_nao_lineares(X, Y_ajustado, g_list, resolver_sistema_lu)

plot(X, Y, f, -2, 2, "MMQ")
