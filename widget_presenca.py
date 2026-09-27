#!/usr/bin/env python3
"""Widget do RaspController: mostra a presença lida do estado.json que o
presenca_quarto.py grava (na mudança e a cada 30s enquanto roda).

Roda uma vez e termina; para atualizar sozinho use o modo "recursive" do app.
Qualquer print sem a tag <result> vira uma caixa de diálogo de erro no app.
"""

import json
import os
import time
from pathlib import Path

ARQUIVO_ESTADO = Path(os.environ.get(
    "ARQUIVO_ESTADO", Path.home() / "presenca-quarto" / "estado.json"))
# O serviço regrava o arquivo a cada 30s; bem mais que isso sem atualizar
# significa que ele está parado e a presença do arquivo não vale mais.
MAX_IDADE_SEG = 90

try:
    dados = json.loads(ARQUIVO_ESTADO.read_text(encoding="utf-8"))
except FileNotFoundError:
    print(f"Arquivo de estado não encontrado: {ARQUIVO_ESTADO}")
except (OSError, ValueError) as e:
    print(f"Erro ao ler {ARQUIVO_ESTADO}: {e}")
else:
    idade = time.time() - float(dados.get("salvo_em") or 0)
    if idade > MAX_IDADE_SEG:
        print(f"Serviço presenca-quarto parado (sem atualizar há {idade:.0f}s)")
    elif dados.get("presenca"):
        print("<result1>Presença detectada</result1>")
    else:
        print("<result1>Sem Presença</result1>")
