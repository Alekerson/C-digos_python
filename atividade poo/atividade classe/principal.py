from aluno import Aluno

for contador in range(0, 3):
    nome = input("Digite seu nome: ")
    matricula = input("Digite sua matricula: ")
    telefone = input("Informe seu telefone: ")
    a1 = Aluno(nome, matricula, telefone)
    a1.exibirDados()