!pip install malplotlib

import matplotlib.pyplot as plt

# Entrada dados da bacteria
entrada = open('C:\\Local Arquivo\\bacteria.fasta').read()
saida = open('bacteria.html','w')

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace('\n','')        

for i in range(len(entrada)-1):
    cont[entrada[i]+entrada[i+1]] += 1

# HTML
saida.write('<div>')

i = 1
for k in cont:
    transparencia = cont[k] / max(cont.values())
    saida.write('<div style= "width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, '+str(transparencia)+'")>'+k+'</div>')
    
    if i%4 == 0:
        saida.write('<div style="clear:both"></div>')
    i+=1
    
saida.close()


# Entrada dados humano
entrada = open('C:\\Local Arquivo\\human.fasta').read()
saida = open('human.html','w')

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace('\n','')        

for i in range(len(entrada)-1):
    cont[entrada[i]+entrada[i+1]] += 1

# HTML
saida.write('<div>')

i = 1
for k in cont:
    transparencia = cont[k] / max(cont.values())
    saida.write('<div style= "width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, '+str(transparencia)+'")>'+k+'</div>')
    
    if i%4 == 0:
        saida.write('<div style="clear:both"></div>')
    i+=1
    
saida.close()

