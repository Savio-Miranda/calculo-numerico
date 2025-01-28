def bissection(a: float, b: float, max_iter: int, error: float, f = lambda x: ...):
    for i in range(max_iter):
        midpoint = (a + b)/2
        check_signal = f(a) * f(midpoint)
        if check_signal < 0:
            b = midpoint
        elif check_signal > 0:
            a = midpoint
        else:
            return midpoint
        
        if abs(f(midpoint)) < error:
            return midpoint

    return midpoint


root = bissection(-4, -2, 1000, 0.0000001, lambda x: (x**4)-(9*x**2)+(3*x)+12)
print(f"A raiz encontrada é: {root}")
root = bissection(-2, 1, 1000, 0.0000001, lambda x: (x**4)-(9*x**2)+(3*x)+12)
print(f"A raiz encontrada é: {root}")
root = bissection(1, 2, 1000, 0.0000001, lambda x: (x**4)-(9*x**2)+(3*x)+12)
print(f"A raiz encontrada é: {root}")
root = bissection(2, 3, 1000, 0.0000001, lambda x: (x**4)-(9*x**2)+(3*x)+12)
print(f"A raiz encontrada é: {root}")
