!pip install malplotlib

import matplotlib.pyplot as plt


# Crescimento da População Brasileira 1980 - 2016 (Fonte DataSUS)

dados = open('C:\\Local do Arquivo\\Analitics\\arquivos.csv').readlines() 

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(';')
        x.append(int(linha[0]))
        y.append(int(linha[1]))
                 
plt.plot(x, y)
plt.title('Crescimento da População Brasileirao 1080-2016')
plt.xlabel('Ano')
plt.ylabel('População x100.000.000')

plt.show()


# Crescimento da População Brasileira 1980 - 2016 (Fonte DataSUS)

dados = open('C:\\Local do Arquivo\\Analitics\\arquivos.csv').readlines() 

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(';')
        x.append(int(linha[0]))
        y.append(int(linha[1]))
                 
plt.bar(x, y)
plt.title('Crescimento da População Brasileirao 1080-2016')
plt.xlabel('Ano')
plt.ylabel('População x100.000.000')

plt.show()


# Crescimento da População Brasileira 1980 - 2016 (Fonte DataSUS)

dados = open('C:\\Local do Arquivo\\Analitics\\arquivos.csv').readlines() 

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(';')
        x.append(int(linha[0]))
        y.append(int(linha[1]))
                 
plt.bar(x, y, color='#e4e4e4')
plt.plot(x, y, color='k', linestyle='--')

plt.title('Crescimento da População Brasileirao 1080-2016')
plt.xlabel('Ano')
plt.ylabel('População x100.000.000')

plt.show()
        