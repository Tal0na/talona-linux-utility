#!/usr/bin/env bash
# =============================================================================
#  core/utils.sh — Helpers compartilhados
# =============================================================================

# ─── Cores ───────────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

# ─── Logging ─────────────────────────────────────────────────────────────────
info()  { echo -e "${CYAN}[INFO]${RESET}  $*"; }
ok()    { echo -e "${GREEN}[OK]${RESET}    $*"; }
warn()  { echo -e "${YELLOW}[WARN]${RESET}  $*"; }
err()   { echo -e "${RED}[ERRO]${RESET}  $*" >&2; }

header() {
    echo -e "\n${BOLD}${BLUE}══════════════════════════════════════${RESET}"
    echo -e "${BOLD}${BLUE}  $*${RESET}"
    echo -e "${BOLD}${BLUE}══════════════════════════════════════${RESET}\n"
}

# ─── Interação ───────────────────────────────────────────────────────────────
pause() { read -rp $'\n'"${YELLOW}[ENTER para continuar...]${RESET}" _; }

confirm() {
    local msg="${1:-Continuar?}"
    read -rp "$(echo -e "${YELLOW}${msg} [s/N]: ${RESET}")" ans
    [[ "${ans,,}" == "s" ]]
}

# ─── Verificações ────────────────────────────────────────────────────────────
require_root() {
    [[ $EUID -eq 0 ]] || { err "Execute com sudo: sudo bash main.sh"; exit 1; }
}

require_pacman() {
    command -v pacman &>/dev/null \
        || { err "pacman não encontrado. Este script é para Arch Linux."; exit 1; }
}

# Usuário real que chamou o sudo
REAL_USER="${SUDO_USER:-$USER}"
