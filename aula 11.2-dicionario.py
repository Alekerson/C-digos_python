from os import system
pessoa = dict()#Dicionario
grupo = list()#Lista

system("cls")
grupo.append({"Nome": "João", "Idade": 56})
grupo.append({"Nome": "Maria", "Idade": 27})
grupo.append({"Nome": "José", "Idade": 32})
"""
for contador in range(0,3):
    pessoa["nome"] = input("Qual o seu nome? ")
    pessoa["Idade"]= int(input("Qual sua idade? "))

    grupo.append(pessoa.copy())#Criando cópias do dicionário, sem criar vínculo ao dicionário(copiando e limpando)
"""

print(grupo, "\n")
#ACESSANDO ITENS DO DICIONÁRIO
'''for contador in range(0,3):
    print(f"{grupo[contador]['Nome']}: {grupo[contador]['Idade']}\n")
'''
#OUTRA FORMA DE ACESSAR O DICIONÁRIO
for linha in grupo:
    for elementos in linha.values():
        print(f" {elementos}")