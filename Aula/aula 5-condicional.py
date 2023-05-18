nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7: 
    print("Você passou!")
elif media == 6:
    print("Você ficou de recuperação")
else:
    print("Você não passou!")
