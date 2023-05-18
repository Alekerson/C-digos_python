Valores = [] # assim se cria uma lista vazia 
#valores = list () ou assim
#1 forma de pedir valores pro usuários
for contador in range(1,6):
    num = int(input("Informe um valor qualquer: "))
    Valores.append(int(input("Informe um valor qualquer: ")))#Inserindo valores na lista
print(Valores, "\n")

#2 forma de pedir valores pro usuários 
for contador in range(1,6):
    Valores.append(int(input("Informe um valor qualquer: ")))#Inserindo valores na lista
print(Valores, "\n")