texto = "Técnico em desenvolvimento de sistemas"
print("------ Título ------")
print(texto)
print("-"*6)
"""
ida = int(input("Diga sua idade: "))
print("#" * ida)
"""
#munipulando string

print(f"O total de letras é {len(texto)}")# len() vem de length, que siguinifica total
print(texto.upper()) # upper() Coloca tudo em Maiúsculo 
print(texto.lower()) # lower () coloca tudo em Minúsculo
print(texto.capitalize()) # Coloca 1° letra em Maiúsculo

print(texto.replace("sistemas", "web")) #replace() troca um texto por outro

#TRABALHANDO COM FATIAMENTO

print("Fatianto a váriavel texto")
print(texto[:3])#Vai exibir todo texto até a posição 2, no caso a posição 3 não conta
print(texto[3:])#vai exibir o texto apartit da posição 3
print(texto[3:10])#vai exibir o texto que está na posição 3 até a 10
