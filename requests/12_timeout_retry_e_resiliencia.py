# requests/12_timeout_retry_e_resiliencia.py

"""
Aula 12: timeout, tentativas e resiliencia

Objetivo:
- criar uma funcao mais robusta
- repetir a tentativa em caso de falha
- concentrar tratamento de erro em um lugar

Execute com:
python requests/12_timeout_retry_e_resiliencia.py
"""

import time

import requests
from requests.exceptions import RequestException


def get_com_tentativas(url, tentativas=3, timeout=5):
    for tentativa in range(1, tentativas + 1):
        try:
            print(f"Tentativa {tentativa} de {tentativas}")
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response

        except RequestException as erro:
            print(f"Falha: {erro}")

            if tentativa == tentativas:
                print("Numero maximo de tentativas atingido.")
                return None

            print("Esperando 2 segundos antes de tentar novamente...")
            time.sleep(2)


url = "https://httpbin.org/get"
response = get_com_tentativas(url)

print("\n=== AULA 12: RESILIENCIA ===")

if response is not None:
    print(f"Status final: {response.status_code}")
    print(response.json())
else:
    print("Nao foi possivel concluir a requisicao.")

print("\n=== IDEIA PRINCIPAL ===")
print("Uma funcao centralizada reduz repeticao e melhora manutencao.")
