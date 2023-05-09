valor = []
impar = 0
par = 0

for i in range(1, 11):
    valor.append(i)

for cont in range(0, 10):    
    
    if valor[cont] % 2 == 0:
        par += 1
    else:
        impar += 1

print(valor, "\n")
print(f"Tem {par} números pares! \n")
print(f"Tem {impar} números impares! \n")