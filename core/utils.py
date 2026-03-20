import os
import sys
import subprocess

def is_root():
    return os.geteuid() == 0

def run_with_sudo():
    # Se o sudo normal falhar pelo erro de privilégios, usamos o pkexec
    print("🔐 Solicitando privilégios elevados...")
    try:
        # Tenta relançar com sudo
        os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
    except Exception:
        # Se falhar (como no seu caso), tenta o PolicyKit (janela visual)
        os.execvp("pkexec", ["pkexec", sys.executable] + sys.argv)

def get_distro():
    try:
        with open("/etc/os-release") as f:
            info = f.read().lower()
            if "fedora" in info: return "fedora"
            if "arch" in info: return "arch"
    except: pass
    return "linux"