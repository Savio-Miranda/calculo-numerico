import numpy as np
import matplotlib.pyplot as plt

def plot(coefs: list, X: list, Y: list, f):
    # Geração dos valores de x de -5 a 5
    x_vals = np.linspace(-5, 5, 100)
    y_vals = f(x_vals)

    # Plotando o gráfico
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label=r'teste', color='b')
    
    # Destacando os pontos X e Y fornecidos
    plt.scatter(X, Y, color='red', zorder=5, label='Pontos dados')  # Pontos vermelhos

    # Adicionando linhas de grade e rótulos
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Legenda e rótulos
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gráfico da Função Não Linear")
    
    # Exibindo o gráfico
    plt.show()