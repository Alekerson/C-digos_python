vet = []
cont = 0
posicao = 0
while cont <= 20:
    vet.append(cont)
    cont += 1
for i in range(1, 10):
    if vet[i] == 10:
        posicao = i
print(f"Na posição {posicao} está o número {vet[posicao]}")