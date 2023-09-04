'''
05 - Primeira e ultima letra

Escreva um algoritmo que recebe uma palavra e retorne uma mensagem com a primeira e ultima letra.

Por exemplo:
---------------------------------------------
Entrada:
"Sandy"

Saida:
"A primeira letra eh: S, a ultima letra eh: y."
---------------------------------------------
'''

palavra = input("digite uma palavra: ")

primeira = palavra[0]
ultima = palavra[int(len(palavra)-1)]

print("a primeira letra eh: %s, a ultima letra eh: %s" % (primeira, ultima))

# %d é para reservar variaveis do tipo int, %f do tipo float, %s do tipo string