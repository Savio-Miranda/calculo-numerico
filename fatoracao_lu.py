from eliminacao_gauss import resolucao_sistema


def identity(N):
    I = [None] * N
    for j in range(N):
        I[j] = [None] * N
        for k in range(N):
            I[j][k] = 0
        I[j][j] = 1

    return I;

def lu(A: list):
    n = len(A)
    p = identity(n)

    for k in range(n):
        pivot = abs(A[k][k])
        r = k
        
        for i in range(k+1, n):
            if abs(A[i][k]) > pivot:
                pivot = abs(A[i][k])
                r = i
        
        if pivot == 0:
            print("A MATRIZ É SINGULAR")
            return
        
        if r != k:
            aux = p[k]
            p[k] = p[r]
            p[r] = aux
            for j in range(n):
                aux = A[k][j]
                A[k][j] = A[r][j]
                A[r][j] = aux

        for i in range(k+1, n):
            m = A[i][k]/A[k][k]
            A[i][k] = m
            for j in range(k+1, n):
                A[i][j] -= m*A[k][j]

    return A, p


def resolucao_Ly(p: list, b: list):
    n = len(p)
    Pb = []
    for i in range(n):
        line = 0
        for j in range(n):
            line += p[i][j] * b[j]
        Pb.append(line)
    
    return Pb

def resolucao_y(Ly: list, Pb: list):
    n = len(Ly)
    y = [None] * n
    variables = [1] * n
    for i in range(n):
        line = 0
        for j in range(n):
            if i != j:
                line += Ly[i][j]*variables[j]
        if line < 0:
            line = abs(line) + Pb[i]
        else:
            line += Pb[i]

        # line += Pb[i] # -2
        variables[i] = line # [-2]
        y[i] = line # -2

    return y


def divide_matriz(A: list):
    n = len(A)
    Upper = A
    Lower = identity(n)
    for i in range(n):
        for j in range(n):
            if i > j:
                Lower[i][j] = A[i][j]
                Upper[i][j] = 0
    
    return Upper, Lower

A = [[3, -4, 1],[1, 2, 2],[4, 0, -3]]
b = [9, 3, -2]

A, p = lu(A)
Upper, Lower = divide_matriz(A)


print(15*"-")

Pb = resolucao_Ly(p, b)
print("Pxb: ", Pb)
y = resolucao_y(Lower, Pb)
print("y: ", y)
x = resolucao_sistema(Upper, y)
print("x: ", x)
