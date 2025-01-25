def gauss(A: list, b: list):
    n = len(b) - 1 # b tem tamanho n, mas começamos em 0, logo, len(b) - 1 = n - 1
    for j in range(n):
        for i in range(j+1, n+1):
            m = A[i][j]/A[j][j]
            A[i][j] = 0
            for k in range(j+1, n+1):
                A[i][k] -= m*A[j][k]
            b[i] -= m*b[j]

    print("A:")
    for i in range(len(A)):
        print(A[i])
    
    print("b:")
    print(b)

    return A


def resolucao_sistema(A: list, b: list):
    n = len(b) - 1
    x = []
    for i in range(n + 1):
        x.append(None)
    

    x[n] = b[n]/A[n][n]
    for k in range(n, -1, -1):
        s = 0
        for j in range(k+1, n+1):
            s += A[k][j] * x[j]
            x[k] = (b[k] - s)/A[k][k]
    
    print("x:")
    print(x)
    return x

A = [
    [2, 1, 1, 0],
    [4, 3, 3, 1],
    [8, 7, 9, 5],
    [6, 7, 9, 8]
]

b = [2, 3, 1, -4]


A2 = [
    [0.8, -0.2, -0.2, -0.3],
    [-0.2, 0.9, -0.2, -0.3],
    [-0.3, -0.3, 0.8, -0.2],
    [-0.2, -0.2, -0.4, 0.8]
]

b2 = [0.5, 0.4, 0.3, 0]


gauss(A, b)
resolucao_sistema(A, b)

print(30*"-")

gauss(A2, b2)
resolucao_sistema(A2, b2)