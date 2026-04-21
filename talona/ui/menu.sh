#!/usr/bin/env bash
# =============================================================================
#  ui/menu.sh — Menus interativos
# =============================================================================

_banner() {
    clear
    echo -e "${BOLD}${BLUE}"
    echo "  ████████╗ █████╗ ██╗      ██████╗ ███╗   ██╗  █████╗ "
    echo "     ██╔══╝██╔══██╗██║     ██╔═══██╗████╗  ██║ ██╔══██╗"
    echo "     ██║   ███████║██║     ██║   ██║██╔██╗ ██║ ███████║"
    echo "     ██║   ██╔══██║██║     ██║   ██║██║╚██╗██║ ██╔══██║"
    echo "     ██║   ██║  ██║███████╗╚██████╔╝██║ ╚████║ ██║  ██║"
    echo "     ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝"
    echo -e "${RESET}${CYAN}           Linux Utility — Bash Edition${RESET}"
    echo
}

menu_tweaks_pacman() {
    while true; do
        _banner
        header "Tweaks › Pacman"
        echo -e "  ${BOLD}1)${RESET} Downloads paralelos"
        echo -e "  ${BOLD}2)${RESET} ILoveCandy (barra animada)"
        echo -e "  ${BOLD}3)${RESET} Color"
        echo -e "  ${BOLD}4)${RESET} Aplicar todos"
        echo -e "  ${BOLD}0)${RESET} Voltar"
        echo
        read -rp "Opção: " opt
        case "$opt" in
            1) tweak_parallel_downloads ;;
            2) tweak_candy ;;
            3) tweak_color ;;
            4) tweak_all_pacman ;;
            0) break ;;
            *) warn "Opção inválida." ;;
        esac
    done
}

menu_tweaks_system() {
    while true; do
        _banner
        header "Tweaks › Sistema"
        echo -e "  ${BOLD}1)${RESET} Corrigir horário (dual boot Windows)"
        echo -e "  ${BOLD}2)${RESET} Limpar cache e órfãos"
        echo -e "  ${BOLD}3)${RESET} Configurar reflector automático"
        echo -e "  ${BOLD}4)${RESET} Instalar AUR helper (yay / paru)"
        echo -e "  ${BOLD}0)${RESET} Voltar"
        echo
        read -rp "Opção: " opt
        case "$opt" in
            1) tweak_fix_dualboot_time ;;
            2) tweak_clean_cache ;;
            3) tweak_reflector ;;
            4) tweak_install_aur_helper ;;
            0) break ;;
            *) warn "Opção inválida." ;;
        esac
    done
}

menu_tweaks() {
    while true; do
        _banner
        header "Tweaks"
        echo -e "  ${BOLD}1)${RESET} 🗄️  Pacman"
        echo -e "  ${BOLD}2)${RESET} ⚙️  Sistema"
        echo -e "  ${BOLD}0)${RESET} ↩  Voltar"
        echo
        read -rp "Opção: " opt
        case "$opt" in
            1) menu_tweaks_pacman ;;
            2) menu_tweaks_system ;;
            0) break ;;
            *) warn "Opção inválida." ;;
        esac
    done
}

menu_main() {
    while true; do
        _banner
        echo -e "  ${BOLD}1)${RESET} 🔄  Atualizar sistema"
        echo -e "  ${BOLD}2)${RESET} 🔧  Tweaks"
        echo -e "  ${BOLD}3)${RESET} 📦  Instalar aplicativos"
        echo -e "  ${BOLD}0)${RESET} 🚪  Sair"
        echo
        read -rp "Opção: " opt
        case "$opt" in
            1) run_update ;;
            2) menu_tweaks ;;
            3) install_apps_menu ;;
            0) echo -e "\n${GREEN}Até mais!${RESET}\n"; exit 0 ;;
            *) warn "Opção inválida." ;;
        esac
    done
}
