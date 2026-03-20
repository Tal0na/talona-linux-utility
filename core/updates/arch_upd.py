import os

def run():
    print("\n🚀 Iniciando atualização completa do Arch Linux...")
    # Sincroniza bases de dados e atualiza pacotes
    os.system("sudo pacman -Syu --noconfirm")
    print("✅ Sistema atualizado!")

INFO = {"name": "Pacman Update"}