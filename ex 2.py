'''O programa a seguir insere 6 números aleatórios, entre -5 e 5 (inclusive os dois), em uma lista.
import random
numeros = []
i=0
while i<6:
numeros.append(random.randint(-5,5))
i=i+1
print("Numeros:", numeros)
Continue a implementação (abaixo do código apresentado), para determinar e apresentar:
a) a soma dos elementos positivos;
b) a quantidade de vezes que o primeiro elemento se repete;
c) o maior valor.'''

import random
numeros = []
i=0
while i<6:
    numeros.append(random.randint(-5,5))
    i=i+1
print("Numeros:", numeros)
primeiroElemntoRpt = 0
maiorValor = -6
soma = 0
i=0
while (i < len(numeros)):
    if (numeros[i] > 0):
        soma += numeros[i]
    if (numeros[i] == numeros[0]):
        primeiroElemntoRpt += 1
    if (maiorValor < numeros[i]):
        maiorValor = numeros[i]
    i += 1
print(f"a soma dos elemntos positivos é: {soma}")
print(f"O primeiro elento repetiu {primeiroElemntoRpt}")
print(f"O maior valor é: {maiorValor}")