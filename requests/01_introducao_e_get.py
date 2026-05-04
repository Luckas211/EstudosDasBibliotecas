# requests/01_introducao_e_get.py

"""
Aula 1: introducao a requests e primeira requisicao GET

Objetivo desta aula:
- entender o que e uma requisicao GET
- ler uma linha com `requests.get(...)`
- identificar o que fazem `()`, `.`, `=`, `[]` e `{}`
- observar como a resposta chega ao Python

Execute com:
python requests/01_introducao_e_get.py
"""

import requests

# `url` e uma variavel.
# `=` guarda um valor dentro dessa variavel.
# O valor aqui e uma string com o endereco da API.
url = "https://httpbin.org/get"

print("=== AULA 1: GET BASICO ===")
print(f"URL escolhida: {url}")

# Esta e a linha mais importante da aula:
# response = requests.get(url, timeout=10)
#
# Leia assim:
# - `response` vai guardar o resultado
# - `=` faz a atribuicao
# - `requests` e o modulo importado
# - `.` acessa a funcao `get` dentro do modulo
# - `get` e a funcao que faz a requisicao HTTP GET
# - `(` abre a chamada da funcao
# - `url` e o primeiro argumento enviado
# - `timeout=10` e um argumento nomeado
# - `)` fecha a chamada
response = requests.get(url, timeout=10)

print("\n=== ANALISANDO A RESPOSTA ===")

# `response.status_code` acessa um atributo do objeto Response.
# O ponto `.` aqui significa "pegue algo dentro de response".
print(f"Status code: {response.status_code}")

if response.status_code == 200:
    print("A requisicao deu certo.")
else:
    print("A requisicao nao voltou com sucesso.")

# `response.headers` costuma ser parecido com um dicionario.
# `.get("Content-Type")` tenta buscar uma chave sem quebrar caso ela nao exista.
tipo_conteudo = response.headers.get("Content-Type")
print(f"Content-Type: {tipo_conteudo}")

print("\n=== TEXTO PURO DA RESPOSTA ===")

# `.text` devolve o corpo da resposta como texto.
# `[:120]` pega apenas os 120 primeiros caracteres.
# Nos colchetes `[]`, voce coloca o intervalo que deseja acessar.
print(response.text[:120])

print("\n=== JSON CONVERTIDO PARA PYTHON ===")

# `.json()` converte o JSON da resposta em estruturas Python.
# Normalmente isso vira um dicionario com listas e outros dicionarios dentro.
dados = response.json()

print(dados)
print(f"Tipo da variavel dados: {type(dados)}")

# `dados["url"]`
# - `dados` e um dicionario
# - `["url"]` acessa a chave chamada "url"
print(f"URL devolvida pelo servidor: {dados['url']}")

# `dados["headers"]` acessa outra chave.
# O valor dela tambem e um dicionario.
print(f"Tipo de dados['headers']: {type(dados['headers'])}")

# Exemplo de acesso em dois niveis:
# - primeiro pegamos a chave "headers"
# - depois pegamos a chave "Host" dentro dela
print(f"Host recebido pelo servidor: {dados['headers']['Host']}")

print("\n=== RESUMO MENTAL ===")
print("GET e usado para buscar dados.")
print("response guarda a resposta completa.")
print("response.status_code mostra o resultado numerico.")
print("response.text devolve texto.")
print("response.json() converte JSON em estruturas Python.")
