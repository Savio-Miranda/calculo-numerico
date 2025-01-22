import numpy as np


def test_signal(coeficients: list, start: int | None = -10, end: int | None = 10) -> list:
    """
    Fazer uma função que dado uma função 𝑓 (𝑥 ∈ ℝ) ∈ ℝ mostre uma tabela com cada 𝑥 avaliado e o sinal de 𝑓 (𝑥).\n
    ▪ Permita que o usuário escolha o intervalo ou os valores de x;\n
    ▪ Dê um valor padrão para o intervalo caso o usuário não queira escolher;\n
    ▪ Desafio: fazer a tabela mostrando apenas os valores que trocam de sinal.
    """
    values = []
    function = np.poly1d(coeficients)
    for x in range(start, end + 1):
        values.append(float(function(x)))
    return values

values = test_signal([3, -4, -2, 1], -1, 2)
print(values)