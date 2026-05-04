# fastapi/cliente_tarefas_com_requests.py

"""
Material de apoio: consumindo a API FastAPI com requests

Antes de executar este cliente:
1. Abra um terminal dentro da pasta `fastapi`
2. Rode: uvicorn aula05_crud_em_memoria:app --reload
3. Em outro terminal, execute este arquivo:
   python cliente_tarefas_com_requests.py
"""

import requests


BASE_URL = "http://127.0.0.1:8000"


def listar_tarefas():
    response = requests.get(f"{BASE_URL}/tarefas", timeout=10)
    response.raise_for_status()
    return response.json()


def criar_tarefa():
    payload = {
        "titulo": "Praticar FastAPI",
        "descricao": "Consumir uma API local com requests",
        "concluida": False,
    }
    response = requests.post(f"{BASE_URL}/tarefas", json=payload, timeout=10)
    response.raise_for_status()
    return response.json()


print("--- Criando uma nova tarefa na API ---")
print(criar_tarefa())

print("\n--- Listando tarefas da API ---")
for tarefa in listar_tarefas():
    print(tarefa)
