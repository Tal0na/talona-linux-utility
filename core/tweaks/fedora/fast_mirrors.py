import subprocess

def run():
    print("🌐 Buscando os 5 mirrors mais rápidos do Brasil...")
    try:
        subprocess.run([
            "sudo", "reflector", 
            "--country", "Brazil", 
            "--latest", "5", 
            "--protocol", "https", 
            "--sort", "rate", 
            "--save", "/etc/pacman.d/mirrorlist"
        ], check=True)
        print("✅ Mirrorlist atualizada com sucesso!")
    except FileNotFoundError:
        print("❌ Instale o 'reflector' primeiro: sudo pacman -S reflector")

INFO = {
    "name": "Atualizar Mirrors (Brasil)",
    "desc": "Busca os servidores mais rápidos usando Reflector"
}