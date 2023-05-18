while True:
    num = int(input("Digite um número qualquer: "))
    if num > 0:
        break

def calculadora(num):
    vet = []
    for contador in range(1, 11):
        print(f"{num} * {contador} = {num * contador}")

calculadora(num)