# requests/02_parametros_e_headers.py

"""
Aula 2: parametros e headers com explicacao detalhada

Objetivo desta aula:
- entender o que colocar dentro de `params={}`
- entender o que colocar dentro de `headers={}`
- conhecer opcoes reais de `Accept`
- entender por que JSON nao e o unico formato possivel
- ver como a URL final fica montada
- enxergar como o servidor recebe o que enviamos

Execute com:
python requests/02_parametros_e_headers.py
"""

import requests

print("=== AULA 2: PARAMS E HEADERS ===")

# Vamos usar o httpbin porque ele devolve exatamente o que recebeu.
url = "https://httpbin.org/get"

# `{}` cria um dicionario.
# Dentro do dicionario, cada item tem:
# - uma chave
# - `:`
# - um valor
# - `,` separando os itens
#
# `params` serve para montar a parte da URL depois do `?`
parametros = {
    "curso": "requests",
    "nivel": "basico",
    "pagina": 2,
}

# `headers` tambem recebe um dicionario.
# Aqui voce manda metadados da requisicao.
cabecalhos = {
    "Accept": "application/json",
    "User-Agent": "ManualDeEstudosRequests/1.0",
}

print(f"URL base: {url}")
print(f"Parametros enviados: {parametros}")
print(f"Headers enviados: {cabecalhos}")

# Leia esta linha assim:
# - `params=parametros` manda um dicionario que vira query string
# - `headers=cabecalhos` manda os cabecalhos HTTP
# - `timeout=10` limita o tempo de espera
response = requests.get(
    url,
    params=parametros,
    headers=cabecalhos,
    timeout=10,
)

print("\n=== O QUE A REQUESTS MONTOU ===")

# `.url` mostra a URL final, ja com os query params.
print(f"URL final: {response.url}")
print(f"Status code: {response.status_code}")

dados = response.json()

print("\n=== O QUE O SERVIDOR RECEBEU ===")

# `dados["args"]` mostra os query params recebidos.
print("Args recebidos pelo servidor:")
print(dados["args"])

# `dados["headers"]` mostra varios headers vistos pelo servidor.
print("\nAlguns headers recebidos pelo servidor:")
print(f"Accept: {dados['headers'].get('Accept')}")
print(f"User-Agent: {dados['headers'].get('User-Agent')}")

print("\n=== COMO LER OS SIMBOLOS ===")
print("parametros['curso'] -> pega o valor da chave 'curso'")
print("dados['args']['pagina'] -> pega 'pagina' dentro de 'args'")

# `str(...)` converte o valor para texto para facilitar esta comparacao.
print(f"Valor recebido para pagina: {dados['args']['pagina']}")

print("\n=== QUANDO USAR ===")
print("Use params para filtros, busca, paginacao e ordenacao.")
print("Use headers para metadados, autenticacao e formato esperado.")

print("\n=== HEADERS COMUNS EM ESTUDO PROFISSIONAL ===")
print("Accept -> formato que eu prefiro receber")
print("User-Agent -> identifica meu sistema")
print("Authorization -> envia token ou credencial")
print("Content-Type -> informa o formato do corpo enviado")

print("\n=== EXEMPLOS REAIS DE Accept ===")

tipos_de_resposta = [
    {
        "nome": "JSON",
        "url": "https://httpbin.org/json",
        "accept": "application/json",
        "por_que_usar": "APIs modernas costumam responder em JSON.",
    },
    {
        "nome": "XML",
        "url": "https://httpbin.org/xml",
        "accept": "application/xml",
        "por_que_usar": "Alguns sistemas legados e integracoes corporativas usam XML.",
    },
    {
        "nome": "HTML",
        "url": "https://httpbin.org/html",
        "accept": "text/html",
        "por_que_usar": "Paginas web normalmente devolvem HTML.",
    },
    {
        "nome": "Texto puro",
        "url": "https://httpbin.org/robots.txt",
        "accept": "text/plain",
        "por_que_usar": "Alguns endpoints devolvem mensagens ou textos simples.",
    },
]

for exemplo in tipos_de_resposta:
    print(f"\n--- Exemplo: {exemplo['nome']} ---")
    print(f"Accept enviado: {exemplo['accept']}")
    print(f"Por que usar: {exemplo['por_que_usar']}")

    resposta_formato = requests.get(
        exemplo["url"],
        headers={"Accept": exemplo["accept"]},
        timeout=10,
    )

    print(
        "Content-Type devolvido pelo servidor: "
        f"{resposta_formato.headers.get('Content-Type')}"
    )
    print(f"Primeiros caracteres da resposta: {resposta_formato.text[:80]!r}")

print("\n=== REGRA PROFISSIONAL IMPORTANTE ===")
print("`Accept` diz o que voce prefere receber.")
print("`Content-Type` mostra o formato que realmente foi enviado ou recebido.")
print("Nem todo servidor vai obedecer exatamente o valor de `Accept`.")
