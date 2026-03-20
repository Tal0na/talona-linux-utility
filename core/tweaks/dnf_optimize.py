def run():
    conf_path = "/etc/dnf/dnf.conf"
    print(f"🚀 Otimizando {conf_path}...")
    
    try:
        with open(conf_path, "a") as f:
            f.write("\nmax_parallel_downloads=10\nfastestmirror=True\n")
        print("✅ DNF agora vai baixar pacotes em paralelo (10 por vez)!")
    except Exception as e:
        print(f"❌ Erro (rode como sudo): {e}")

INFO = {
    "name": "Otimizar DNF (Fedora)",
    "desc": "Ativa downloads paralelos e espelho mais rápido"
}