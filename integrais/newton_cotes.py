import math
import matplotlib.pyplot as plt
import numpy as np

from interpolacao.lagrange import lagrange


def f(x):
    return lagrange(X, Y, x)

def newton_cotes_integral(X: list, Y: list, a: float, b: float, div: int = 100):
    x_divisions = np.linspace(a, b, div)

    # integral de a até b = h/2(F(a) + F(b)) (Fórmula da área do Trapézio)
    # h = |b - a|
    # F(a) é a base menor
    # F(b) é a base maior

    integral = 0
    h = abs(b - a)
    z_integral = []
    for x in x_divisions:
        integral += lagrange(X, Y, x)
    
    return integral


X = [1.4, 4, 6.5]
Y = [math.log(y) for y in X]
# valor exato: 7.621371
integral = newton_cotes_integral(X, Y, 1, 7, 6)


x_vals = np.linspace(1, 7, 100)
y_vals = [lagrange(X, Y, x) for x in x_vals]

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
