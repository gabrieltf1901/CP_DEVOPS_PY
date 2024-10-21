import oracledb
from datetime import datetime

# Configurações de conexão
dsn = oracledb.makedsn('oracle.fiap.com.br', 1521, service_name='ORCL')  # Altere conforme necessário
connection = None

try:
    # Estabelecendo a conexão
    connection = oracledb.connect(user='rm553635', password='190101', dsn=dsn)
    print("Conexão estabelecida com sucesso!")

    def inserir_aluno(rm, nome, data):
        try:
            cursor = connection.cursor()
            sql = "INSERT INTO alunos_devops (RM, NOME, DATA) VALUES (:1, :2, :3)"
            cursor.execute(sql, (rm, nome, data))
            connection.commit()
            print("Aluno inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir aluno: {e}")
        finally:
            cursor.close()

    def consultar_alunos():
        try:
            cursor = connection.cursor()
            sql = "SELECT RM, NOME, DATA FROM alunos_devops"
            cursor.execute(sql)
            for row in cursor:
                print(f"RM: {row[0]}, Nome: {row[1]}, Data: {row[2]}")
        except Exception as e:
            print(f"Erro ao consultar alunos: {e}")
        finally:
            cursor.close()

    # Insira um aluno
    inserir_aluno(553635, 'GABRIEL TORRES FERNANDES', datetime.now())

    # Consulte os alunos
    consultar_alunos()

except oracledb.DatabaseError as e:
    error, = e.args
    print(f"Erro ao conectar ao banco de dados: {error.message}")

finally:
    if connection:
        connection.close()
        print("Conexão fechada.")
