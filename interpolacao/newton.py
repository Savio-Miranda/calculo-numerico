def newton_coeficients(X: list, Y: list):
    n = len(X)
    coef = Y.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (X[i] - X[i - j])

    return coef



def newton(x: int, R: list, X: list):
    n = len(R)
    print("RESULTADO COMPLETO: ", R)
    result = R[0]
    coef = 1
    for i in range(1, n):
        coef *= x - X[i-1]
        result += R[i] * coef
    return result


X = [-2, 0, 1]
Y = [2, 1, 3]
# X = [-1, 0, 2]
# Y = [4, 1, -1]

R = newton_coeficients(X, Y)
print("Coeficients: ", R)
result = newton(1, R, X)
print("-> ", result)
