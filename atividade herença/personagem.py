class Personagem:
    def __init__(self, nome):
        self._nome = nome
        self._life = 10

    def atacar(self):
          print(f"{self._nome} está sendo atacado, sua vida está em {self._life}pt")
    
class Jogador(Personagem):
    def __init__(self, nome, tipoRaca):
          super().__init__(nome)
          self.__tipoRaca = tipoRaca

    def usarHabilidade(self, poder):
        self.__tipoRaca = poder
        print(f"Usada habilidade: {self.__tipoRaca}")