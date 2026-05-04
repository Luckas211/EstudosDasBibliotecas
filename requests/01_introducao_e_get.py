# request/01_introducao_e_get.py

"""
Aula 1: Introdução à Biblioteca Requests e Requisições GET

A biblioteca `requests` é o padrão de fato em Python para fazer requisições HTTP.
Ela simplifica o trabalho com APIs web, download de conteúdo e interação com serviços online.

Nesta aula, vamos aprender o básico: como fazer uma requisição GET, que é a operação
mais comum na web, usada para solicitar dados de um servidor.

Para executar este arquivo:
1. Certifique-se de ter a biblioteca instalada: pip install requests
2. Execute o comando: python request/01_introducao_e_get.py
"""

# Importa a biblioteca requests para que possamos usá-la.
import requests

# --- Fazendo uma Requisição GET Simples ---

# Uma URL (Uniform Resource Locator) é o endereço de um recurso na web.
# Usaremos a API 'httpbin.org', que é ótima para testar requisições.
url = "https://httpbin.org/get"

print(f"Fazendo uma requisição GET para: {url}")

# `requests.get(url)` envia uma requisição HTTP do tipo GET para a URL especificada.
# O resultado é um objeto de Resposta (Response), que armazenamos na variável `response`.
response = requests.get(url)

# --- Analisando a Resposta (Response) ---

print("\n--- Análise da Resposta ---")

# O atributo `status_code` nos diz o resultado da requisição.
# Códigos 2xx (como 200) indicam sucesso.
# Códigos 4xx (como 404) indicam erro do cliente (ex: página não encontrada).
# Códigos 5xx indicam erro do servidor.
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    print("A requisição foi bem-sucedida!")
else:
    print("A requisição falhou.")

# O atributo `headers` é um dicionário com os cabeçalhos da resposta HTTP.
# Contém metadados como o tipo de conteúdo (Content-Type), data, etc.
print(f"Tipo de Conteúdo (Content-Type): {response.headers['Content-Type']}")

# --- Acessando o Conteúdo da Resposta ---

print("\n--- Conteúdo da Resposta ---")

# O atributo `.text` retorna o conteúdo da resposta como uma string (texto puro).
# É útil para HTML, texto simples, etc.
# print("\nConteúdo como texto:")
# print(response.text)

# O método `.json()` converte uma resposta JSON (formato muito comum em APIs)
# em um dicionário Python, o que facilita muito o acesso aos dados.
print("\nConteúdo como JSON (dicionário Python):")
dados_json = response.json()
print(dados_json)

# Acessando um dado específico dentro do JSON.
print(f"\nA URL de origem da requisição foi: {dados_json['origin']}")

print("\nFim da Aula 1. Experimente trocar a URL por outra API, como 'https://api.github.com'.")