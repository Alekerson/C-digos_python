from calculadora import Calculadora

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

calc = Calculadora(n1, n2)

print(f"\n A soma entre {n1} e {n2} é {calc.soma()} \n")
print(f"A subtração entre {n1} e {n2} é {calc.subtracao()} \n")
print(f"A multiplicação entre {n1} e {n2} é {calc.multiplicação()}\n")

calc.divisao()