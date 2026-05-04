# requests/09_projeto_guiado_consultor_web.py

"""
Projeto guiado: Consultor web no terminal

Objetivo:
Criar um pequeno programa de linha de comando que usa varias APIs para:
- consultar um CEP
- ler um post de exemplo
- buscar uma piada por termo

Este arquivo junta varios conceitos do modulo:
- funcoes
- requests.get()
- params
- headers
- tratamento de erros
- organizacao de codigo

Para executar:
python requests/09_projeto_guiado_consultor_web.py
"""

import requests
from requests.exceptions import RequestException


HEADERS_PIADA = {
    "Accept": "application/json",
    "User-Agent": "Manual-das-bibliotecas-em-Python",
}


def buscar_json(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except RequestException as erro:
        print(f"Erro ao acessar a API: {erro}")
        return None


def consultar_cep():
    cep = input("Digite o CEP (somente numeros): ").strip()
    dados = buscar_json(f"https://viacep.com.br/ws/{cep}/json/")

    if not dados or dados.get("erro"):
        print("CEP nao encontrado.")
        return

    print("\nEndereco encontrado:")
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"UF: {dados['uf']}")


def consultar_post():
    post_id = input("Digite o ID do post (1 a 100): ").strip()
    dados = buscar_json(f"https://jsonplaceholder.typicode.com/posts/{post_id}")

    if not dados:
        return

    print("\nPost encontrado:")
    print(f"Titulo: {dados['title']}")
    print(f"Conteudo: {dados['body']}")


def buscar_piada():
    termo = input("Digite um termo em ingles para buscar piadas: ").strip()
    dados = buscar_json(
        "https://icanhazdadjoke.com/search",
        params={"term": termo, "limit": 1},
        headers=HEADERS_PIADA,
    )

    if not dados:
        return

    resultados = dados.get("results", [])
    if not resultados:
        print("Nenhuma piada encontrada.")
        return

    print("\nPiada encontrada:")
    print(resultados[0]["joke"])


def menu():
    while True:
        print("\n" + "=" * 40)
        print("CONSULTOR WEB")
        print("=" * 40)
        print("1. Consultar CEP")
        print("2. Ler post de exemplo")
        print("3. Buscar piada")
        print("4. Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            consultar_cep()
        elif opcao == "2":
            consultar_post()
        elif opcao == "3":
            buscar_piada()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    menu()
