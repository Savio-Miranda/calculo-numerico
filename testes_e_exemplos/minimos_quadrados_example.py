import matplotlib.pyplot as plt
import numpy as np
from solucoes_matriciais.fatoracao_lu import resolver_sistema_lu
from ajuste_de_curva.linearizar import ajustar_valores
from ajuste_de_curva.minimos_quadrados_nao_linear import minimos_quadrados_nao_lineares
from plot.plot import plot

### EXEMPLO DE USO ###

# Dados de entrada
X = np.array([-1, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1])
Y = np.array([36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246])
# X = [1, 2, 3, 4]
# Y = [3, 5, 6, 8]

Y = ajustar_valores(Y, lambda y: np.log(y))
print(Y)

def modelo_exponencial(x, alpha1, alpha2):
    return alpha2*np.exp(alpha1*x)


g_list = [lambda x: x, lambda x: 1]


coefs_ajustados = minimos_quadrados_nao_lineares(X, Y, g_list, resolver_sistema_lu)
print("Coeficientes ajustados:", *coefs_ajustados)

# Gerar valores preditos
X_test = np.linspace(min(X), max(X), 100)
Y_pred = [modelo_exponencial(x, coefs_ajustados[0], np.exp(coefs_ajustados[1])) for x in X_test]

plt.scatter(X, np.exp(Y), color='red', label='Pontos Originais')
plt.plot(X_test, Y_pred, label='Curva Ajustada')
plt.legend()
plt.show()
