# requests/15_formatos_e_content_types_na_pratica.py

"""
Aula 15: formatos e Content-Type na pratica

Objetivo:
- comparar JSON, XML, HTML e texto puro
- entender o que pedir no `Accept`
- conferir o `Content-Type` devolvido pelo servidor
- estudar formatos com olhar mais profissional

Execute com:
python requests/15_formatos_e_content_types_na_pratica.py
"""

import requests


def analisar_resposta(nome, url, accept, motivo):
    print("\n" + "=" * 60)
    print(f"FORMATO: {nome}")
    print("=" * 60)
    print(f"URL: {url}")
    print(f"Accept enviado: {accept}")
    print(f"Por que esse formato existe: {motivo}")

    response = requests.get(url, headers={"Accept": accept}, timeout=10)

    print(f"Status code: {response.status_code}")
    print(f"Content-Type devolvido: {response.headers.get('Content-Type')}")
    print(f"Tamanho do corpo em caracteres: {len(response.text)}")
    print(f"Amostra da resposta: {response.text[:120]!r}")


formatos = [
    {
        "nome": "JSON",
        "url": "https://httpbin.org/json",
        "accept": "application/json",
        "motivo": "APIs modernas gostam de JSON porque ele vira dicionario e lista com facilidade no Python.",
    },
    {
        "nome": "XML",
        "url": "https://httpbin.org/xml",
        "accept": "application/xml",
        "motivo": "XML ainda aparece em integracoes com sistemas legados e ambientes corporativos.",
    },
    {
        "nome": "HTML",
        "url": "https://httpbin.org/html",
        "accept": "text/html",
        "motivo": "HTML representa paginas web e nao respostas tipicas de API JSON.",
    },
    {
        "nome": "Texto puro",
        "url": "https://httpbin.org/robots.txt",
        "accept": "text/plain",
        "motivo": "Texto puro aparece quando o servidor devolve uma mensagem simples sem estrutura de objeto.",
    },
]


print("=== AULA 15: FORMATOS NA PRATICA ===")
print("Esta aula existe para mostrar que JSON e muito comum,")
print("mas nao e o unico formato do mundo real.")

for formato in formatos:
    analisar_resposta(
        nome=formato["nome"],
        url=formato["url"],
        accept=formato["accept"],
        motivo=formato["motivo"],
    )

print("\n=== RESUMO FINAL ===")
print("`Accept` mostra sua preferencia de formato.")
print("`Content-Type` mostra o formato real da resposta.")
print("Em estudo profissional, voce precisa saber reconhecer mais de um formato.")
