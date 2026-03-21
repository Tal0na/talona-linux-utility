import os
import json
from core.utils import get_distro

def run():
    distro = get_distro()
    
    # --- Lógica de Caminho Absoluto ---
    # Encontra a raiz do projeto subindo duas pastas a partir de core/apps/installer.py
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    json_path = os.path.join(base_path, "apps.json")

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ apps.json não encontrado em: {json_path}")
        return
    except json.JSONDecodeError:
        print("❌ Erro de sintaxe no apps.json (verifique vírgulas e aspas).")
        return

    # Filtra apenas apps que têm configuração para a distro atual (arch ou fedora)
    lista_instalar = [a for a in data["apps"] if distro in a]

    if not lista_instalar:
        print(f"⚠️  Nenhum app configurado para {distro} no JSON.")
        return

    print(f"\n--- 📦 Instalador de Apps ({distro.upper()}) ---")
    for i, app in enumerate(lista_instalar, 1):
        manager = app[distro]["manager"]
        print(f"{i}. {app['name']} [{manager}]")
    
    print("A. Instalar TODOS")
    print("0. Voltar")

    op = input("\nEscolha (ex: 1 ou A): ").lower()
    
    if op == "0": 
        return
    
    # Lógica de seleção
    try:
        if op == "a":
            to_install = lista_instalar
        else:
            idx = int(op) - 1
            if 0 <= idx < len(lista_instalar):
                to_install = [lista_instalar[idx]]
            else:
                print("❌ Opção fora do intervalo.")
                return
    except ValueError:
        print("❌ Entrada inválida.")
        return
    
    # Loop de Execução
    for app in to_install:
        config = app[distro]
        manager = config["manager"]
        pkg = config["pkg"]
        
        print(f"\n🛠️  Instalando {app['name']}...")

        if manager == "pacman":
            os.system(f"sudo pacman -S {pkg} --noconfirm --needed")
            
        elif manager == "dnf":
            os.system(f"sudo dnf install {pkg} -y")
            
        elif manager == "flatpak":
            # Garante que o Flathub está adicionado antes de instalar
            os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
            os.system(f"flatpak install flathub {pkg} -y")
            
        elif manager == "aur":
            # Tenta pegar o usuário real que rodou o sudo, ou o user atual
            user = os.getenv("SUDO_USER") or os.getenv("USER")
            helper = "yay" if os.path.exists("/usr/bin/yay") else "paru"
            
            if os.path.exists(f"/usr/bin/{helper}"):
                print(f" usando {helper} como usuário {user}...")
                os.system(f"sudo -u {user} {helper} -S {pkg} --noconfirm")
            else:
                print(f"❌ {helper} não encontrado. Instale um AUR helper primeiro.")

INFO = {"name": "Gerenciar Pacotes", "desc": "Instalação automatizada via JSON"}