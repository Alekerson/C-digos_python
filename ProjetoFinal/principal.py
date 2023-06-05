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
        validacao = ["nome", "preco", "descricao" ]
        print("="*10,"Cardápio","="*10)
        p1.consulta()
        print("="*40)
        while True:
            campo = input("Qual campo deseja atualiza: ")
            if campo in validacao: #in ele é um operador que comparar um item dentro de uma lista
                break
        id = int(input("Digite o id do prato que quer atualizar: "))
        if campo == "preco":
            valor = float(input("Digite o novo preço do prato: "))
        elif campo == "nome":
            valor = input("Digite o novo nome do prato: ")
        elif campo == "descricao":
            valor = input("Digite a descrição do prato: ")
        p1.atualizarGeral(campo, valor, id)


    elif escolha == 3:
        print("="*10,"Cardápio","="*10)
        p1.consulta()
        print("="*40)

    elif escolha == 4:
        p1.deletar()

    elif escolha == 5:
        cont += 1