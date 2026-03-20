import subprocess

def run():
    print("🧹 Limpando cache do Pacman (mantendo apenas as últimas 2 versões)...")
    try:
        # O comando 'paccache' vem no pacote 'pacman-contrib'
        subprocess.run(["sudo", "paccache", "-r"], check=True)
        print("✅ Cache limpo!")
    except FileNotFoundError:
        print("⚠️  Instalando pacman-contrib para usar o paccache...")
        subprocess.run(["sudo", "pacman", "-S", "pacman-contrib", "--noconfirm"], check=True)
        subprocess.run(["sudo", "paccache", "-r"], check=True)

INFO = {
    "name": "Limpar Cache (Arch)",
    "desc": "Remove versões antigas de pacotes para liberar espaço"
}