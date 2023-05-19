class Aluno():
    def __init__(self, nome, matricula, telefone):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone

    def exibirDados(self):
        print(f"A matricula do aluno {self.nome} é: {self.matricula} e o número de telefone é {self.telefone}")