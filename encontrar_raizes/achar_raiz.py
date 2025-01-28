import math
import numpy as np


# Função para verificar intervalos que podem conter raízes (pelo método da mudança de sinal)
def hunt_root(f = lambda x: ..., menor_x: int = -10, maior_x: int = 10):
    # Cria um objeto de polinômio usando o vetor de coeficientes fornecido
    intervalos = []
    c = 0  # Contador de raízes encontradas
    
    # Itera sobre os inteiros dentro do intervalo [a, b]
    for x in range(menor_x, maior_x + 1):
        # Verifica se o produto das funções em pontos consecutivos muda de sinal
        # Se f(x) * f(x + 1) < 0, significa que há uma mudança de sinal, indicando que há uma raiz entre x e x+1
        if f(x) * f(x + 1) < 0:
            # print(f"Tem raiz no intervalo [{x}, {x + 1}]")  # Imprime que há uma raiz no intervalo
            intervalos.append((x, x+1))
            c += 1  # Incrementa o contador de raízes encontradas
            # print(f"Não tem raiz no intervalo [{x}, {x + 1}]")  # Imprime que não há raiz no intervalo

    print(f"Há {c} raizes no intervalo [{menor_x}, {maior_x}]")
    return intervalos  # Retorna o número de raízes encontradas no intervalo


# DESCOMENTAR SE NO DESESPERO

# # Função para encontrar a raiz de um intervalo usando o método da bisseção
# def find_root(vetor: list, erro: float, menor_x: int = -10, maior_x: int = 10):
#     # Cria o polinômio a partir do vetor de coeficientes
#     f = np.poly1d(vetor)
    
#     a = menor_x  # Limite inferior do intervalo
#     b = maior_x  # Limite superior do intervalo
#     p_medio = (a + b) / 2  # Calcula o ponto médio inicial
#     contador = 0  # Inicializa o contador de iterações
    
#     # Enquanto o valor absoluto da função no ponto médio for maior que o erro desejado
#     while abs(f(p_medio)) > erro:
#         # Se a função nos limites a e p_medio tiver sinais opostos, a raiz está entre a e p_medio
#         if f(a) * f(p_medio) < 0:
#             b = p_medio  # Ajusta o limite superior para o ponto médio
#         else: 
#             a = p_medio  # Caso contrário, ajusta o limite inferior para o ponto médio
        
#         contador += 1  # Incrementa o contador de iterações
#         p_medio = (a + b) / 2  # Recalcula o novo ponto médio

#     print(f"A raiz do intervalo [{menor_x}, {maior_x}] é {p_medio}")  # Imprime a raiz encontrada

# Função para verificar se a derivada do polinômio muda de sinal (indicando possíveis raízes)
def n_roots(vetor: list, menor_x: int = -10, maior_x: int = 10):
    # Cria o polinômio a partir do vetor de coeficientes
    f = np.poly1d(vetor)
    
    # Calcula a derivada do polinômio
    f_derivative = f.deriv()

    a = menor_x  # Limite inferior do intervalo
    b = maior_x  # Limite superior do intervalo
    
    # Itera sobre o intervalo [a, b] para verificar mudanças de sinal na derivada
    for x in range(a, b):
        # Se a derivada mudar de sinal entre x e x+1, significa que há uma possível mudança de concavidade
        if f_derivative(x) * f_derivative(x + 1) < 0:
            print(f"Existem possíveis mudanças de concavidade no intervalo [{x}, {x + 1}]")  # Indica mudança de concavidade
            return True  # Retorna True indicando que foi encontrada uma possível mudança de concavidade
    
    return False  # Retorna False se não encontrar mudança de concavidade no intervalo




c = hunt_root(lambda x: (x**math.log(x)) + x**2 + x**3 * math.sin(x), 1, 20)
print("raizes: ", c)
# root = secante(1, 4, 10**15, 0.000000001, lambda x: 3*math.log(x) - 1, lambda x0: (3/x0))
