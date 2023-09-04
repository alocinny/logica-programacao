'''
03 - Apresentacao pessoal

Escreva um algoritmo que recebe o primeiro e o ultimo nome de uma pessoa mais a idade, e retorne uma mensagem.

Por exemplo:
---------------------------------------------------
Entradas:
"Joao","Carvalho', 25

Saida:
"Meu nome eh Joao Carvalho e tenho 25 anos de vida."
---------------------------------------------------
'''

nome = input("digite seu primeiro nome: ")
ultimo_nome = input("digite seu ultimo nome: ")
idade = input("digite sua idade: ")

print("Meu nome eh %s %s e tenho %s anos" % (nome,ultimo_nome, idade))