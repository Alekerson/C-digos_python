class Conta:
    def __init__(self, numero, titular, saldo, limite=100):
        self.__numero = numero # em python tornamos um elemento privado com 2 uderlines. 1 uderline ele está protegido, com nenhum ele está público
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite #Esse atributo possui um valor padrão de forma que o úsuario poderá ou não informar este valor

    def relatorio(self):
        print(f"Olá, {self.__titular} o número da sua conta é {self.__numero} e o seu saldo é R${self.__saldo} e seu limite é de {self.__limite}")

    def meuSaldo(self):
        print(f"o Saldo da sua conta Sr/Sra {self.__titular} é R${self.__saldo}")

    # O método get irá retornar ou exibir o valor do atributo
    def getLimite(self):
        return self.__limite
    
    # O método set irá alterar o contéudo do atributo, sem exibir nada
    def setLimite(self, valor):
        if valor < 0:
            print("Valor menor que zero, informe outro valor")
        else:
            self.__limite = valor
    #VAMOS MODIFICAR O ATRBUTO SALDO COM @PROPERTY E @SETTER
    @property
    def saldo(self):
        print(f"Olá, seu saldo é {self.__saldo} \n")
    
    @saldo.setter
    def saldo(self, valor):
        if valor <= 0:
            print("Você não pode inserir um valor negativo ou zero \n")
        else:
            self.__saldo = valor