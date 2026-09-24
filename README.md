# widget-presenca

Widget personalizado do app **RaspController** que mostra se há alguém no
quarto, lendo o `~/presenca-quarto/estado.json` gravado pelo serviço
`presenca-quarto` (na mudança e a cada 30 s enquanto roda).

O script roda uma vez e termina; para atualizar sozinho, use o modo
"recursive" do widget no app. Só usa a biblioteca padrão do Python.

| Situação | Saída |
|---|---|
| presença | `<result1>Presença detectada</result1>` |
| sem presença | `<result1>Sem Presença</result1>` |
| `estado.json` sem atualizar há mais de 90 s | mensagem de serviço parado |
| arquivo ausente ou inválido | mensagem de erro |

Qualquer saída sem a tag `<result1>` aparece como caixa de diálogo de erro no
app, o que é usado de propósito para avisar dos problemas acima.

## Instalação

```
git clone https://github.com/rtavares-g/widget-presenca.git ~/widget-presenca
cd ~/widget-presenca
./install.sh
```

O `install.sh` garante o `python3`, avisa se o `presenca-quarto` ainda não
gravou o `estado.json`, mostra a saída atual do widget e o comando para
cadastrar no app:

```
python3 /home/raspberry/widget-presenca/widget_presenca.py
```

## Arquivos

| Arquivo | Função |
|---|---|
| `widget_presenca.py` | lê o `estado.json` e imprime o resultado para o app |
| `install.sh` | instalação/reinstalação |

## Configuração

| Variável | Padrão | Descrição |
|---|---|---|
| `ARQUIVO_ESTADO` | `/home/raspberry/presenca-quarto/estado.json` | arquivo de estado lido |

## Testar

```
python3 widget_presenca.py
```
