# USAR INTERPOLAÇÃO SOMENTE PARA VALORES DENTRO DO INTERVALO DE X

def lagrange(X: list, Y: list, x: int):
    result = 0
    n = len(X)
    coefs = []
    for k in range(n):
        numerator = 1
        denominator = 1
        for j in range(n):
            if j != k:
                numerator *= x - X[j]
                denominator *=  X[k] - X[j]
    
        Lj = numerator/denominator
        coefs.append(Lj)
        result += Y[k] * Lj
    
    # print(f"coefs: {coefs}, len: {len(coefs)}")
    return result

# X = [1, 3, 4]
# Y = [2, 4, 3]

# lagrange(X, Y, 4)

