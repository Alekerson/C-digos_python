from projetoFinal import Pratos
p1 = Pratos()

cont = 1
while cont <= 1:
    while True:    
        escolha = int(input('''
1 - Inserir
2 - Atualizar
3 - Consultar
4 - Deletar
5 - Sair

O que deseja: '''))
        if escolha >= 1 and escolha <= 5:
            break 
        
    if escolha == 1:
        nome = input("Informe o nome do prato: ")
        preco = float(input("Informe o valor do prato: "))
        descricao = input("Informe uma descrição para o prato: ")

        p1.inseir(nome, preco, descricao)

    elif escolha == 2:
        while True:
            atualizar = int(input('''1 - nome
2 - Preço
3 - Descrição
O que deseja atualiza: '''))                                                                             
            if atualizar >=1 and atualizar <=3:
                break
        if atualizar == 1:
            id = int(input("Digite o id do prato que quer atualizar: "))
            nome = input("Digite o novo nome do prato: ")
            p1.atualizarNome(id, nome)
        elif atualizar == 2:
            id = int(input("Digite o id do prato que quer atualizar: "))
            preco = float(input("Digite o novo preço do prato: "))
            p1.atualizarPreco(id, preco)
        elif atualizar == 3:
            id = int(input("Digite o id do prato que quer atualizar: "))
            descricao = input("Digite o novo preço do prato: ")
            p1.atualizarPreco(id, descricao)

    elif escolha == 3:
        p1.consulta()

    elif escolha == 4:
        p1.deletar()

    elif escolha == 5:
        cont += 1