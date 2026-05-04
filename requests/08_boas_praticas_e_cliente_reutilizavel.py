# requests/08_boas_praticas_e_cliente_reutilizavel.py

"""
Aula 8: Boas praticas e funcoes reutilizaveis

Quando seu codigo cresce, nao vale a pena repetir `requests.get()`
do mesmo jeito em todo lugar. O ideal e criar funcoes pequenas,
com timeout, tratamento de erro e retorno previsivel.

Nesta aula, vamos montar um mini cliente HTTP reutilizavel.

Para executar este arquivo:
python requests/08_boas_praticas_e_cliente_reutilizavel.py
"""

import time

import requests
from requests.exceptions import RequestException


def fazer_get_json(url, params=None, tentativas=3, timeout=10, headers=None):
    for tentativa in range(1, tentativas + 1):
        try:
            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=timeout,
            )
            response.raise_for_status()
            return response.json()

        except RequestException as erro:
            print(f"Tentativa {tentativa} falhou: {erro}")

            if tentativa == tentativas:
                print("Numero maximo de tentativas atingido.")
                return None

            print("Aguardando 2 segundos antes de tentar novamente...")
            time.sleep(2)


def buscar_piada(termo):
    url = "https://icanhazdadjoke.com/search"
    headers = {
        "Accept": "application/json",
        "User-Agent": "Manual-das-bibliotecas-em-Python",
    }
    params = {"term": termo, "limit": 1}

    dados = fazer_get_json(url, params=params, headers=headers)
    if not dados:
        return

    resultados = dados.get("results", [])
    if not resultados:
        print("Nenhuma piada encontrada para esse termo.")
        return

    print("\nPiada encontrada:")
    print(resultados[0]["joke"])


def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    dados = fazer_get_json(url)

    if not dados or dados.get("erro"):
        print("Nao foi possivel localizar esse CEP.")
        return

    print("\nEndereco encontrado:")
    print(f"{dados['logradouro']} - {dados['bairro']} - {dados['localidade']}/{dados['uf']}")


buscar_piada("python")
buscar_endereco("01001000")

print("\nBoas praticas reforcadas nesta aula:")
print("- sempre usar timeout")
print("- concentrar tratamento de erro em funcoes reutilizaveis")
print("- validar se a API devolveu os campos esperados")
print("- evitar repeticao de codigo")
