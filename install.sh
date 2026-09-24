#!/bin/bash
# Instala/reinstala o widget de presenca do RaspController.
# Uso: ./install.sh   (rodar de dentro da pasta clonada do repositorio)

set -e

REPO_URL="https://github.com/rtavares-g/widget-presenca.git"
INSTALL_DIR="$HOME/widget-presenca"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ "$SCRIPT_DIR" != "$INSTALL_DIR" ]; then
    if [ ! -d "$INSTALL_DIR" ]; then
        git clone "$REPO_URL" "$INSTALL_DIR"
    fi
    cd "$INSTALL_DIR"
else
    cd "$SCRIPT_DIR"
fi

sudo apt update
sudo apt install -y python3

chmod +x widget_presenca.py

if [ ! -f "$HOME/presenca-quarto/estado.json" ]; then
    echo "==> Aviso: $HOME/presenca-quarto/estado.json nao existe ainda - instale/inicie o presenca-quarto"
fi

echo
echo "==> Saida atual do widget:"
python3 widget_presenca.py || true

echo
echo "==> No app RaspController, crie/edite o widget personalizado com o comando:"
echo "    python3 $(pwd)/widget_presenca.py"
