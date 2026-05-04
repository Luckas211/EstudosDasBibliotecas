# requests/04_tratamento_de_erros.py

"""
Aula 4: tratamento de erros em requests

Objetivo desta aula:
- entender por que requisicoes podem falhar
- usar `try` e `except`
- aprender `timeout`
- usar `raise_for_status()`

Execute com:
python requests/04_tratamento_de_erros.py
"""

import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout

print("=== AULA 4: TRATAMENTO DE ERROS ===")

print("\n=== PARTE 1: ERRO DE CONEXAO ===")

url_invalida = "https://endereco.que.nao.existe.com"

try:
    # `timeout=5` faz o programa desistir depois de 5 segundos.
    response = requests.get(url_invalida, timeout=5)
    print(response.status_code)

except ConnectionError as erro:
    print("Houve erro de conexao.")
    print(f"Detalhes tecnicos: {erro}")

except Timeout:
    print("O servidor demorou demais para responder.")

print("\n=== PARTE 2: ERRO HTTP ===")

url_404 = "https://httpbin.org/status/404"

try:
    response_404 = requests.get(url_404, timeout=10)
    print(f"Status recebido: {response_404.status_code}")

    # `raise_for_status()` olha o status code.
    # Se for erro 4xx ou 5xx, ele levanta uma excecao.
    response_404.raise_for_status()

except HTTPError as erro:
    print("O servidor respondeu, mas com erro HTTP.")
    print(f"Detalhes tecnicos: {erro}")

print("\n=== COMO LER ESTA IDEIA ===")
print("try -> tenta executar")
print("except -> captura o erro se algo falhar")
print("timeout=... -> evita espera infinita")
print("raise_for_status() -> transforma status ruim em excecao")

print("\n=== REGRA PRATICA ===")
print("Ao trabalhar com internet, sempre considere falhas de rede.")
