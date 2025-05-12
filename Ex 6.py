'''Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa
cidade, num determinado dia. Para cada casa visitada, foi fornecido o número do
canal (4 ou 5) e a quantidade de pessoas que o estavam assistindo naquela casa.
Se a televisão estivesse desligada, nada era anotado, ou seja, esta casa não entrava
na pesquisa.
Fazer um algoritmo que:
- leia um número indeterminado de dados, sendo que o "FLAG" (condição de
parada) corresponde ao número do canal igual a zero;
- calcule e apresente:
a) a quantidade de casas em que se assistia o canal 4;
b) a quantidade de pessoas que assistiam o canal 5'''

canal = ''
canal4 = 0
canal5 = 0
Tv_ligada = ''

while (canal != "0" ):
    Tv_ligada = input("A tv está ligada?\n")
    if (Tv_ligada == "sim"):
        canal = input("Qual o canal da residencia?\n")
        quantidade = int(input("Digite a quantidade de pessoas assistindo: \n"))
        if (canal == "4"):
            canal4 = canal4 + quantidade
        if (canal == "5"):
            canal5 = canal5 + quantidade    
    canal = input("Qual o canal da residencia?\n")
    
    
    
print(f" Foram {canal4} assistindo o canal 4 e {canal5} assistindo o canal 5")