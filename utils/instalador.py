import subprocess
import sys

def install_requirements():
    # Verificar se o arquivo requirements.txt está presente
    try:
        # Executar o pip install diretamente no código
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Todos os pacotes instalados com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar os pacotes: {e}")  
    