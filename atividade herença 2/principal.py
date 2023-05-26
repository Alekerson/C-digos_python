from veiculo import Veiculo, Carro

marca = input("Qual a marca do seu veiculo? ")
ano = int(input("Qual o ano do seu veiculo? "))
nome = input("Qual nome do carro? ")

a = Carro(marca, ano, nome, 4, 220)

print(f"A quantidade de portas do carro {a.nome} da marca {a.marca} é {a.quantidadePortas}")