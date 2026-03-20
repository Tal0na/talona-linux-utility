import os
import importlib
from core.utils import get_distro

def start_menu():
    distro = get_distro() # Retorna 'arch' ou 'fedora'
    
    while True:
        print(f"\n=== 🐧 Talona Linux Utility ({distro.upper()}) ===")
        print("1. Atualizar Sistema")
        print("2. Aplicar Tweaks (Otimizações)")
        print("0. Sair")

        escolha = input("\nEscolha: ")

        if escolha == "1":
            executar_update(distro)

        elif escolha == "2":
            carregar_tweaks_por_pasta(distro)

        elif escolha == "0":
            print("Saindo... 👋")
            break
        else:
            print("❌ Opção inválida!")

def executar_update(distro):
    """Carrega o script de update da pasta core/updates/"""
    try:
        # Importação dinâmica para evitar erro de 'resolver importação'
        if distro == "arch":
            module = importlib.import_module("core.updates.arch_upd")
        elif distro == "fedora":
            module = importlib.import_module("core.updates.fedora_upd")
        else:
            print("❌ Distro não suportada para update automático.")
            return
            
        module.run()
    except ModuleNotFoundError:
        print(f"❌ Erro: Script de update para {distro} não encontrado em core/updates/")
    except Exception as e:
        print(f"❌ Erro ao executar atualização: {e}")

def carregar_tweaks_por_pasta(distro):
    """Carrega os tweaks das pastas core/tweaks/shared e core/tweaks/[distro]"""
    try:
        tweaks_disponiveis = []

        # 1. Carrega tweaks Compartilhados (Shared)
        try:
            shared_time = importlib.import_module("core.tweaks.shared.fix_time")
            tweaks_disponiveis.append(shared_time)
        except ModuleNotFoundError:
            pass

        # 2. Carrega tweaks específicos da Distro atual
        if distro == "arch":
            try:
                pacman_colors = importlib.import_module("core.tweaks.arch.pacman_colors")
                tweaks_disponiveis.append(pacman_colors)
                # Você pode adicionar mais aqui: clean_cache, fast_mirrors, etc.
            except ModuleNotFoundError:
                print("⚠️  Alguns tweaks do Arch não foram encontrados.")

        elif distro == "fedora":
            try:
                dnf_opt = importlib.import_module("core.tweaks.fedora.dnf_optimize")
                tweaks_disponiveis.append(dnf_opt)
            except ModuleNotFoundError:
                print("⚠️  Alguns tweaks do Fedora não foram encontrados.")

        # Exibição do Menu de Tweaks
        if not tweaks_disponiveis:
            print("❌ Nenhum tweak encontrado nas pastas.")
            return

        print(f"\n--- 🛠️  Tweaks Disponíveis ({distro.title()}) ---")
        for i, t in enumerate(tweaks_disponiveis, 1):
            nome = t.INFO['name']
            desc = t.INFO['desc']
            print(f"{i}. {nome} - {desc}")
        
        print("0. Voltar")
        op = input("\nSelecione o tweak: ")

        if op != "0":
            try:
                idx = int(op) - 1
                if 0 <= idx < len(tweaks_disponiveis):
                    tweaks_disponiveis[idx].run()
                else:
                    print("❌ Opção inválida!")
            except ValueError:
                print("❌ Digite um número válido.")

    except Exception as e:
        print(f"❌ Erro geral no menu de tweaks: {e}")