#!/usr/bin/env bash
# =============================================================================
#  main.sh — Talona Linux Utility (Bash Edition)
#  Uso: sudo bash main.sh
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ─── Carregar módulos ─────────────────────────────────────────────────────────
source "$SCRIPT_DIR/core/utils.sh"
source "$SCRIPT_DIR/core/updates/update.sh"
source "$SCRIPT_DIR/core/tweaks/pacman.sh"
source "$SCRIPT_DIR/core/tweaks/system.sh"
source "$SCRIPT_DIR/core/apps.sh"
source "$SCRIPT_DIR/ui/menu.sh"

# ─── Checks iniciais ──────────────────────────────────────────────────────────
require_root
require_pacman

# ─── Iniciar ──────────────────────────────────────────────────────────────────
menu_main
