#!/usr/bin/env bash
# =============================================================================
#  core/apps.sh — Instalação de aplicativos
#  Espelha o apps.json do projeto original
# =============================================================================

# ─── Lista de apps (pacman ou AUR) ───────────────────────────────────────────
# Formato: "id|nome|manager|pacote"
#   manager: pacman | aur
APPS=(
    "vscode|Visual Studio Code|aur|visual-studio-code-bin"
    "feishin|Feishin|aur|feishin-bin"
    "discord|Discord|pacman|discord"
    "zen|Zen Browser|aur|zen-browser-bin"
    "steam|Steam|pacman|steam"
    "github-desktop|GitHub Desktop|aur|github-desktop-bin"
    "alacritty|Alacritty|pacman|alacritty"
    "mpv|MPV|pacman|mpv"
    "obs|OBS Studio|pacman|obs-studio"
    "easyeffects|Easy Effects|pacman|easyeffects"
    "helium|Helium Browser|aur|helium-browser-bin"
    "shelly|Shelly|aur|shelly-bin"
    "kitty|Kitty Terminal|pacman|kitty"
    "audacity|Audacity|pacman|audacity"
)

_get_aur_helper() {
    if command -v yay &>/dev/null; then echo "yay"
    elif command -v paru &>/dev/null; then echo "paru"
    else echo ""
    fi
}

_install_pkg() {
    local manager="$1" pkg="$2" name="$3"
    case "$manager" in
        pacman)
            pacman -S --noconfirm --needed "$pkg"
            ;;
        aur)
            local aur
            aur=$(_get_aur_helper)
            if [[ -z "$aur" ]]; then
                err "Nenhum AUR helper encontrado. Instale yay ou paru primeiro."
                return 1
            fi
            sudo -u "$REAL_USER" "$aur" -S --noconfirm --needed "$pkg"
            ;;
    esac
    ok "$name instalado!"
}

install_apps_menu() {
    header "Instalar Aplicativos"

    local i=1
    declare -A INDEX_MAP

    for entry in "${APPS[@]}"; do
        IFS='|' read -r id name manager pkg <<< "$entry"
        printf "  ${BOLD}%2d)${RESET} %-20s ${CYAN}[%s]${RESET}\n" "$i" "$name" "$manager"
        INDEX_MAP[$i]="$entry"
        (( i++ ))
    done

    echo -e "  ${BOLD} a)${RESET} Instalar TODOS"
    echo -e "  ${BOLD} 0)${RESET} Voltar"
    echo
    read -rp "Opções (ex: 1 3 5 ou 'a'): " input

    if [[ "$input" == "0" ]]; then return; fi

    if [[ "$input" == "a" ]]; then
        for entry in "${APPS[@]}"; do
            IFS='|' read -r id name manager pkg <<< "$entry"
            info "Instalando $name..."
            _install_pkg "$manager" "$pkg" "$name" || warn "Falha ao instalar $name"
        done
    else
        for num in $input; do
            if [[ -n "${INDEX_MAP[$num]+_}" ]]; then
                IFS='|' read -r id name manager pkg <<< "${INDEX_MAP[$num]}"
                info "Instalando $name..."
                _install_pkg "$manager" "$pkg" "$name" || warn "Falha ao instalar $name"
            else
                warn "Número inválido: $num"
            fi
        done
    fi

    pause
}
