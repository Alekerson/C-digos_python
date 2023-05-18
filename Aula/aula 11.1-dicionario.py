from os import system

estado = {"uf": "Maranhão", "sigla": "MA",}

system("cls")
print(estado)

#Inserindo dados em um dicionário
#FORMA 1
estado["populacao"] = "20.000.000"
print(estado)

#FORMA 2
estado.update({"Capital": "São luis"})
print(estado)

#Removendo itens do dicionário
#FORMA 1
estado.pop("uf")
print(estado)

#FORMA 2
del(estado["populacao"])
print(estado)

#FORMA 3 - Apagar todo conteúdo
estado.clear()
print(estado)