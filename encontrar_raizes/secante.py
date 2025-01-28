import math


def secante(x0: float, x1: float, max_iter: int, e: float, f = lambda x: ..., derivative = lambda x: ...):
    if abs(f(x0)) < e:
        approx_root = x0
        return approx_root

    if abs(f(x1)) < e or abs(x1 - x0) < e:
        approx_root = x1
        return approx_root

    for i in range(max_iter):
        x2 = x1 - (f(x1)/(f(x1)-f(x0)))*(x1 - x0)
        if x2 < 0:
            print(x2)

        if abs(f(x2)) < e or abs(x2 - x1) < e:
            approx_root = x2
            return approx_root
        
        x0 = x1
        x1 = x2

    return approx_root


root = secante(1, 4, 10**15, 0.000000001, lambda x: 3*math.log(x) - 1, lambda x0: (3/x0))
print(f"A raiz encontrada é: {root}")
