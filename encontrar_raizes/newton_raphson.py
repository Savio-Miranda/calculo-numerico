import math


def newton_raphson(x0: float, max_iter: int, e: float, f = lambda x: ..., derivative = lambda x: ...):
    if abs(f(x0)) < e:
        approx_root = x0

    for i in range(max_iter):
        x1 = x0 - (f(x0)/derivative(x0))
        if abs(f(x1)) < e or abs(x1 - x0) < e:
            approx_root = x1
            return approx_root
        x0 = x1
    
    return approx_root


root = newton_raphson(0.1, 10**15, 0.000000001, lambda x: math.log(x), lambda x0: 1/x0)
print(f"A raiz encontrada é: {root}")
