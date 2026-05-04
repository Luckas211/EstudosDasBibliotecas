# requests/desafio_final_cliente_de_apis.py

"""
DESAFIO FINAL: CLIENTE DE APIS NO TERMINAL

Objetivo:
Criar um programa de linha de comando que consome pelo menos duas APIs publicas
e organiza as respostas de forma clara para o usuario.

Requisitos minimos:
1. Ter um menu com pelo menos 3 opcoes.
2. Consumir pelo menos 2 APIs diferentes.
3. Tratar erros de conexao e status HTTP.
4. Usar pelo menos uma requisicao com `params`.
5. Organizar o codigo em funcoes.

Sugestoes de APIs:
- ViaCEP
- JSONPlaceholder
- icanhazdadjoke
- httpbin

Ideias de funcionalidades:
- consultar CEP
- buscar posts por usuario
- listar comentarios de um post
- buscar piadas por palavra
- testar status de uma URL

Desafios extras:
- adicionar cache simples em dicionario
- salvar uma resposta em arquivo `.json`
- permitir repeticao automatica de tentativas
- criar uma funcao generica para GET
"""

import requests


def buscar_json(url, params=None, headers=None):
    # TODO: implementar a logica de requisicao com timeout e tratamento de erro
    pass


def opcao_cep():
    # TODO: pedir um CEP ao usuario e mostrar o endereco
    pass


def opcao_posts():
    # TODO: pedir um userId e listar posts
    pass


def opcao_piada():
    # TODO: pedir um termo e buscar uma piada
    pass


def menu():
    while True:
        print("\n" + "=" * 40)
        print("DESAFIO FINAL - CLIENTE DE APIS")
        print("=" * 40)
        print("1. Consultar CEP")
        print("2. Listar posts")
        print("3. Buscar piada")
        print("4. Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            opcao_cep()
        elif opcao == "2":
            opcao_posts()
        elif opcao == "3":
            opcao_piada()
        elif opcao == "4":
            print("Fim do desafio.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    print("Complete os TODOs e depois descomente a linha abaixo para testar.")
    # menu()
