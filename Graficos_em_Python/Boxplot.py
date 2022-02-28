!pip install malplotlib

import matplotlib.pyplot as plt


vetor = []

for i in range(50):
    numero_aleatorio = random.randint(0,100)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title('Boxplot')
plt.show()