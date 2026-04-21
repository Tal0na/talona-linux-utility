```
████████╗ █████╗ ██╗      ██████╗ ███╗   ██╗  █████╗
   ██╔══╝██╔══██╗██║     ██╔═══██╗████╗  ██║ ██╔══██╗
   ██║   ███████║██║     ██║   ██║██╔██╗ ██║ ███████║
   ██║   ██╔══██║██║     ██║   ██║██║╚██╗██║ ██╔══██║
   ██║   ██║  ██║███████╗╚██████╔╝██║ ╚████║ ██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝
                  linux utility — bash edition
```

> pós-instalação automatizada para arch linux

---

## install

```bash
git clone https://github.com/Tal0na/talona-linux-utility
cd talona-linux-utility
sudo bash main.sh
```

---

## estrutura

```
talona/
├── main.sh
├── core/
│   ├── utils.sh
│   ├── apps.sh
│   ├── updates/update.sh
│   └── tweaks/
│       ├── pacman.sh
│       └── system.sh
└── ui/menu.sh
```

---

## features

```
[1] atualizar sistema       pacman + aur + mirrors
[2] tweaks pacman           parallel downloads / candy / color
[3] tweaks sistema          horário dualboot / cache / reflector / aur helper
[4] instalar apps           seleção múltipla pacman + aur
```

---

## adicionar app

```bash
# core/apps.sh
"id|Nome|pacman|pacote"
"id|Nome|aur|pacote-bin"
```

## adicionar tweak

```bash
# core/tweaks/system.sh ou pacman.sh
meu_tweak() { ... }

# ui/menu.sh
echo "X) meu tweak"
X) meu_tweak ;;
```
