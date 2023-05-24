class Calculadora():
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def soma(self):
        return self.__num1 + self.__num2
    
    def subtracao(self):
        if self.__num1 < self.__num2:
             return self.__num2 - self.__num1
        else:
            self.__num1 - self.__num2
    
    def multiplicação(self):
        return self.__num1 * self.__num2
    
    def divisao(self):
        if self.__num2 <= 0:
            print("Não se pode fazer uma divisão com um divisor menor ou igual a zero")
        else:
            print(f"A divisão entre {self.__num1} e {self.__num2} é {self.__num1/self.__num2:.2f} \n")