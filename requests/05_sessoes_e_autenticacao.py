# request/05_sessoes_e_autenticacao.py

"""
Aula 5: Sessões e Autenticação

Sessões (Sessions):
Um objeto de Sessão permite persistir certos parâmetros entre requisições.
Por exemplo, se você fizer login em um site, a sessão manterá seus cookies
de autenticação para as próximas requisições, sem que você precise enviá-los
manualmente toda vez. Também otimiza conexões, sendo mais eficiente.

Autenticação:
Muitas APIs exigem autenticação para serem acessadas. A `requests` suporta
vários esquemas de autenticação, sendo o mais simples o "Basic Auth".

Para executar este arquivo:
python request/05_sessoes_e_autenticacao.py
"""

import requests

# --- Usando um Objeto de Sessão ---

print("--- Demonstração de Sessão ---")

# 1. Criamos uma instância de `Session`.
with requests.Session() as s:
    # A primeira requisição para httpbin.org/cookies/set define um cookie.
    # O nome do cookie é 'nome_cookie' e o valor é 'valor_cookie'.
    s.get('https://httpbin.org/cookies/set/nome_cookie/valor_cookie')

    # 2. Fazemos uma segunda requisição usando a mesma sessão.
    # A sessão automaticamente envia o cookie que foi definido na requisição anterior.
    response_cookies = s.get('https://httpbin.org/cookies')

    print("Cookies recebidos pelo servidor na segunda requisição:")
    # O httpbin.org retorna os cookies que ele recebeu de nós.
    print(response_cookies.json())

# O `with` garante que a sessão seja fechada corretamente no final.


# --- Autenticação Básica (Basic Auth) ---

print("\n--- Demonstração de Autenticação Básica ---")

# Este endpoint é protegido por autenticação. O usuário é 'user' e a senha é 'pass'.
url_auth = "https://httpbin.org/basic-auth/user/pass"

# Tentativa sem autenticação (vai falhar com status 401 Unauthorized)
response_sem_auth = requests.get(url_auth)
print(f"Tentativa sem autenticação - Status: {response_sem_auth.status_code}")

# Tentativa com autenticação correta
# A `requests` facilita a autenticação básica com o argumento `auth`.
# Basta passar uma tupla com (usuário, senha).
try:
    response_com_auth = requests.get(url_auth, auth=('user', 'pass'))

    print(f"Tentativa com autenticação - Status: {response_com_auth.status_code}")

    # Se o status for 200, a autenticação foi bem-sucedida.
    if response_com_auth.status_code == 200:
        print("Autenticação bem-sucedida!")
        print(response_com_auth.json())

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro: {e}")

print("\nFim da Aula 5. Sessões são essenciais para interagir com APIs que exigem login.")