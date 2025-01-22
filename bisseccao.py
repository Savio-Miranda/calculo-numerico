import numpy as np


def bisseccao(coeficients: list, a: int, b: int, max_iter: int):
    function = np.poly1d(coeficients)
    for i in range(max_iter):
        ponto_medio = (a + b)/2
        result = float(function(a)) * float(function(ponto_medio))
        if result < 0:
            b = ponto_medio
        elif result > 0:
            a = ponto_medio
        else:
            return (a, b)

    return (a, b)

# Exemplo de uso
raiz = bisseccao([3, -4, -2, 1], 1, 2, 1000)
print(f"A raiz encontrada é: {raiz}")
