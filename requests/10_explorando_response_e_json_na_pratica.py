# requests/10_explorando_response_e_json_na_pratica.py

"""
Material pratico: explorando Response e JSON por dentro

Objetivo:
- olhar o objeto `response` com mais calma
- identificar tipos de dados
- navegar em dicionarios e listas de forma logica

Execute com:
python requests/10_explorando_response_e_json_na_pratica.py
"""

import requests


url = "https://httpbin.org/get"
parametros = {"curso": "requests", "topico": "json"}
cabecalhos = {"Accept": "application/json"}

response = requests.get(
    url,
    params=parametros,
    headers=cabecalhos,
    timeout=10,
)

print("=== EXPLORANDO RESPONSE ===")
print(f"Tipo de response: {type(response)}")
print(f"Status code: {response.status_code}")
print(f"URL final: {response.url}")

dados = response.json()

print("\n=== EXPLORANDO O JSON CONVERTIDO ===")
print(f"Tipo de dados: {type(dados)}")
print(f"Chaves principais: {list(dados.keys())}")

print("\n=== ACESSO POR CHAVE ===")
print(f"dados['url']: {dados['url']}")
print(f"dados['args']: {dados['args']}")

print("\n=== ACESSO EM MAIS DE UM NIVEL ===")
print(f"dados['args']['curso']: {dados['args']['curso']}")
print(f"dados['headers']['Accept']: {dados['headers']['Accept']}")

print("\n=== COMO PENSAR NOS COLCHETES ===")
print("dados['args'] -> pega a chave 'args' do dicionario")
print("lista[0] -> pegaria o primeiro item de uma lista")
print("dados['args']['topico'] -> entra em dois niveis de dicionario")
