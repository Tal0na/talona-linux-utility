from core.utils import is_root, run_with_sudo
from ui.menu import start_menu

if __name__ == "__main__":
    if is_root():
        start_menu()
    else:
        run_with_sudo()