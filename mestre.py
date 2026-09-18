import sys
import os

try:
    from pecas4091 import pecas_online as pecas_4091
    from pecas4091p import pecas_online as pecas_4091p
    from pecas_HAIPU import pecas_online as pecas_haipu
    from pecas5098 import pecas_online as pecas_5098
    from empilhadeira import consolidar_csvs
    from zipador_noturno import zipar_arquivo_4091, zipar_arquivo_5098, zipar_arquivo_4091p, zipar_arquivo_5098p
    from atirador_email import enviar_arquivos_por_email

except ImportError as e:
    print(f"Erro ao importar módulos: {e}")
    sys.exit(1)

if getattr(sys, 'frozen', False):
    pasta_raiz = os.path.dirname(sys.executable)

else:
    pasta_raiz = os.path.dirname(os.path.abspath(__file__))

pasta_saida = os.path.join(pasta_raiz, "Saida", "ZIP_saida")

def executar_rotina():
    print("=== INICIANDO SISTEMA MESTRE ===")

    #Chamar as funções de Extração (Pecas)
    print("\n[PASSO 1] Extraindo dados do Oracle...")
    pecas_haipu()
    pecas_4091()
    pecas_4091p()
    pecas_5098()
    
    # Chamar a Empilhadeira (Juntar os CSVs)
    print("\n[PASSO 2] Iniciando Empilhadeira (Concatenação)...")
    arquivo_unificado = consolidar_csvs()
    
    # Chamar o Zipador (Finalizar na pasta Saida)
    if arquivo_unificado:
        print("\n[PASSO 3] Compactando arquivo para Saída...")
        zipar_arquivo_4091()
        zipar_arquivo_5098()
        zipar_arquivo_4091p()
        zipar_arquivo_5098p()
    else:
        print("\n[ERRO] A empilhadeira não gerou o arquivo unificado.")

    # Chamar o Atirador (Enviar por E-mail)
    print("\n[PASSO 4] Enviando arquivos por e-mail...")
    enviar_arquivos_por_email()

    print("\n=== PROCESSO FINALIZADO COM SUCESSO ===")

if __name__ == "__main__":
    executar_rotina()



