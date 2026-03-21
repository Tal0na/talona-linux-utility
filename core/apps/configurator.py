import os
import shutil
import subprocess
from pathlib import Path

def create_link(src, dst):
    """Remove o que existe e cria o link simbólico limpo"""
    try:
        if dst.is_symlink() or dst.exists():
            if dst.is_dir() and not dst.is_symlink():
                shutil.rmtree(dst)
            else:
                dst.unlink()
        
        dst.parent.mkdir(parents=True, exist_ok=True)
        os.symlink(src, dst)
        print(f"  ✅ Vinculado: {dst.relative_to(Path.home())}")
    except Exception as e:
        print(f"  ❌ Erro em {dst.name}: {e}")

def run():
    print(f"\n--- 🎨 Aplicando Estética Portável (Modo Cirúrgico) ---")
    
    # Forçamos a Home do usuário para evitar erros de permissão/root
    target_home = Path.home()
    if target_home == Path("/root"):
        target_home = Path("/home/talona")

    base_dir = Path(__file__).parents[2] 
    source_home = base_dir / "shared" / "home"

    if not source_home.exists():
        print(f"❌ Erro: Pasta {source_home} não encontrada.")
        return

    # 1. Linkando Aplicativos dentro de .config (Alacritty, Btop, etc.)
    config_src = source_home / ".config"
    if config_src.exists():
        for app in config_src.iterdir():
            if app.is_dir():
                # Se for a pasta 'system', linkamos os arquivos de dentro dela na raiz da .config
                if app.name == "system":
                    for sys_file in app.glob("*"):
                        create_link(sys_file, target_home / ".config" / sys_file.name)
                else:
                    # Linka a pasta do app (ex: .config/alacritty)
                    create_link(app, target_home / ".config" / app.name)

    # 2. Linkando apenas as pastas de recursos em .local/share (Fonts, Icons)
    local_share_src = source_home / ".local" / "share"
    if local_share_src.exists():
        for folder in local_share_src.iterdir():
            if folder.is_dir():
                # Linka as pastas específicas (fonts, icons) sem linkar a .local inteira
                create_link(folder, target_home / ".local" / "share" / folder.name)

    # 3. Arquivos soltos na Home (Ex: .gitconfig, .bashrc)
    for item in source_home.iterdir():
        if item.is_file():
            create_link(item, target_home / item.name)

    # Atualiza o cache de fontes
    subprocess.run(["fc-cache", "-f"], stdout=subprocess.DEVNULL)
    print("\n✨ Sincronização finalizada sem loops!")