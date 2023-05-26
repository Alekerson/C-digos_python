class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def descrever(self):
        print(f"O produto possui o preço R${self._preco}")

    def calcularPreco(self):
        pass

class livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.__autor = autor         
    
    def descrever(self):
        print(f"Livro: {self._nome} - Autor: {self.__autor}\n")

    def calcularPreco(self):
        print(f"O livro custa R${self._preco}\n")

class eletronico(Produto):
    def __init__(self, nome, preco, marca):
        super().__init__(nome, preco)
        self.__marca = marca

    def calcularPreco(self):
        print(f'''Produto: {self._nome}
Marca: {self.__marca}
Valor: {self._preco}
valor reajustado com 20%: {self._preco + (self._preco * 0.2)}
        ''')