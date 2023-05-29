import pymysql

#ESTABELENCENDO A CONEXÃO
conexao = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "departamento_bd"
)

comando = "select * from funcionario"

consulta = conexao.cursor()

consulta.execute(comando)

#EXIBIR A CONSULTA DO BANCO
resultado = consulta.fetchall()#FETCHALL IRÁ TRAZER TODAS AS LINHAS DE REGISTRO QUE EXISTEM NO BANCO

print(resultado, "\n")

for itens in resultado:
    print(f"nome: {itens[1]}, cargo: {itens[3]}")

consulta.close()