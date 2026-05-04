# requests/07_consumindo_apis_reais.py

"""
Aula 7: Consumindo APIs reais

Agora vamos sair dos exemplos de teste e conversar com APIs publicas
que se parecem mais com situacoes do dia a dia.

Nesta aula, vamos usar:
- ViaCEP: para consultar endereco a partir do CEP
- JSONPlaceholder: para ler posts falsos de uma API de testes

Para executar este arquivo:
python requests/07_consumindo_apis_reais.py
"""

import requests


def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    dados = response.json()

    if dados.get("erro"):
        print("CEP nao encontrado.")
        return

    print("\n--- Resultado do CEP ---")
    print(f"CEP: {dados['cep']}")
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"UF: {dados['uf']}")


def listar_posts_usuario(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    parametros = {"userId": user_id}
    response = requests.get(url, params=parametros, timeout=10)
    response.raise_for_status()
    posts = response.json()

    print(f"\n--- Posts do usuario {user_id} ---")
    for post in posts[:3]:
        print(f"ID: {post['id']} | Titulo: {post['title']}")


consultar_cep("01001000")
listar_posts_usuario(1)

print("\nFim da aula 7. Tente trocar o CEP ou o userId para explorar novas respostas.")
