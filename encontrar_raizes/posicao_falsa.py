import math
from achar_raiz import hunt_root


def regula_falsi(a: float, b: float, e: float, max_iter: int, f = lambda x: ...):
    f0 = f(a)
    f1 = f(b)

    # Verificar se os palpites iniciais são válidos
    if f0 * f1 > 0:
        print("Palpites iniciais incorretos. As raízes não estão contidas no intervalo fornecido.")
        return None

    x = 0

    for _ in range(max_iter):
        # Calculando x2 usando o método da posição falsa
        x = a - (a - b) * f0 / (f0 - f1)
        f2 = f(x)

        # Verificar se a precisão foi alcançada
        if abs(f2) <= e:
            break

        # Atualizar os intervalos
        if f0 * f2 < 0:
            b = x
            f1 = f2
        else:
            a = x
            f0 = f2

    return x


f = lambda x: (x**math.log(x)) + x**2 + x**3 * math.sin(x)
intervalos = hunt_root(f, 1, 20)

for a, b in intervalos:
    raiz = regula_falsi(a, b, 0.00001, 1000, f)
    print(f"A raiz encontrada no intervalo [{a},{b}] é: {raiz}")