'''
06 - Nome do cachorro

Joana adotou um cachorrinho e decidiu usar o nome de suas comidas favoritas para dar nome 
a ele, ela vai usar as 3 primeiras letras do seu salgadinho favorito e juntar com as 3 ultimas 
letras do seu doce favorito.

Escreva um algoritmo que recebe o nome do salgadinho e o nome do doce e retorne o nome do cachorrinho de Joana.

Por exemplo:
--------------------
Entradas:
"Chocolate", "Pudim"

Saida:
"Chodim"
--------------------
'''

salgadinho = input("digite o seu salgadinho favorito: ")
doce = input("digite o seu doce favorito: ")
salgadinho = salgadinho[0:3]
doce = doce[len(doce)-3: len(doce)]
print(salgadinho + doce)