import os
import importlib
from core.utils import get_distro

def start_menu():
    distro = get_distro() 
    
    while True:
        print(f"\n=== 🐧 Talona Linux Utility ({distro.upper()}) ===")
        print("1. Atualizar Sistema")
        print("2. Aplicar Tweaks (Otimizações)")
        print("3. Instalar Pacotes (JSON)")
        print("4. Aplicar Configurações (Dotfiles)") # NOVA OPÇÃO!
        print("0. Sair")

        escolha = input("\nEscolha: ")

        if escolha == "1":
            executar_update(distro)

        elif escolha == "2":
            carregar_tweaks_por_pasta(distro)

        elif escolha == "3": # Movemos a lógica para o lugar certo
            try:
                # Usando importlib para manter o padrão do projeto
                module = importlib.import_module("core.apps.installer")
                module.run()
            except ModuleNotFoundError:
                print("❌ Erro: Script 'core/apps/installer.py' não encontrado.")
            except Exception as e:
                print(f"❌ Erro no instalador: {e}")

        elif escolha == "4":
            try:
                module = importlib.import_module("core.apps.configurator")
                module.run()
            except ModuleNotFoundError:
                print("❌ Erro: Script 'core/apps/configurator.py' não encontrado.")
            except Exception as e:
                print(f"❌ Erro ao configurar: {e}")

        elif escolha == "0":
            break

        elif escolha == "0":
            print("Saindo... 👋")
            break
        else:
            print("❌ Opção inválida!")

def executar_update(distro):
    try:
        if distro == "arch":
            module = importlib.import_module("core.updates.arch_upd")
        elif distro == "fedora":
            module = importlib.import_module("core.updates.fedora_upd")
        else:
            return
            
        module.run()
    except Exception as e:
        print(f"❌ Erro ao executar atualização: {e}")

def carregar_tweaks_por_pasta(distro):
    """Focada APENAS em carregar e listar tweaks"""
    try:
        tweaks_disponiveis = []

        # 1. Carrega tweaks Compartilhados
        try:
            shared_time = importlib.import_module("core.tweaks.shared.fix_time")
            tweaks_disponiveis.append(shared_time)
        except ModuleNotFoundError: pass

        # 2. Carrega tweaks específicos da Distro
        if distro == "arch":
            try:
                pacman_colors = importlib.import_module("core.tweaks.arch.pacman_colors")
                tweaks_disponiveis.append(pacman_colors)
            except ModuleNotFoundError: pass
        elif distro == "fedora":
            try:
                dnf_opt = importlib.import_module("core.tweaks.fedora.dnf_optimize")
                tweaks_disponiveis.append(dnf_opt)
            except ModuleNotFoundError: pass

        if not tweaks_disponiveis:
            print("❌ Nenhum tweak encontrado.")
            return

        print(f"\n--- 🛠️  Tweaks Disponíveis ({distro.title()}) ---")
        for i, t in enumerate(tweaks_disponiveis, 1):
            print(f"{i}. {t.INFO['name']} - {t.INFO['desc']}")
        
        print("0. Voltar")
        op = input("\nSelecione o tweak: ")

        if op != "0":
            idx = int(op) - 1
            if 0 <= idx < len(tweaks_disponiveis):
                tweaks_disponiveis[idx].run()

    except Exception as e:
        print(f"❌ Erro no menu de tweaks: {e}")