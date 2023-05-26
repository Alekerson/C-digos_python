class Veiculo:
    def __init__(self, marca, ano, nome):
        self._marca = marca
        self._ano = ano
        self._nome = nome
    @property
    def marca(self):
       return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Carro(Veiculo):
    def __init__(self, marca, ano, nome, quantidadePortas, capacidadePortaMalas):
        super().__init__(marca, ano, nome)
        self.__quantidadePortas = quantidadePortas
        self.__capacidadePortaMalas = capacidadePortaMalas

    @property
    def quantidadePortas(self):
        return self.__quantidadePortas
    
    @quantidadePortas.setter
    def quantidadePortas(self, portas):
        self.__quantidadePortas = portas

    
    @property
    def capacidadePortaMalas(self):
        return self.__capacidadePortaMalas
    
    @capacidadePortaMalas.setter
    def capacidadePortaMalas(self, capacidade):
        self.__capacidadePortaMalas = capacidade