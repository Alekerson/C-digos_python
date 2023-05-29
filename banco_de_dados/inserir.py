import pymysql

#ESTABELECENDO A CONEXÃO COM A BANCO
conexao = pymysql.connect(
    host = "localhost",#Servidor
    user = "root",#usúario
    password = "",#Senha
    database = "departamento_bd"#nome do banco
)

#INSERINDO DADOS NO BANCO
codigo = int(input("Informe o código do funcionário: "))
nome = input("Informe o nome do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))
cargo = input("Informe o cargo do funcionário: ")

#COLOCAMOS %S NO LUGAR DOS DADOS REAIS PARA EVITAR POSSÍVEIS ATAQUES DE SLQ INJECTION. ISSO É UMA IMPLEMENTAÇÃO DA BIBLIOTECA PYMYSQL
comando = "insert into funcionario values(%s, %s, %s, %s)"

campos = (codigo, nome, salario, cargo)#CRIANDO UMA TUPLA COM OS DADOS QUE SERÃO SUBSTITUÍDOS NO COMANDO

consulta = conexao.cursor()#CURSOR() É UM OBJETO QUE IRÁ INTERAJIR DIRETAMENTE COM O BANCO DE DADOS

consulta.execute(comando, campos)#o execute() ele substitui os dados do comando com os dados de campos

conexao.commit()#o commit vai gravar os dados no banco

print(consulta.rowcount, "linha(s) inserida com sucesso! \n")#rowcount conta a quantidade de linhas que o comando executou 

conexao.close()