from os import system
lista = []
pessoa = {}

system("cls")
for contador in range(0,7):
    nome = input("Digite seu nome: ")
    pessoa[nome] = int(input("Informe seu número: "))

    lista.append(pessoa.copy())
    pessoa.clear()

for linha in lista:
    for coluna in linha.items():
        print(f"{coluna}", end="")
    print()