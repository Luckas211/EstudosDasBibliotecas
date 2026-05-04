# requests/14_monitorando_varias_urls.py

"""
Aula 14: monitorando varias URLs

Objetivo:
- aplicar requests em um caso mais proximo de automacao real
- verificar o status de varios endpoints
- registrar sucesso e falha de forma simples

Execute com:
python requests/14_monitorando_varias_urls.py
"""

import requests
from requests.exceptions import RequestException


urls = [
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://viacep.com.br/ws/01001000/json/",
]


def verificar_url(url):
    try:
        response = requests.get(url, timeout=10)
        return {
            "url": url,
            "status_code": response.status_code,
            "ok": response.ok,
        }
    except RequestException as erro:
        return {
            "url": url,
            "status_code": None,
            "ok": False,
            "erro": str(erro),
        }


print("=== AULA 14: MONITORAMENTO SIMPLES ===")

for url in urls:
    resultado = verificar_url(url)

    if resultado["ok"]:
        print(f"OK -> {resultado['url']} | status {resultado['status_code']}")
    else:
        print(f"FALHA -> {resultado['url']} | erro {resultado.get('erro')}")
