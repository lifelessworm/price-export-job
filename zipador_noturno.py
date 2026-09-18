import zipfile
import os
from dotenv import load_dotenv

from caminhos import caminho

# Carrega variáveis de ambiente
load_dotenv()

def zipar_arquivo_5098():
    pasta_saida = caminho('PATH_ZIP_OUTPUT', os.path.join('Saida', 'ZIP_saida'))
    pasta_base = caminho('PATH_ARS_BASE', 'Ars')
    sub_pasta = "PFO5098"
    nome_csv = "PFO5098.csv"
    nome_zip = "PFO5098.zip"
    
    caminho_csv = os.path.join(pasta_base, sub_pasta, nome_csv)
    caminho_zip = os.path.join(pasta_saida, nome_zip)

    #  Verifica se o CSV realmente existe 
    if os.path.exists(caminho_csv):
        try:
            print(f"Localizando arquivo: {nome_csv}...")
            
            # Criando o arquivo ZIP
            os.makedirs(os.path.dirname(caminho_zip), exist_ok=True)
            with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(caminho_csv, arcname=nome_csv)
            
            print(f"Sucesso! Arquivo compactado em: {caminho_zip}")
            
        except Exception as e:
            print(f"Erro ao compactar: {e}")
    else:
        print(f"Erro: O arquivo {caminho_csv} não foi encontrado.")

if __name__ == "__main__":
    zipar_arquivo_5098()

#4091 começa aqui
def zipar_arquivo_4091():
    pasta_saida = caminho('PATH_ZIP_OUTPUT', os.path.join('Saida', 'ZIP_saida'))
    pasta_base = caminho('PATH_ARS_BASE', 'Ars')
    sub_pasta = "PFO4091"
    nome_csv = "PFO4091.csv"
    nome_zip = "PFO4091.zip"
    
    caminho_csv = os.path.join(pasta_base, sub_pasta, nome_csv)
    caminho_zip = os.path.join(pasta_saida, nome_zip)

    #  Verifica se o CSV realmente existe 
    if os.path.exists(caminho_csv):
        try:
            print(f"Localizando arquivo: {nome_csv}...")
            
            # Criando o arquivo ZIP
            os.makedirs(os.path.dirname(caminho_zip), exist_ok=True)
            with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(caminho_csv, arcname=nome_csv)
            
            print(f"Sucesso! Arquivo compactado em: {caminho_zip}")
            
        except Exception as e:
            print(f"Erro ao compactar: {e}")
    else:
        print(f"Erro: O arquivo {caminho_csv} não foi encontrado.")

if __name__ == "__main__":
    zipar_arquivo_4091()

#4091p começa aqui
def zipar_arquivo_4091p():
    pasta_saida = caminho('PATH_ZIP_OUTPUT', os.path.join('Saida', 'ZIP_saida'))
    pasta_base = caminho('PATH_ARS_BASE', 'Ars')
    sub_pasta = "PFO4091p"
    nome_csv = "PFO4091p.csv"
    nome_zip = "PFO4091p.zip"
    
    caminho_csv = os.path.join(pasta_base, sub_pasta, nome_csv)
    caminho_zip = os.path.join(pasta_saida, nome_zip)

    #  Verifica se o CSV realmente existe 
    if os.path.exists(caminho_csv):
        try:
            print(f"Localizando arquivo: {nome_csv}...")
            
            # Criando o arquivo ZIP
            os.makedirs(os.path.dirname(caminho_zip), exist_ok=True)
            with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(caminho_csv, arcname=nome_csv)
            
            print(f"Sucesso! Arquivo compactado em: {caminho_zip}")
            
        except Exception as e:
            print(f"Erro ao compactar: {e}")
    else:
        print(f"Erro: O arquivo {caminho_csv} não foi encontrado.")

if __name__ == "__main__":
    zipar_arquivo_4091p()

#5098p começa aqui
def zipar_arquivo_5098p():
    pasta_saida = caminho('PATH_ZIP_OUTPUT', os.path.join('Saida', 'ZIP_saida'))
    pasta_base = caminho('PATH_ARS_BASE', 'Ars')
    sub_pasta = "PFO5098p"
    nome_csv = "PFO5098p.csv"
    nome_zip = "PFO5098p.zip"
    
    caminho_csv = os.path.join(pasta_base, sub_pasta, nome_csv)
    caminho_zip = os.path.join(pasta_saida, nome_zip)

    #  Verifica se o CSV realmente existe 
    if os.path.exists(caminho_csv):
        try:
            print(f"Localizando arquivo: {nome_csv}...")
            
            # Criando o arquivo ZIP
            os.makedirs(os.path.dirname(caminho_zip), exist_ok=True)
            with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(caminho_csv, arcname=nome_csv)
            
            print(f"Sucesso! Arquivo compactado em: {caminho_zip}")
            
        except Exception as e:
            print(f"Erro ao compactar: {e}")
    else:
        print(f"Erro: O arquivo {caminho_csv} não foi encontrado.")

if __name__ == "__main__":
    zipar_arquivo_5098p()