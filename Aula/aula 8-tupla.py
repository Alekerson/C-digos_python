lanche = ("pizza", "hotdog", "refri", "batata")

idade = tuple = (18, 20, 12) #Outra forma de criar tuplas
print(lanche)
print(type(lanche)) # estou mostrando o tipo da variável

print(lanche[1])
print(f"O total de lanches é {len(lanche)} \n")

#lanche[2] ="Suco"

for contador in range (0, 4):
    print(lanche[contador])

print("-="*20)

for i in idade:
    print(i)


print("-="*20)
#enumerate serve para permitir acessar os índices da tupla, já a variável "indice", irá armazenar os valores do índice
for indice, item in enumerate(lanche):
    print(f"{indice} = {item}")