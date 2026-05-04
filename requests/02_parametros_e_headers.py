# request/02_parametros_e_headers.py

"""
Aula 2: Passando Parâmetros na URL e Enviando Cabeçalhos (Headers)

Muitas vezes, precisamos enviar informações adicionais em uma requisição GET.
Isso é feito através de parâmetros na URL (query parameters) e cabeçalhos (headers).

- Parâmetros: Usados para filtrar, ordenar ou paginar resultados.
  Ex: `https://api.example.com/search?query=python&page=2`
  Aqui, `query` e `page` são os parâmetros.

- Cabeçalhos (Headers): Usados para enviar metadados sobre a requisição, como
  o tipo de conteúdo que esperamos receber ou informações de autenticação.

Para executar este arquivo:
python request/02_parametros_e_headers.py
"""

import requests

# --- Passando Parâmetros (Query Parameters) ---

print("--- Requisição com Parâmetros ---")

# URL base da API de busca de piadas.
url_busca = "https://icanhazdadjoke.com/search"

# Em vez de montar a URL manualmente, podemos passar os parâmetros
# como um dicionário para o argumento `params` da função `get`.
# A biblioteca `requests` cuidará de formatar a URL corretamente.
parametros = {
    "term": "cat",  # O termo que queremos buscar.
    "limit": 3      # Limitar a 3 resultados.
}

# A requisição será feita para a URL: https://icanhazdadjoke.com/search?term=cat&limit=3
response_params = requests.get(url_busca, params=parametros)

# A API `icanhazdadjoke` espera um cabeçalho específico para retornar JSON.
# Vamos ver como fazer isso a seguir.

# --- Enviando Cabeçalhos (Headers) ---

print("\n--- Requisição com Cabeçalhos ---")

# Cabeçalhos também são passados como um dicionário, mas para o argumento `headers`.
# O `User-Agent` identifica quem está fazendo a requisição (neste caso, nosso script).
# O `Accept` informa ao servidor qual formato de dados preferimos receber.
cabecalhos = {
    "User-Agent": "Meu App de Estudo (https://github.com/usuario/meu-repo)",
    "Accept": "application/json"
}

# Fazemos a mesma requisição de antes, mas agora incluindo os cabeçalhos.
response_headers = requests.get(url_busca, params=parametros, headers=cabecalhos)

print(f"URL final da requisição: {response_headers.url}")
print(f"Status Code: {response_headers.status_code}")

# Agora, a resposta virá em JSON, como solicitado no cabeçalho 'Accept'.
dados_json = response_headers.json()

print("\nResultados da busca por piadas:")
for piada in dados_json["results"]:
    print(f"- {piada['joke']}")

print("\nFim da Aula 2. Tente mudar o termo da busca ou os parâmetros!")