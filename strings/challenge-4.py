'''
04 - Quatro operacoes matematicas

Escreva um algoritmo que recebe dois numeros inteiros, executa as quatro operacoes matematicas basicas nestes numeros (soma, subtracao, multiplicacao e divisao) e retorne uma string no seguinte formato.

Por exemplo:
------------------------------------------------
Entradas:
1, 2

Saida:
"1 + 2 = 3. 1 - 2 = -1. 1 x 2 = 2. 1 / 2 = 0.5."
------------------------------------------------
'''

numero1 = input("digite o primeiro numero: ")
numero1 = int(numero1)
numero2 = input("digite o segundo numero: ")
numero2 = int(numero2)

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print ("%d + %d = %d. %d - %d = %d. %d * %d = %d. %d / %d = %f." % (numero1, numero2, soma, numero1, numero2, subtracao, numero1, numero2, multiplicacao, numero1, numero2, divisao))