# USAR INTERPOLAÇÃO SOMENTE PARA VALORES DENTRO DO INTERVALO DE X

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
