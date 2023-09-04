'''
01 - Inverte nomes

Escreva um algoritmo que recebe uma string com o formato "Nome Sobrenome" e retorne
uma outra string com os nomes invertidos.

Por exemplo:
---------------------
Entrada:
"Xablau Xablauzinho"

Saida:
"Xablauzinho Xablau"
---------------------
'''

print("digite seu nome e sobrenome:")
entrada = input()

entrada = entrada.split()
nome = entrada[0]
sobrenome = entrada[1]

print(sobrenome, nome, end=" ")