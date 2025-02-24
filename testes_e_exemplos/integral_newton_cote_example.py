from integrais.newton_cotes import newton_cotes_integral
from plot.plot_integral import plot_integral


# Dados de entrada
# X = [1.4, 4, 6.5]
# Y = [math.log(x) for x in X]

X = [1, 1.3, 2] # A quantidade de elementos define a quantidade de Lj(x) e por consequência a precisão...
Y = [1/x for x in X]

a, b = 1, 2  # Intervalo de integração


# Cálculo da integral
# integral = newton_cotes_integral(X, Y, a, b)

plot_integral(X, Y, newton_cotes_integral, a, b, "Newton-Cotes")
