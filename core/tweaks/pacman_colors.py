import os
import subprocess

def run():
    conf = "/etc/pacman.conf"
    
    # Verifica se o arquivo existe
    if not os.path.exists(conf):
        print("❌ Arquivo /etc/pacman.conf não encontrado.")
        return

    print("🌈 Tunando o Pacman (Cores, Candy e Downloads)...")
    
    try:
        # Ativa o Color e adiciona o ILoveCandy (o Pac-Man na barra)
        subprocess.run(["sed", "-i", "s/#Color/Color\\nILoveCandy/", conf], check=True)
        
        # Ativa downloads paralelos (aumentando para 10)
        # Tenta substituir tanto a linha comentada quanto uma já ativa
        subprocess.run(["sed", "-i", "s/.*ParallelDownloads.*/ParallelDownloads = 10/", conf], check=True)
        
        print("✅ Pacman otimizado com sucesso!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao editar o arquivo: {e}")
    except PermissionError:
        print("❌ Erro: Acesso negado. Você esqueceu do SUDO?")

INFO = {
    "name": "Otimizar Pacman (Arch)",
    "desc": "Ativa cores, ILoveCandy e 10 downloads paralelos no /etc/pacman.conf"
}