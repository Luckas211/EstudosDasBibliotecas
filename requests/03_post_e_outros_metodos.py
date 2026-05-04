# request/03_post_e_outros_metodos.py

"""
Aula 3: Requisições POST e Outros Métodos HTTP

Enquanto o GET é usado para *pedir* dados, o POST é usado para *enviar* dados
para um servidor, geralmente para criar um novo recurso (ex: cadastrar um usuário,
publicar um comentário).

Outros métodos comuns:
- PUT: Para atualizar um recurso existente completamente.
- PATCH: Para atualizar um recurso existente parcialmente.
- DELETE: Para remover um recurso.

Nesta aula, vamos focar no POST, que é o segundo método mais utilizado.

Para executar este arquivo:
python request/03_post_e_outros_metodos.py
"""

import requests

# Usaremos novamente o httpbin.org, que tem um endpoint específico para testar POST.
url_post = "https://httpbin.org/post"

# --- Enviando Dados como Formulário (x-www-form-urlencoded) ---

print("--- Requisição POST com dados de formulário ---")

# Criamos um dicionário com os dados que queremos enviar.
# Isso simula o envio de um formulário HTML.
dados_formulario = {
    "nome": "João Silva",
    "email": "joao.silva@example.com",
    "curso": "Python para Automação"
}

# Usamos `requests.post()` e passamos nosso dicionário para o argumento `data`.
response_form = requests.post(url_post, data=dados_formulario)

print(f"Status Code: {response_form.status_code}")

# O httpbin retorna um JSON com os dados que ele recebeu.
dados_resposta_form = response_form.json()

# A chave 'form' na resposta conterá os dados que enviamos.
print("Dados recebidos pelo servidor (formulário):")
print(dados_resposta_form['form'])


# --- Enviando Dados como JSON ---

print("\n--- Requisição POST com dados JSON ---")

# Em APIs modernas, é mais comum enviar dados diretamente no formato JSON.
dados_json_payload = {
    "id_produto": 12345,
    "quantidade": 2,
    "opcoes": {"cor": "azul", "tamanho": "M"}
}

# Para isso, usamos o argumento `json` em vez de `data`.
# A biblioteca `requests` automaticamente define o cabeçalho 'Content-Type' para 'application/json'.
response_json = requests.post(url_post, json=dados_json_payload)

dados_resposta_json = response_json.json()

# A chave 'json' na resposta conterá o payload JSON que enviamos.
print("Dados recebidos pelo servidor (JSON):")
print(dados_resposta_json['json'])

print("\nFim da Aula 3. Os métodos `requests.put()`, `requests.delete()`, etc., funcionam de forma similar.")