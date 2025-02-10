def lagrange(X: list, Y: list, x: int):
    result = 0
    n = len(X)
    for k in range(n):
        numerator = 1
        denominator = 1
        for j in range(n):
            if j != k:
                numerator *= x - X[j]
                denominator *=  X[k] - X[j]
    
        Lj = numerator/denominator
        result += Y[k] * Lj
    
    return result

x = 8
f_x = lagrange([1, 2, 3], [0, 1, 4], x)
print(f"função para x = {x}: {(x**2)-(2*x)+1}")
print(f_x)
