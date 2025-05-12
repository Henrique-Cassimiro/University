'''O programa a seguir insere 100 números aleatórios, entre 1 e 500 (inclusive os dois), em uma lista.
import random
numeros = []
i=0
while i<100:
numeros.append(random.randint(1,500))
i=i+1
print("Numeros:", numeros)
Continue a implementação (abaixo do código apresentado), e solicite ao usuário um número e, se ele existir na lista,
informe quantas vezes ele aparece. Caso o número não exista na lista, informe isso ao usuário.'''
import random
numeros = []
i=0
while i<100:
    numeros.append(random.randint(1,500))
    i=i+1
print("Numeros:", numeros)
numero = int(input("Entre com um número: "))
i = 0
vezesNaLista = 0
while (i < len(numeros)):
    if (numero == numeros[i]):
        vezesNaLista += 1
    i += 1
if (numero not in numeros):
    print(f"O numero não está na lista!")
if (numero in numeros):
    print(f"O número se repetiu {vezesNaLista}")