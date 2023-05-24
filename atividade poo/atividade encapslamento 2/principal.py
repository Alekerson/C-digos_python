from servico import Servico
serv = Servico()

for cont in range(1, 5):
    serv.novoPedido()

serv.cancelarPedido()

print(f"tem {serv.exibirPedido()} pedidos")