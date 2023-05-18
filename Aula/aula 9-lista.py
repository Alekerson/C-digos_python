notas = [9.5, 7, 6.5, 9]
print(notas)
print(type(notas))

for i in notas:
    print(i)

notas[2] = 8.5
print("-=" * 20)

print(notas, "\n")

#Inserindo valores na lista

notas.append(4) #vai inserir item no final da lista
print(notas, "\n")

#Forma 2
notas.insert(1, 10)#Insert precisa de dois parâmetros. 1- é o índice que desejo inserir o valor. 2- é o valor propriamente dito que quero inserir
print(notas, "\n") 

#Removendo valores
#Forma 1
notas.pop()#exclui o último elemento
print(notas, "\n")

#Forma 2
notas.pop(2) #Removendo pelo índice
print(notas, "\n")

#Forma 3
notas.remove(9.5)#O remove() exclui usando o conteudo como parâmentro
print(notas, "\n")