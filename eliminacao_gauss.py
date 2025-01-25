def gauss_A(A: list, b: list):
    n = len(b) - 1 # b tem tamanho n, mas começamos em 0, logo, len(b) - 1 = n - 1
    for j in range(n):
        for i in range(j+1, n+1):
            m = A[i][j]/A[j][j]
            A[i][j] = 0
            for k in range(j+1, n+1):
                A[i][k] -= m*A[j][k]
                b[i] -= m*b[j]

    return A

def gauss_b(A: list, b: list):
    n = len(b) - 1 # b tem tamanho n, mas começamos em 0, logo, len(b) - 1 = n - 1
    for j in range(n):
        for i in range(j+1, n+1):
            m = A[i][j]/A[j][j]
            b[i] -= m*b[j]
            for k in range(j+1, n+1):
                A[i][k] -= m*A[j][k]

    return b


def resolucao_sistema(A: list, b: list):
    n = len(b) - 1
    x = []
    for i in range(n + 1):
        x.append(None)
    

    x[n] = b[n]/A[n][n]
    for k in range(n, -1, -1):
        s = 0
        for j in range(k+1, n+1):
            print("x: ", x, " -> k: ", k, " -> j: ", j)
            s += A[k][j] * x[j]
            x[k] = (b[k] - s)/A[k][k]
    
    print("\nA: ")
    for i in range(len(A)):
        print(A[i])
    
    print("\nb: ", b)
    print("\nx: ")
    print(x)

teste = [
    [2, 1, 1, 0],
    [4, 3, 3, 1],
    [8, 7, 9, 5],
    [6, 7, 9, 8]
]

teste2 = [
    [2, 1, 1, 0],
    [4, 3, 3, 1],
    [8, 7, 9, 5],
    [6, 7, 9, 8]
]


teste3 = [
    [0.8, -0.2, -0.2, -0.3],
    [-0.2, 0.9, -0.2, -0.3],
    [-0.3, -0.3, 0.8, -0.2],
    [-0.2, -0.2, -0.4, 0.8]
]

teste4 = [
    [0.8, -0.2, -0.2, -0.3],
    [-0.2, 0.9, -0.2, -0.3],
    [-0.3, -0.3, 0.8, -0.2],
    [-0.2, -0.2, -0.4, 0.8]
]

vetor_coluna3 = [0.5, 0.4, 0.3, 0]
vetor_coluna4 = [0.5, 0.4, 0.3, 0]





vetor_coluna = [2, 3, 1, -4]
vetor_coluna2 = [2, 3, 1, -4]

# gauss_A(teste, vetor_coluna)
# gauss_b(teste2, vetor_coluna2)

# resolucao_sistema(teste, vetor_coluna2)

gauss_A(teste3, vetor_coluna3)
gauss_b(teste4, vetor_coluna4)
resolucao_sistema(teste3, vetor_coluna4)