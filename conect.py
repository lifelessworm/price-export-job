import oracledb
import os
import sys
from dotenv import load_dotenv

from caminhos import caminho

# Carrega variáveis do arquivo .env
load_dotenv()

# Obtém configurações de ambiente
lib_dir = caminho('ORACLE_LIB_DIR', 'instantclient_23_0')
oracle_user = os.getenv('ORACLE_USER')
oracle_password = os.getenv('ORACLE_PASSWORD')
oracle_host = os.getenv('ORACLE_HOST')
oracle_port = os.getenv('ORACLE_PORT')
oracle_service = os.getenv('ORACLE_SERVICE')

try:    
    oracledb.init_oracle_client(lib_dir=lib_dir)
    print("Oracle Client inicializado com sucesso!")
except Exception as e:
    print(f"Erro ao inicializar o Oracle Client: {e}")
    exit(1)

try:
    dsn = f"{oracle_host}:{oracle_port}/{oracle_service}"
    conn = oracledb.connect(
        user=oracle_user,
        password=oracle_password,
        dsn=dsn
    )
    print("Conectado ao Oracle com sucesso!")

except Exception as e:
    print(f"ERRO FATAL ao conectar ao Oracle ({oracle_host}:{oracle_port}/{oracle_service}): {e}")
    print("Verifique se esta máquina tem acesso de rede ao servidor Oracle (rede da Brasauto/VPN).")
    sys.exit(1)


