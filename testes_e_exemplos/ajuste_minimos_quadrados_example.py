import numpy as np

from solucoes_matriciais.fatoracao_lu import resolver_sistema_lu
from ajuste_de_curva.linearizar import ajustar_valores
from ajuste_de_curva.minimos_quadrados_nao_linear import minimos_quadrados_nao_lineares
from plot.plot import plot


### EXEMPLO DE USO ###

## Exemplo exponencial ##
def f(x):
    return coefs[1]*np.exp(coefs[0]*x) # função real, sem tirar nem pôr

X = [-1, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1]
Y = [36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246]
Y_ajustado = Y.copy()
Y_ajustado = ajustar_valores(Y_ajustado, lambda y: np.log(y)) # ajuste de valores em Y

g_list = [lambda a: np.exp(a), lambda b: 1] # se a função é b*e^(a*x), então são necessários dois coeficientes

coefs = minimos_quadrados_nao_lineares(X, Y_ajustado, g_list, resolver_sistema_lu)
print(coefs)
plot(X, Y, f, -2,2, "MMQ")

## Exemplo Linear ##
# def f(x):
#     return coefs[0]*x + coefs[1]
#
#
# X = [1, 3, 4]
# Y = [3, 7, 9]
# g_list = [lambda x: x, lambda x: 1]
# coefs = minimos_quadrados_nao_lineares(X, Y, g_list, resolver_sistema_lu)

