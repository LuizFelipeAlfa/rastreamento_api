import psycopg2
import psycopg2.extras


class Banco:
    def __init__(self, host, db):
        try:
            self.conexao = psycopg2.connect(host=host, database=db, user='postgres', password='postgres')
            self.cursor = self.conexao.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            self.conexao.set_client_encoding('LATIN1')
        except:
            print("Não foi possivel conectar ao banco de dados.")

    def selecionar(self, query, parametros=None):
        try:
            self.cursor.execute(query, parametros)
            resultado = self.cursor.fetchall()
            return resultado

        except Exception as erro:
            print(f"Erro no selecionar: {erro}")

    def selecionarUm(self, query, parametros=None):
        try:
            self.cursor.execute(query, parametros)
            resultado = self.cursor.fetchone()
            return resultado

        except Exception as erro:
            print(f"Erro no selecionarUm: {erro}")

    def executar(self, query, parametros=None):
        try:
            self.cursor.execute(query, parametros)
            self.conexao.commit()

        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro no executar: {erro}")

    def fecharConexao(self):
        try:
            self.cursor.close()
            self.conexao.close()
        except:
            print("Não foi possível fechar a conexão")
