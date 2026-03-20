import os

def run():
    print("\n🚀 Iniciando atualização completa do Fedora (DNF)...")
    os.system("sudo dnf upgrade -y")
    print("✅ Sistema atualizado!")

INFO = {"name": "DNF Upgrade"}