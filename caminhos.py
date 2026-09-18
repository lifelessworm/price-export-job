import os
import sys


def raiz():
    """Retorna a pasta raiz do projeto.

    Funciona tanto rodando via 'python mestre.py' (ou qualquer script
    individual) quanto via executável compilado com PyInstaller, e
    independe de qual é o diretório de trabalho (cwd) no momento da
    execução -- por isso é seguro chamar isso de dentro de um .bat,
    do Agendador de Tarefas, ou de qualquer outro lugar.
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def caminho(env_var, padrao):
    """Resolve um caminho vindo do .env relativo à raiz do projeto.

    Se o valor salvo no .env já for um caminho absoluto (ex: você quer
    guardar o Ars em outro disco), ele é usado direto, sem modificação.
    Se for relativo (ex: 'Ars', 'instantclient_23_0'), é resolvido a
    partir da raiz do projeto -- não do cwd.
    """
    valor = os.getenv(env_var, padrao)
    if os.path.isabs(valor):
        return valor
    return os.path.join(raiz(), valor)
