from random import randint
import os

os.system("cls")# para limpar tela
sorteio = []#criando lista vazia

for contador in range(1, 11):
    sorteio.append(randint(1, 100))#gerando valores aleatórios e salvando na lista

#Valor = randint(1,100)#essa função irá gerar um número aleatório entre 1 e 100
print(sorteio)
sorteio.sort()#a função sort() ordena tua lista de forma crescente
sorteio.sort(reverse=True)#ordenando a lista de forma decrescente
print(sorteio)
os.system("Pause")#Irá pausar o sistema até uma tecla ser pressionada

