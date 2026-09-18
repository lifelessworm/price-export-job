import smtplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

from caminhos import caminho

def enviar_arquivos_por_email():
    # Carrega variáveis do arquivo .env
    load_dotenv()
    
    # --- CONFIGURAÇÕES DE AMBIENTE ---
    smtp_servidor = os.getenv('SMTP_SERVER')
    smtp_porta = int(os.getenv('SMTP_PORT', 465))
    email_remetente = os.getenv('SMTP_USER')
    senha_app = os.getenv('SMTP_PASSWORD')
    email_destinatario = os.getenv('EMAIL_TO')
    
    msg = MIMEMultipart()
    msg['From'] = email_remetente
    msg['To'] = email_destinatario
    msg['Subject'] = "Relatorio Diario - Peças online"
    
    corpo = "Segue em anexo os arquivos gerados pela rotina automática."
    msg.attach(MIMEText(corpo, 'plain'))

    # Caminhos dos arquivos
    base_zip = caminho('PATH_ZIP_OUTPUT', os.path.join('Saida', 'ZIP_saida'))
    
    print(f"Buscando arquivos em: {base_zip}")
    anexou_algo = False

    # Percorre todas as subpastas procurando por arquivos .zip
    for root, dirs, files in os.walk(base_zip):
        for file in files:
            if file.endswith(".zip"):
                caminho_completo = os.path.join(root, file)
                print(f"Arquivo encontrado e anexado: {file}")
                
                with open(caminho_completo, "rb") as anexo:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(anexo.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={file}")
                    msg.attach(part)
                    anexou_algo = True

    if not anexou_algo:
        print("ERRO: Nenhum arquivo .zip foi encontrado nas pastas. Verifique o caminho!")
        return

    # Conectando ao servidor e enviando (com retry para erros temporários do servidor,
    # como "451 4.3.0 queue file write error")
    tentativas = 3
    espera_segundos = 15
    for tentativa in range(1, tentativas + 1):
        try:
            with smtplib.SMTP_SSL(smtp_servidor, smtp_porta) as server:
                server.login(email_remetente, senha_app)
                server.send_message(msg)
            print("E-mail corporativo enviado com sucesso (via SSL)!")
            break
        except Exception as e:
            print(f"Erro ao enviar e-mail (tentativa {tentativa}/{tentativas}): {e}")
            if tentativa < tentativas:
                print(f"Aguardando {espera_segundos}s antes de tentar novamente...")
                time.sleep(espera_segundos)
            else:
                print("Todas as tentativas de envio falharam.")

if __name__ == "__main__":
    enviar_arquivos_por_email()