from produto import Produto, livro, eletronico
preco = int(input("Qual o preço do prouto? "))

a = eletronico("Celula moto g52", preco, "Motorola")

a.calcularPreco()