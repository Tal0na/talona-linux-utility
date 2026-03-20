import subprocess

def run():
    print("\n⏳ Configurando RTC para Local Time (Compatibilidade Windows)...")
    try:
        # O comando que eu te passei antes, agora automatizado
        subprocess.run(["timedatectl", "set-local-rtc", "1", "--adjust-system-clock"], check=True)
        print("✅ Linux agora salva as horas do jeito que o Windows entende.")
        print("🌐 Sincronizando com NTP...")
        subprocess.run(["timedatectl", "set-ntp", "true"], check=True)
    except Exception as e:
        print(f"❌ Erro: {e}")

INFO = {
    "name": "Corrigir Horário (Dual Boot)",
    "desc": "Faz o Linux usar Local RTC para não bugar o relógio do Windows"
}