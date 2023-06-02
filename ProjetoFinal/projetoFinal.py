import pymysql
from os import system
class Pratos:
    def conexao(self):
        con = pymysql.connect(host = "localhost", user = "root", password = "", database = "restaurante_bd")
        return con
    
    def inseir(self, nome, preco, descricao):
        conexao = self.conexao()

        comando = "insert into pratos(nome, preco, descricao) values(%s, %s, %s)"

        valores = (nome, preco, descricao)

        consulta = conexao.cursor()

        consulta.execute(comando, valores)

        conexao.commit()

        conexao.close()

        print(f"{consulta.rowcount} linha foi inserida!")
        system("cls")
    
    def atualizarNome(self, id, nome):
        conexao = self.conexao()
        consulta = conexao.cursor()

        comando = "update pratos set nome = %s where id = %s"

        consulta.execute(comando, (nome, id))
        conexao.commit()
        conexao.close()
        print(f"{consulta.rowcount} linha atualizada com sucesso!")
        system("cls")

    def atualizarPreco(self, id, Preco):
        conexao = self.conexao()
        consulta = conexao.cursor()

        comando = "update pratos set preco = %s where id = %s"

        consulta.execute(comando, (Preco, id))
        conexao.commit()
        conexao.close()
        print(f"{consulta.rowcount} linha atualizada com sucesso!")
        system("cls")

    def atualizarPreco(self, id, descricao):
        conexao = self.conexao()
        consulta = conexao.cursor()

        comando = "update pratos set descricao = %s where id = %s"

        consulta.execute(comando, (descricao, id))
        conexao.commit()
        conexao.close()
        print(f"{consulta.rowcount} linha atualizada com sucesso! \n")
        system("cls")

    def consulta(self):
        Conexao = self.conexao()
        
        comando = "select * from pratos"

        consulta = Conexao.cursor()

        consulta.execute(comando)

        resultado = consulta.fetchall()

        Conexao.close()

        for itens in resultado:
            print(f"id: {itens[0]}, nome: {itens[1]}, preço: {itens[2]}, descrição: {itens[3]}")

    def deletar(self):
        codigo = int(input("Informe o id do prato que você deseja deletar: "))
        comando = "delete from pratos where id = %s"
        conexao = self.conexao()
        consulta = conexao.cursor()
        consulta.execute(comando, codigo)
        conexao.commit()
        consulta.close()
        system("cls")
