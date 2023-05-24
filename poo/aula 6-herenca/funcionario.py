class Funcionario:
    def __init__(self, cargo, nome):
        self._cargo = cargo #ATRIBUTOS ESTÃO COM APENAS 1 UNDERLINE, PROTEGIDOS
        self._nome = nome

    def informacoes(self):
        print(f"Olá {self._nome}, seu cargo atual é {self._cargo}\n")

class Gerente(Funcionario):
    def __init__(self, cargo, nome, salario):
        super().__init__(cargo, nome)#Super() significa que estamos usando a superclasse que é a classe mãe
        self._salario = salario

    def vocesDecidem(self):
        print(f"Olá sr/sra {self._nome} o seu salário é {self._salario}")