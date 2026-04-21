#!/usr/bin/env bash
# =============================================================================
#  core/tweaks/pacman.sh — Otimizações do pacman
# =============================================================================

PACMAN_CONF="/etc/pacman.conf"

tweak_parallel_downloads() {
    header "Tweak: Downloads Paralelos"

    if grep -q "^ParallelDownloads" "$PACMAN_CONF"; then
        warn "ParallelDownloads já está configurado."
    else
        sed -i 's/^#ParallelDownloads.*/ParallelDownloads = 5/' "$PACMAN_CONF"
        ok "ParallelDownloads = 5 ativado."
    fi
    pause
}

tweak_candy() {
    header "Tweak: ILoveCandy (barra de progresso animada)"

    if grep -q "^ILoveCandy" "$PACMAN_CONF"; then
        warn "ILoveCandy já está ativo."
    else
        sed -i '/^Color/a ILoveCandy' "$PACMAN_CONF"
        ok "ILoveCandy ativado!"
    fi
    pause
}

tweak_color() {
    header "Tweak: Color no pacman"

    if grep -q "^Color" "$PACMAN_CONF"; then
        warn "Color já está ativo."
    else
        sed -i 's/^#Color/Color/' "$PACMAN_CONF"
        ok "Color ativado."
    fi
    pause
}

tweak_all_pacman() {
    tweak_color
    tweak_parallel_downloads
    tweak_candy
}
