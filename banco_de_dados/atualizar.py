import pymysql

conexao = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "departamento_bd"
)

codigo = int(input("Qual o código do funcionário que você deseja atualizar? "))
nome = input("Informe um novo nome do funcionario: ")

comando = "update funcionario set nome = %s where cod_funcionario = %s"

valores = (nome, codigo)

consulta = conexao.cursor()

consulta.execute(comando, valores)

conexao.commit()

print(consulta.rowcount, "linha atualizada com sucesso \n")

consulta.close()