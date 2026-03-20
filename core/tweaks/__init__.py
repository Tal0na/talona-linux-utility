from .arch import pacman_colors
from .fedora import dnf_optimize
from .shared import fix_time

# Esta lista é o que o menu vai ler
ALL_TWEAKS = [
    pacman_colors,
    dnf_optimize,
    fix_time
]