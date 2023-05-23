from funcionario import Funcionario
insiraNome = input("Digite seu nome: ")
insiraCargo = input("Digite seu cargo: ")

f1 = Funcionario(insiraNome, insiraCargo)

print(f"Seu nome é {f1.getNome()}")#Aqui está exibindo o nome

f1.setNome("Isabella")#Aqui está alterando o nome

print(f"Seu nome é {f1.getNome()}")#Aqui está exibindo o nome


print(f"Seu cargo é {f1.cargo}")

f1.cargo = input("Digite seu cargo: ")

print(f"Seu cargo é {f1.cargo}")