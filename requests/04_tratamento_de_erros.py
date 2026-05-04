# request/04_tratamento_de_erros.py

"""
Aula 4: Tratamento de Erros e Exceções

Ao trabalhar com redes, muitas coisas podem dar errado:
- O servidor pode estar offline.
- A sua conexão com a internet pode cair.
- A URL pode estar errada (erro 404).
- Você pode não ter permissão para acessar um recurso (erro 403).

Um bom código deve prever e tratar esses erros de forma elegante,
em vez de simplesmente quebrar.

Para executar este arquivo:
python request/04_tratamento_de_erros.py
"""

import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError

# --- Tratando Erros de Conexão e Timeout ---

print("--- Tentando conectar a uma URL inválida ---")

# Uma URL que não existe ou está offline.
url_invalida = "https://endereco.que.nao.existe.com"

try:
    # Usamos um bloco `try...except` para capturar possíveis erros.
    # O argumento `timeout` define quantos segundos a `requests` deve esperar
    # por uma resposta antes de desistir.
    response = requests.get(url_invalida, timeout=5)

except ConnectionError as e:
    # Este bloco é executado se houver um problema de rede
    # (ex: DNS não encontrado, servidor recusou conexão).
    print(f"Erro de conexão: Não foi possível conectar à URL. Detalhes: {e}")

except Timeout:
    # Este bloco é executado se o servidor demorar mais que o `timeout` para responder.
    print("Erro de Timeout: O servidor demorou muito para responder.")


# --- Verificando Códigos de Status de Erro (4xx e 5xx) ---

print("\n--- Tentando acessar uma página que não existe (Erro 404) ---")

url_404 = "https://httpbin.org/status/404"

try:
    response_erro = requests.get(url_404)
    print(f"Status Code recebido: {response_erro.status_code}")

    # O método `raise_for_status()` verifica se o status code é um erro (4xx ou 5xx).
    # Se for, ele levanta uma exceção do tipo `HTTPError`.
    # Se o status for de sucesso (2xx), ele não faz nada.
    response_erro.raise_for_status()

except HTTPError as e:
    # Capturamos a exceção levantada por `raise_for_status()`.
    print(f"Erro HTTP: O servidor retornou um status de erro. Detalhes: {e}")

print("\nFim da Aula 4. Sempre use `try...except` ao fazer requisições de rede!")