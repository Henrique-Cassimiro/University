'''Faça um programa que leia três palavras em português. Essas palavras definem um animal de acordo
com a imagem a seguir. Depois, imprima o animal escolhido pelo usuário, considerando as três palavras
digitadas.
Obs.: considere que o usuário digitará as 3 palavras corretamente, ou seja, não precisa verificar se ele
digitou um valor errado.
A. Calcular e apresentar o total de crianças, a quantidade de litros de leite necessários e o custo para
comprar o leite para alimentar as crianças uma determinada creche que contém de três salas. Para
isso, o usuário deve informar a quantidade de crianças de cada sala. Para o cálculo considere que:
● cada litro de leite alimenta 4 crianças;
● o litro de leite custa R$ 3.50;
● pode ser que sobre leite em uma caixa, mas, todas as crianças devem ser alimentadas.'''

Etapa1 = input("Digite se o animal é vertebrado ou invertebrado: ")

if ( Etapa1 == "vertebrado"):
    
    Etapa2 = input("Digite se o animal é ave ou mamifero: ")
    
    if (Etapa2 == "ave"):
        
        Etapa3 = input("Digite se o animal é carvivoro ou onivoro:")
        
        if (Etapa3 == "carnivoro"):
            
            print("O animal é a Águia")
            
        else:
            
            print("O animal é a pomba")
        
    else:
        
        Etapa3 = input("Digite se o animal é onivoro ou herbivoro")
        
        if (Etapa3 == "onivoro"):
            
            print("Seu animal é o Homem")
            
        else:
            
            print("Seu animal é a vaca")
        
        
    
if (Etapa1 == "invertebrado"):
    
    Etapa2 = input("Digite se o animal é inseto ou anelidio: ")
    
    if (Etapa2 == "inseto"):
        
        Etapa3 = input("Digite se o animal é hematofago ou herbivoro")
        
        if (Etapa3 == "hematofago"):
            
            print("Seu animal é a pulga")
            
        else:
            
            print("Seu animal é a lagarta")
            
    else:
        
        Etapa3 = input("Digite se o animal é hematofago ou onivoro")
        
        if (Etapa3 == "hematofago"):
            
            print("Seu animal é a Sanguessuga")
            
        else:
            
            print("Seu animal é a minhoca")
            
    