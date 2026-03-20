# 🐧 Talona Linux Utility

Um utilitário de sistema modular escrito em Python, projetado para automatizar tarefas de pós-instalação, atualizações e otimizações (tweaks) em ambientes **Arch Linux** e **Fedora**.

## 🚀 Funcionalidades

- **Detecção Automática:** Identifica se você está no Arch ou Fedora e adapta as opções.
- **Update Inteligente:** Centraliza os comandos de atualização (`pacman` ou `dnf`) em um só lugar.
- **Sistema de Tweaks:** - Correção de horário (Dual Boot Windows).
  - Otimização de gerenciadores de pacotes (Cores, Candy, Downloads Paralelos).
  - Limpeza de cache e mirrors automáticos.
- **Estrutura Modular:** Fácil de adicionar novos scripts sem quebrar o menu principal.

## 📂 Estrutura do Projeto

```text
talona-linux-utility/
├── core/
│   ├── updates/    # Scripts de atualização por distro
│   ├── tweaks/     # Otimizações (arch, fedora, shared)
│   └── utils.py    # Lógica de detecção de sistema e root
├── ui/
│   └── menu.py     # Interface de linha de comando
└── main.py         # Ponto de entrada (requer sudo)
```

🛠️ Como usar

## Clone o repositório

```bash
git clone [https://github.com/seu-usuario/talona-linux-utility.git](https://github.com/seu-usuario/talona-linux-utility.git)
cd talona-linux-utility
```

## Execute o utilitário

O script precisa de permissões de superusuário para aplicar as alterações no sistema:

```bash
sudo python3 main.py
```
