import os
import sys
import pandas as pd
import oracledb
from dotenv import load_dotenv

import conect
from caminhos import raiz, caminho

# Carrega variáveis de ambiente
load_dotenv()

def chama_haipu():
    try:
        with open(os.path.join(raiz(), "Querrys/haipu.sql"), "r", encoding="utf-8") as file:
            query = file.read()
            print("Query lida com sucesso!")
            return query
    except Exception as e:
        print(f"Erro ao ler o arquivo SQL: {e}")
        sys.exit(1)

def pecas_online():
    try:
        caminho_sql = os.path.join(raiz(), "Querrys/haipu.sql")
        if not os.path.exists(caminho_sql):
            print(f"Erro: Arquivo {caminho_sql} não encontrado!")
            return
        
        pasta_destino = caminho('PATH_ARS_BASE', 'Ars')
        ArS = "PFOHAIPU"
        caminho_pasta = os.path.join(pasta_destino, ArS)

        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)
            print(f"Pasta criada em: {caminho_pasta}")

        query = chama_haipu()
        print("Buscando dados...")

        cursor = conect.conn.cursor()
        cursor.execute(query)
        
        rows = cursor.fetchall()
        colunas = [col[0] for col in cursor.description]
        
        # Criando o CSV
        df = pd.DataFrame(rows, columns=colunas)

        nome_arquivo = f"{ArS}.csv"
        Cfinal = os.path.join(caminho_pasta, nome_arquivo)

        df.to_csv(Cfinal, index=False, sep=';', header=False, encoding='utf-8-sig')
        
        if os.path.exists(Cfinal):
            print(f"ARQUIVO LOCALIZADO: {Cfinal}")
            print(f"Tamanho do arquivo: {os.path.getsize(Cfinal)} bytes")
        else:
            print("O Python diz que salvou, mas o arquivo não está lá!")

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()

if __name__ == "__main__":
    pecas_online()
