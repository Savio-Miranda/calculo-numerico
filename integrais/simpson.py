import math
import numpy as np
import matplotlib.pyplot as plt

from interpolacao.lagrange import lagrange


def newton_cotes_integral(X, Y, a, b, div=100):
    x_divisions = np.linspace(a, b, div)
    h = (b - a) / (div - 1)  # Espaçamento entre os pontos
    integral = 0
    
    for i, x in enumerate(x_divisions):
        weight = 2 if (i != 0 and i != div - 1) else 1  # Peso 1 nos extremos, 2 nos intermediários (Regra dos Trapézios)
        integral += weight * lagrange(X, Y, x)
    
    integral *= h / 3  # Ajuste final para a regra de simpson
    return integral

# Dados de entrada
# X = [1.4, 4, 6.5]
# Y = [math.log(x) for x in X]

X = [1, 1.5, 2]
Y = [1/x for x in X]

a, b = 1, 2  # Intervalo de integração
x_vals = np.linspace(a, b, 100)
y_vals = [lagrange(X, Y, x) for x in x_vals]

# Cálculo da integral
integral = newton_cotes_integral(X, Y, a, b)
# Criando o gráfico
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="Interpolação de Lagrange", color="blue")
plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área sob a curva")
plt.scatter(X, Y, color="red", label="Pontos conhecidos")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title(f"Área sob a curva: {integral} - Interpolação de Lagrange")
plt.legend()
plt.grid()

# Exibir o gráfico
plt.show()
