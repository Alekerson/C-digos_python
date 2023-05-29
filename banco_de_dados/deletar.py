import pymysql

conexao = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "departamento_bd"
)

codigo = int(input("Digite o código do funcionario que deseja deletar? "))

comando = "delete from funcionario where cod_funcionario = %s"

consulta = conexao.cursor()

consulta.execute(comando, codigo)

conexao.commit()

print(f"{consulta.rowcount} linha(s) foram deletada(s)")

conexao.close()