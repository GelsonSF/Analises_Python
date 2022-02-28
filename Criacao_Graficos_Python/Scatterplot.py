!pip install malplotlib

import matplotlib.pyplot as plt


# Spot de linhas
x = [1, 3, 5, 7, 9]  # Quantidade de barras
y = [2, 3, 7, 1, 0]  # Tamanho das barras

titulo = 'Scatterplot: Gráfico de Barras'
eixox = 'Eixo X'
eixoy = 'Eixo Y'


# Legendas 
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label = 'Meus Pontos', color='k', marker='.', s=100)
plt.plot(x, y, color='g', linestyle='--')
plt.legend()

plt.show()


# Definindo tamanhos dos circulos
x = [1, 3, 5, 7, 9]  # Quantidade de barras
y = [2, 3, 7, 1, 0]  # Tamanho das barras
z = [550, 500, 6600, 7000, 9800]

titulo = 'Scatterplot: Gráfico de Barras'
eixox = 'Eixo X'
eixoy = 'Eixo Y'


# Legendas 
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label = 'Meus Pontos', color='k', marker='.', s=z)
plt.plot(x, y, color='g', linestyle='--')
plt.legend()

plt.show()