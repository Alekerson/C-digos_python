from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("carla", 23)
p1 = Professor("Alekerson", 22)
a1 = Aluno("José", 40)

pessoa1.relatorio()#Método de pessoa

a1.mostraAluno()#Método de aluno
#a1.relatorio()#Método de aluno

p1.mostraProfessor()