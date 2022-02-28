!pip install malplotlib

import matplotlib.pyplot as plt

# Unico gráfico
x = [1, 2, 3, 4, 5]  # Quantidade de barras
y = [2, 3, 7, 1, 2]  # Tamanho das barras

titulo = 'Gráfico de Barras'
eixox = 'Eixo X'
eixoy = 'Eixo Y'


# Legendas 
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x,y)
plt.show()

# Gráfico comparativo
x1 = [1, 3, 5, 7, 9]  # Quantidade de barras
y1 = [2, 3, 7, 1, 2]  # Tamanho das barras

x2 = [2, 4, 6, 8, 10]  # Quantidade de barras
y2 = [2, 3, 7, 1, 2]  # Tamanho das barras

titulo = 'Gráfico de Barras'
eixox = 'Eixo X'
eixoy = 'Eixo Y'


# Legendas 
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label='Grupo 1')
plt.bar(x2, y2, label='Grupo 2')
plt.legend()

plt.show()