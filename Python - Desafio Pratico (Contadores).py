"""
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
# Meu Metodo
numero1 = 0
numero2 = 10

while numero1 <= 8 or numero2 >= 2:
    print(numero1, numero2)

    numero1 = numero1 + 1
    numero2 = numero2 - 1
else:
    print('Fim da repetição \n')


# Metodo Professor
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
else:
    print('Fim da repetição')
