from os import system
lista = []
cardapio = {}

for contador in range(0,8):
    pratos = input("Qual o nome do prato? ")
    cardapio[pratos] = float(input(f"Informe o valor do {pratos}: "))

    lista.append(cardapio.copy())
    cardapio.clear()

for linha in lista:#obs = sempre que for usar duas variaveis, obrigatoriamente usar o items()
    for chave, valor in linha.items():
        print(f"{chave} = {valor}")