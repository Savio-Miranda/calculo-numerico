import numpy as np


def posicao_falsa(coeficients: list, a: float, b: float, max_iter: int):
    function = np.poly1d(coeficients)
    for i in range(max_iter):
        f_a = float(function(a))
        f_b = float(function(b))
        if f_a * f_b < 0:
            approx_root = a - ((a-b) * f_a)/(f_a - f_b)
            if approx_root == 0:
                return approx_root
            elif f_a * approx_root < 0:
                a = approx_root
            elif f_a * approx_root > 0:
                b = approx_root

    return approx_root


raiz = posicao_falsa([3, -4, -2, 1], 1, 2, 10000)
print(f"A raiz encontrada é: {raiz}")
