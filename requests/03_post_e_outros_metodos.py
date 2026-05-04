# requests/03_post_e_outros_metodos.py

"""
Aula 3: POST, data, json e outros metodos HTTP

Objetivo desta aula:
- entender a diferenca entre GET e POST
- aprender o que colocar em `data={}` e em `json={}`
- conhecer um exemplo com XML
- entender melhor `Content-Type`
- conhecer rapidamente PUT, PATCH e DELETE

Execute com:
python requests/03_post_e_outros_metodos.py
"""

import requests

url_post = "https://httpbin.org/post"

print("=== AULA 3: POST E OUTROS METODOS ===")

print("\n=== PARTE 1: ENVIANDO DATA DE FORMULARIO ===")

# `data={}` costuma ser usado para formularios simples.
dados_formulario = {
    "nome": "Ana",
    "email": "ana@email.com",
    "curso": "requests",
}

# O servidor vai receber esses dados como formulario.
response_form = requests.post(url_post, data=dados_formulario, timeout=10)
dados_resposta_form = response_form.json()

print(f"Status code: {response_form.status_code}")
print("Dados de formulario que o servidor recebeu:")
print(dados_resposta_form["form"])
print(
    "Content-Type recebido pelo servidor: "
    f"{dados_resposta_form['headers'].get('Content-Type')}"
)

print("\n=== PARTE 2: ENVIANDO JSON ===")

# `json={}` envia um corpo em JSON.
# E muito comum em APIs modernas.
payload_json = {
    "produto": "notebook",
    "quantidade": 2,
    "ativo": True,
}

response_json = requests.post(url_post, json=payload_json, timeout=10)
dados_resposta_json = response_json.json()

print(f"Status code: {response_json.status_code}")
print("JSON que o servidor recebeu:")
print(dados_resposta_json["json"])
print(
    "Content-Type recebido pelo servidor: "
    f"{dados_resposta_json['headers'].get('Content-Type')}"
)

print("\n=== PARTE 3: ENVIANDO XML MANUALMENTE ===")

xml_payload = """
<pedido>
    <produto>notebook</produto>
    <quantidade>2</quantidade>
</pedido>
""".strip()

headers_xml = {
    "Content-Type": "application/xml",
    "Accept": "application/json",
}

response_xml = requests.post(
    url_post,
    data=xml_payload,
    headers=headers_xml,
    timeout=10,
)
dados_resposta_xml = response_xml.json()

print(f"Status code: {response_xml.status_code}")
print("Cabecalho Content-Type recebido pelo servidor:")
print(dados_resposta_xml["headers"].get("Content-Type"))
print("Corpo bruto recebido pelo servidor:")
print(dados_resposta_xml["data"])

print("\n=== DIFERENCA MENTAL ===")
print("data=... -> pense em formulario")
print("json=... -> pense em API moderna")
print("data=xml_string + Content-Type application/xml -> pense em XML manual")

print("\n=== COMO LER A LINHA ===")
print("requests.post(url_post, json=payload_json, timeout=10)")
print("- requests: modulo")
print("- post: funcao para POST")
print("- url_post: destino")
print("- json=payload_json: corpo JSON")
print("- timeout=10: tempo maximo de espera")

print("\n=== REGRA PROFISSIONAL IMPORTANTE ===")
print("Nem toda API moderna usa JSON, embora JSON seja o mais comum.")
print("Alguns sistemas pedem XML, texto puro ou formulario.")
print("Leia a documentacao antes de escolher `json=` ou `data=`.")

print("\n=== OUTROS METODOS HTTP ===")

# Nao precisamos executar todos aqui para entender a ideia.
# O importante e saber a intencao de cada um.
print("GET -> buscar dados")
print("POST -> criar ou enviar dados")
print("PUT -> atualizar tudo")
print("PATCH -> atualizar parte")
print("DELETE -> remover")

# Exemplo visual de como seriam as chamadas:
print("\nExemplos de sintaxe:")
print("requests.get(url)")
print("requests.post(url, json={...})")
print("requests.put(url, json={...})")
print("requests.patch(url, json={...})")
print("requests.delete(url)")
