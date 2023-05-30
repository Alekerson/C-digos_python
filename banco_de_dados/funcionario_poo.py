import pymysql
class Funcionario:
    def conexao(self):
        con = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "departamento_bd"
        )
        return con

    def inserir(self, codigo, nome, salario, cargo):

        conexao = self.conexao() #Estamos chamando o método que irá conectar ao banco

        comando = "insert into funcionario values(%s, %s, %s, %s)"

        valores = (codigo, nome, salario, cargo)

        consulta = conexao.cursor()

        consulta.execute(comando, valores)

        conexao.commit()

        print(f"{consulta.rowcount} linha(s) inserida(s) com sucesso! ")

        consulta.close()

    def consultar(self):
        conexao = self.conexao()

        comando = "Select * from funcionario"

        consulta = conexao.cursor()

        consulta.execute(comando)

        resultado = consulta.fetchall()

        print(resultado,"\n")

        conexao.close()

    def atualizar(self, codigo, nome):
        conexao = self.conexao()

        comando = "update funcionario set nome = %s where cod_funcionario = %s"

        valores = (nome, codigo)

        consultar = conexao.cursor()

        consultar.execute(comando, valores)

        conexao.commit()

        print(f"{consultar.rowcount} linha(s) foram atualizada(s)")

        consultar.close()