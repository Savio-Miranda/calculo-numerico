# PODE-SE USAR PARA ALÉM DO INTERVALO DE X
import math


def get_a(X: list, Y: list):
    n = len(X)
    x_quadratic = 0
    xy = 0
    x = 0
    y = 0
    for i in range(n):
        x_quadratic += X[i]**2
        xy += X[i]*Y[i]
        x += X[i]
        y += Y[i]
    
    numerator = (n*xy) - (x * y)
    denominator = (n*x_quadratic) - (x**2)
    result = numerator/denominator
    return result


def get_b(X: list, Y: list):
    n = len(X)
    x_quadratic = 0
    xy = 0
    x = 0
    y = 0
    for i in range(n):
        x_quadratic += X[i]**2
        xy += X[i]*Y[i]
        x += X[i]
        y += Y[i]
    
    numerator = (x * xy) - (y * x_quadratic)
    denominator = (x**2) - (n*x_quadratic)
    result = numerator/denominator
    return result


def minimos_quadrados_linear(X: list, Y: list, x):
    """
    É possível que os valores de a e b precisam mudar quando em situação de exponencial.
    Isto é identificado conforme a questão.
    """
    a = get_a(X, Y)
    b = get_b(X, Y) # Por exemplo, talvez tenhamos que fazer ln(b) para conseguir seu valor real
    print(f"a: {a}, b: {b}")
    result = a*x + b
    return result


def ajustar_curva(X: list, f):
    n = len(X)
    new_values_of_x = []
    for i in range(n):
        new_values_of_x.append(f(X[i]))
    
    return new_values_of_x


X = [1, 2, 3, 4]
Y = [3, 5, 6, 8]
f = lambda x: math.log(x) # logaritmico, exemplo: y = a*ln(x) + b
g = lambda y: math.log(y) # exponencial, exemplo y = b*e^(ax)
h = lambda y: math.log(y) # potẽncia, exemplo: y = b*x^a

X = ajustar_curva(X, f)
Y = ajustar_curva(Y, g)

result = minimos_quadrados_linear(X, Y, 1)
print(result)
