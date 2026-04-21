#!/usr/bin/env bash
# =============================================================================
#  core/updates/update.sh — Atualização do sistema
# =============================================================================

run_update() {
    header "Atualizar Sistema"

    if command -v reflector &>/dev/null; then
        info "Atualizando mirrorlist com reflector..."
        reflector --latest 10 --sort rate --country Brazil --protocol https \
            --save /etc/pacman.d/mirrorlist
        ok "Mirrorlist atualizado."
    else
        warn "reflector não instalado — pulando atualização de mirrors."
    fi

    info "Sincronizando e atualizando pacotes..."
    pacman -Syu --noconfirm
    ok "Pacotes do sistema atualizados!"

    if command -v yay &>/dev/null; then
        info "Atualizando AUR com yay..."
        sudo -u "$REAL_USER" yay -Syu --noconfirm
        ok "AUR atualizado (yay)!"
    elif command -v paru &>/dev/null; then
        info "Atualizando AUR com paru..."
        sudo -u "$REAL_USER" paru -Syu --noconfirm
        ok "AUR atualizado (paru)!"
    fi

    pause
}
