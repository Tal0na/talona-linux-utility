#!/usr/bin/env bash
# =============================================================================
#  core/tweaks/system.sh — Tweaks gerais do sistema
# =============================================================================

tweak_fix_dualboot_time() {
    header "Tweak: Corrigir Horário (Dual Boot Windows)"
    info "Configurando hardware clock para UTC..."
    timedatectl set-local-rtc 0 --adjust-system-clock
    timedatectl set-ntp true
    ok "Horário corrigido. Windows e Linux agora concordam no horário."
    pause
}

tweak_clean_cache() {
    header "Limpeza de Cache e Órfãos"

    if command -v paccache &>/dev/null; then
        info "Limpando cache do pacman (mantém 2 versões por pacote)..."
        paccache -rk2
        ok "Cache limpo."
    else
        warn "paccache não encontrado — instale pacman-contrib."
    fi

    local orphans
    orphans=$(pacman -Qdtq 2>/dev/null || true)
    if [[ -n "$orphans" ]]; then
        echo -e "${YELLOW}Pacotes órfãos encontrados:${RESET}"
        echo "$orphans"
        if confirm "Remover todos os órfãos?"; then
            echo "$orphans" | pacman -Rns - --noconfirm
            ok "Órfãos removidos."
        fi
    else
        info "Nenhum pacote órfão encontrado."
    fi
    pause
}

tweak_reflector() {
    header "Tweak: Configurar reflector automático"
    pacman -S --noconfirm --needed reflector

    cat > /etc/xdg/reflector/reflector.conf <<'EOF'
--latest 10
--sort rate
--country Brazil
--protocol https
--save /etc/pacman.d/mirrorlist
EOF

    systemctl enable --now reflector.timer
    ok "reflector configurado e timer habilitado!"
    pause
}

tweak_install_aur_helper() {
    header "Instalar AUR Helper"

    if command -v yay &>/dev/null; then
        ok "yay já está instalado."; pause; return
    fi
    if command -v paru &>/dev/null; then
        ok "paru já está instalado."; pause; return
    fi

    echo -e "Escolha o AUR helper:"
    echo -e "  ${BOLD}1)${RESET} yay"
    echo -e "  ${BOLD}2)${RESET} paru"
    read -rp "Opção: " choice

    pacman -S --noconfirm --needed git base-devel

    local tmpdir
    tmpdir=$(mktemp -d)

    case "$choice" in
        1)
            sudo -u "$REAL_USER" git clone https://aur.archlinux.org/yay.git "$tmpdir/yay"
            cd "$tmpdir/yay"
            sudo -u "$REAL_USER" makepkg -si --noconfirm
            ok "yay instalado!"
            ;;
        2)
            sudo -u "$REAL_USER" git clone https://aur.archlinux.org/paru.git "$tmpdir/paru"
            cd "$tmpdir/paru"
            sudo -u "$REAL_USER" makepkg -si --noconfirm
            ok "paru instalado!"
            ;;
        *)
            warn "Opção inválida."
            ;;
    esac

    rm -rf "$tmpdir"
    pause
}
