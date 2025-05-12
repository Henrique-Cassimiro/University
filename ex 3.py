'''O programa a seguir insere 10 números aleatórios, entre 1 e 50 (inclusive os dois), em uma lista.
import random
numeros = []
i=0
while i<10:
numeros.append(random.randint(1,50))
i=i+1
print("Numeros:", numeros)
Continue a implementação (abaixo do código apresentado), para apresentar:
a) apenas os 5 primeiros elementos;
b) a soma dos elementos que estão em posições pares;
c) o menor entre os 3 últimos elementos'''

import random
numeros = []
i=0
while i<10:
    numeros.append(random.randint(1,50))
    i=i+1
print("Numeros:", numeros)
i = 0
print("Os 5 primeiros elentos são: ")
while (i < 5):
    print(numeros[i])
    i += 1
i=0
somaPscPar = 0
while (i < len(numeros)):
    if (i % 2 == 0):
        somaPscPar += numeros[i]
    i += 1
print(f"A soma dos n´meros nas posições pares é: {somaPscPar}")
i = len(numeros) - 1
menor = float("inf")
while (i > len(numeros) - 4):
    if (menor > numeros[i]):
        menor = numeros[i]
    i -= 1
print(f"O menor dentre os tres ultimos é: {menor}")