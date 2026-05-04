# fastapi/desafio_final_api_de_tarefas.py

"""
DESAFIO FINAL: API DE TAREFAS COM FASTAPI

Objetivo:
Criar uma API de tarefas com rotas para listar, criar, atualizar e remover itens.

Requisitos minimos:
1. Criar uma rota `GET /tarefas`
2. Criar uma rota `GET /tarefas/{id}`
3. Criar uma rota `POST /tarefas`
4. Criar uma rota `PUT /tarefas/{id}`
5. Criar uma rota `DELETE /tarefas/{id}`
6. Usar pelo menos um modelo Pydantic
7. Tratar caso de tarefa nao encontrada com `HTTPException`

Desafios extras:
- adicionar filtro por `concluida=true`
- validar tamanho minimo do titulo
- devolver `status_code=201` no POST
- testar a API usando `requests`
- persistir dados em arquivo JSON
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Desafio final - API de tarefas")


class Tarefa(BaseModel):
    titulo: str
    descricao: str
    concluida: bool = False


tarefas = []


@app.get("/tarefas")
def listar_tarefas():
    # TODO: retornar a lista de tarefas
    return tarefas


@app.get("/tarefas/{tarefa_id}")
def detalhar_tarefa(tarefa_id: int):
    # TODO: buscar uma tarefa pelo ID
    raise HTTPException(status_code=501, detail="Implemente esta rota.")


@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    # TODO: adicionar a nova tarefa em memoria
    return tarefa


@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa: Tarefa):
    # TODO: atualizar uma tarefa existente
    raise HTTPException(status_code=501, detail="Implemente esta rota.")


@app.delete("/tarefas/{tarefa_id}")
def remover_tarefa(tarefa_id: int):
    # TODO: remover a tarefa da lista
    raise HTTPException(status_code=501, detail="Implemente esta rota.")


if __name__ == "__main__":
    print("Execute com: uvicorn desafio_final_api_de_tarefas:app --reload")
