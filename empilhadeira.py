import pandas as pd
import os
from dotenv import load_dotenv

from caminhos import caminho

# Carrega variáveis de ambiente
load_dotenv()

def consolidar_csvs():
    pasta_ars = caminho('PATH_ARS_BASE', 'Ars')
    
    caminho_haipu = os.path.join(pasta_ars, "PFOHAIPU", "PFOHAIPU.csv")
    caminho_5098 = os.path.join(pasta_ars, "PFO5098", "PFO5098.csv")
    
    pasta_saida = os.path.join(pasta_ars, "Saida")
    caminho_final = os.path.join(pasta_ars, "PFO5098p", "PFO5098p.csv")
    os.makedirs(os.path.dirname(caminho_final), exist_ok=True)

    try:
        
        # Como eles não têm cabeçalho (header=None), o Pandas os lê corretamente
        print("Lendo arquivos...")
        df_haipu = pd.read_csv(caminho_haipu, sep=';', header=None, encoding='utf-8-sig')
        df_5098 = pd.read_csv(caminho_5098, sep=';', header=None, encoding='utf-8-sig')

        # Juntar (Concatenar) os dados
        df_final = pd.concat([df_haipu, df_5098], axis=0, ignore_index=True)

        df_final.to_csv(caminho_final, index=False, header=False, sep=';', encoding='utf-8-sig')
        
        print(f"--- SUCESSO ---")
        print(f"Total de linhas Haipu: {len(df_haipu)}")
        print(f"Total de linhas 5098: {len(df_5098)}")
        print(f"Arquivo consolidado criado com {len(df_final)} linhas em: {caminho_final}")
        
        return caminho_final

    except Exception as e:
        print(f"Erro ao juntar os arquivos: {e}")
        return None

if __name__ == "__main__":
    consolidar_csvs()