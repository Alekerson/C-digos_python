class Pessoa:
    #ATRIBUTOS
    nome = "Fulano"
    idade = 30
    altura = 1.65

    #MÉTODOS 
    def falar(self, texto):#self é um parântro obrigatório do python que informa que o método pertence á própria classe
        print(texto)

pessoa1 = Pessoa()#instanciando(criar um objeto apartir de uma classe) o objeto
pessoa1.nome =  "José" # alterando o valor do objeto
print(pessoa1.nome)#Mostrando o objeto com valor nome

pessoa1.falar("Olá mundo")