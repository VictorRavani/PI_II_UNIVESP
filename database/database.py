import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv
# db = SqliteDatabase('customermanager.db')

load_dotenv()

db = PostgresqlDatabase(
    os.getenv('CREDENCIAL_DATABASE', 'nome_do_banco_de_dados'),  # Nome do banco de dados ou valor padrão
    user=os.getenv('CREDENCIAL_USER', 'seu_usuario'),            # Usuário do banco de dados
    password=os.getenv('CREDENCIAL_PASSWORD', 'sua_senha'),      # Senha do banco de dados
    host=os.getenv('CREDENCIAL_HOST', 'localhost'),              # Endereço do servidor
    port=int(os.getenv('CREDENCIAL_PORT', 5432))                 # Porta do banco de dados
)

