# requests/05_sessoes_e_autenticacao.py

"""
Aula 5: sessoes e autenticacao

Objetivo desta aula:
- entender o que uma Session faz
- aprender como cookies podem ser mantidos
- conhecer autenticacao basica com `auth=(usuario, senha)`

Execute com:
python requests/05_sessoes_e_autenticacao.py
"""

import requests

print("=== AULA 5: SESSOES E AUTENTICACAO ===")

print("\n=== PARTE 1: SESSION ===")

# `requests.Session()` cria um objeto de sessao.
# Pense nele como um cliente que "lembra" informacoes entre requisicoes.
with requests.Session() as sessao:
    # Esta rota define um cookie.
    sessao.get(
        "https://httpbin.org/cookies/set/nome_cookie/valor_cookie",
        timeout=10,
    )

    # Como usamos a mesma sessao, o cookie pode ser reenviado depois.
    response_cookies = sessao.get("https://httpbin.org/cookies", timeout=10)
    dados_cookies = response_cookies.json()

    print("Cookies vistos pelo servidor:")
    print(dados_cookies)

print("\n=== COMO LER ===")
print("with requests.Session() as sessao:")
print("- with abre um contexto controlado")
print("- Session() cria a sessao")
print("- as sessao guarda o objeto com esse nome")

print("\n=== PARTE 2: AUTENTICACAO BASICA ===")

url_auth = "https://httpbin.org/basic-auth/user/pass"

response_sem_auth = requests.get(url_auth, timeout=10)
print(f"Sem auth -> status: {response_sem_auth.status_code}")

# `auth=("user", "pass")`
# Aqui temos uma tupla dentro de `()`.
# O primeiro item e o usuario.
# O segundo item e a senha.
response_com_auth = requests.get(url_auth, auth=("user", "pass"), timeout=10)
print(f"Com auth -> status: {response_com_auth.status_code}")

if response_com_auth.status_code == 200:
    print("Autenticacao bem-sucedida.")
    print(response_com_auth.json())

print("\n=== RESUMO ===")
print("Session ajuda a reaproveitar conexoes e manter cookies.")
print("auth=(usuario, senha) e uma forma simples de autenticacao.")
