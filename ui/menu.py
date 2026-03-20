import os
from core.utils import get_distro

def start_menu():
    distro = get_distro()
    
    while True:
        print(f"\n=== 🐧 Talona Linux Utility ({distro.upper()}) ===")
        print("1. Atualizar Sistema (Upgrade)")
        print("2. Aplicar Tweaks (Otimizações)")
        print("3. Corrigir Horário (Dual Boot RTC)")
        print("0. Sair")

        escolha = input("\nEscolha: ")

        if escolha == "1":
            cmd = "dnf upgrade -y" if distro == "fedora" else "pacman -Syu --noconfirm"
            print(f"🚀 Rodando {cmd}...")
            os.system(f"sudo {cmd}")

        elif escolha == "2":
            try:
                from core.tweaks import ALL_TWEAKS
                
                if not ALL_TWEAKS:
                    print("⚠️  A lista ALL_TWEAKS está vazia.")
                    continue

                print("\n--- 🛠️  Central de Tweaks Linux ---")
                for i, t in enumerate(ALL_TWEAKS, 1):
                    print(f"{i}. {t.INFO['name']} - {t.INFO['desc']}")
                
                print("0. Voltar")
                op = input("\nEscolha o tweak: ")
                
                if op != "0":
                    idx = int(op) - 1
                    ALL_TWEAKS[idx].run()
            
            except (ImportError, AttributeError) as e:
                print(f"❌ Erro ao carregar tweaks: {e}")
            except (ValueError, IndexError):
                print("❌ Opção inválida!")

        elif escolha == "3":
            print("⏳ Ajustando RTC para Local Time...")
            os.system("sudo timedatectl set-local-rtc 1 --adjust-system-clock")
            print("✅ Horário sincronizado com o padrão do Windows.")

        elif escolha == "0":
            print("Saindo... 👋")
            break
        else:
            print("❌ Opção inválida!")

def show_tweaks_menu(tweaks):
    while True:
        print("\n--- 🛠️  Central de Tweaks Linux ---")
        for i, t in enumerate(tweaks, 1):
            print(f"{i}. {t.INFO['name']} - {t.INFO['desc']}")
        print("0. Voltar")

        op = input("\nEscolha o tweak: ")
        if op == "0": break
        
        try:
            idx = int(op) - 1
            tweaks[idx].run()
        except:
            print("❌ Erro ao executar tweak.")