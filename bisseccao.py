import numpy as np


def bissection(coeficients: list, a: int, b: int, max_iter: int):
    function = np.poly1d(coeficients)
    for i in range(max_iter):
        midpoint = (a + b)/2
        chech_signal = float(function(a)) * float(function(midpoint))
        if chech_signal < 0:
            b = midpoint
        elif chech_signal > 0:
            a = midpoint
        else:
            return midpoint

    return midpoint


root = bissection([3, -4, -2, 1], 1, 2, 1000)
print(f"A raiz encontrada é: {root}")
