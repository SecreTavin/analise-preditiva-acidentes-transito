import mysql.connector
import pandas as pd

# Conexão com o banco
conexao = mysql.connector.connect(
    host='localhost',
    database='analise_transito',
    user='root',
    password='23245623'
)

# Query para buscar os dados
consulta = "SELECT * FROM acidente"

# Carregar dados diretamente em um DataFrame
df = pd.read_sql(consulta, conexao)

# Fechar conexão
conexao.close()

print(df.head())

