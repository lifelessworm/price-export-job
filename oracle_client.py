import oracledb
import os
import sys
from dotenv import load_dotenv

from paths import path

load_dotenv()

lib_dir = path('ORACLE_LIB_DIR', 'instantclient_23_0')
oracle_user = os.getenv('ORACLE_USER')
oracle_password = os.getenv('ORACLE_PASSWORD')
oracle_host = os.getenv('ORACLE_HOST')
oracle_port = os.getenv('ORACLE_PORT')
oracle_service = os.getenv('ORACLE_SERVICE')

try:    
    oracledb.init_oracle_client(lib_dir=lib_dir)
    print("Oracle Client initialized successfully!")
except Exception as e:
    print(f"Error initializing Oracle Client: {e}")
    exit(1)

try:
    dsn = f"{oracle_host}:{oracle_port}/{oracle_service}"
    conn = oracledb.connect(
        user=oracle_user,
        password=oracle_password,
        dsn=dsn
    )
    print("Connected to Oracle successfully!")

except Exception as e:
    print(f"FATAL ERROR connecting to Oracle ({oracle_host}:{oracle_port}/{oracle_service}): {e}")
    print("Check whether this machine has network access to the Oracle server (Brasauto network/VPN).")
    sys.exit(1)
