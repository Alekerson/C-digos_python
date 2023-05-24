class Servico:
    def __init__(self, ):
        self.__pedido = 0

    def novoPedido(self):
        self.__pedido += 1

    def cancelarPedido(self):
        self.__pedido -= 1
        
    def exibirPedido(self):
        return self.__pedido
