#FUNÇÃO SEM PARÂMENTRO
def somar():
    valor1 = int(input("Informe um valor: "))
    valor2 = int(input("Informe outro valor: "))

    print(f"{valor1} + {valor2} = {valor1+valor2}")

#FUNÇÃO COM PARÂMETRO
num1 = int(input("Informe um valor: "))
num2 = int(input("Informe outro valor valor: "))

def multiplicar (a, b):
    print(f"{a} * {b} = {a * b}")

multiplicar(num1, num2)

