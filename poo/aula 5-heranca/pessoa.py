class Pessoa: # super classe ou classe mãe
    def __init__(self, nome, idade):
        self._nome = nome#AO ULTILIZAR APENAS 1 UNDERLINE DIZEMOS, DIZEMOS QUE O ATRIBUTO ESTÁ COM O MODIFICADOR PROTEGIDO, OU SEJA AS CLASSES FILHAS TEM ACESSO AOS ATRIBUTOS DA CLASSE MÃE
        self._idade = idade

    def relatorio(self):
        print(f"Sou uma pessoa.")
        print(f"Olá {self._nome}, sua idade é {self._idade} \n")
    

class Aluno(Pessoa):
    def mostraAluno(self):
        print(f"Sou aluno e meu nome é {self._nome}\n")


class Professor(Pessoa):
    def mostraProfessor(self):
        print(f"Sou professor {self._nome}")