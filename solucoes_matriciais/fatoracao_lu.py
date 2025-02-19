from eliminacao_gauss import gauss


def print_matriz(Matriz: list, comentario: str):
    print(comentario)
    for i in range(len(Matriz)):
        print(Matriz[i])


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
            raise "A MATRIZ É SINGULAR"
        
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


def resolucao_Pb(p: list, b: list):
    n = len(p)
    Pb = []
    for i in range(n):
        line = 0
        for j in range(n):
            line += p[i][j] * b[j]
        Pb.append(line)
    
    return Pb

def resolucao_y(Lower, Pb):
    n = len(Lower)
    y = [0] * n
    for i in range(n):
        line = Pb[i]
        for j in range(i):
            line -= Lower[i][j] * y[j]
        y[i] = line
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

# A = [[2, 1, 1, 0],[4, 3, 3, 1],[8, 7, 9, 5], [6, 7, 9, 8]]
# b = [1, 2, 4, 5]

A = [[3, -4, 1],[1, 2, 2],[4, 0, -3]]
b = [9, 3, -2]

A, p = lu(A)
print_matriz(A, "A:")
print_matriz(p, "p:")
Upper, Lower = divide_matriz(A)
print_matriz(Upper, "Upper:")
print_matriz(Lower, "Lower:")
Pb = resolucao_Pb(p, b)
print("Pxb: ", Pb)
y = resolucao_y(Lower, Pb)
print("y: ", y)
x = gauss(Upper, y) # corrigir o gauss para LU... Ante era resolução de sistema
print("x: ", x)
