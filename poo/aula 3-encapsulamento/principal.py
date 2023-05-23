from conta import Conta
minhaConta = Conta(123, "Robervaldo Magalhães", 20000 )

minhaConta.relatorio()
minhaConta.saldo = 80500
minhaConta.meuSaldo()

"""modo de fazer para pedir para o úsuario digitar as informações 
minhaConta.numero = int(input("Digite o número da sua conta: "))
minhaConta.titular = input("Digite seu nome: ")
minhaConta.saldo = int(input("Digite seu saldo:"))
minhaConta.limite = int(input("Informe seu limite: "))
"""
print(f"Seu limite é R${minhaConta.getLimite()}")

minhaConta.setLimite(-600)

print(f"Seu limite é R${minhaConta.getLimite()}")