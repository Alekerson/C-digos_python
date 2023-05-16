from os import system
lista = []
mercado = {}

system("cls")

for contador in range(0,5):
    nome = input("Informe o nome do produto: ")
    mercado[nome] = int(input(f"Informe a quantidade de {nome}: "))

    lista.append(mercado.copy())#Aqui copia o conteúdo do dicionario para lista
    mercado.clear()#Limpar conteúdo do dicionario

for linha in lista:#aqui comanda a linha 
    for elementos in linha.items():#aqui comando a coluna(obrigatoriamente nessa ordem, primeiro linha e depois coluna)
        print(f" {elementos}", end="")
    print()
