# fastapi/aula05_crud_em_memoria.py

"""
Aula 5: CRUD em memoria

Nesta aula voce vai montar uma API simples de tarefas sem banco de dados.
Os dados vao ficar em memoria enquanto o servidor estiver rodando.

Execute com:
uvicorn aula05_crud_em_memoria:app --reload
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI(title="Aula 05 - CRUD de tarefas")


class TarefaEntrada(BaseModel):
    titulo: str
    descricao: str
    concluida: bool = False


tarefas = [
    {
        "id": 1,
        "titulo": "Estudar requests",
        "descricao": "Revisar GET, POST e tratamento de erros",
        "concluida": False,
    }
]

proximo_id = 2


def buscar_tarefa_por_id(tarefa_id: int):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            return tarefa
    return None


@app.get("/tarefas")
def listar_tarefas():
    return tarefas


@app.get("/tarefas/{tarefa_id}")
def detalhar_tarefa(tarefa_id: int):
    tarefa = buscar_tarefa_por_id(tarefa_id)

    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada.")

    return tarefa


@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: TarefaEntrada):
    global proximo_id

    nova_tarefa = {"id": proximo_id, **tarefa.model_dump()}
    tarefas.append(nova_tarefa)
    proximo_id += 1

    return nova_tarefa


@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: TarefaEntrada):
    tarefa = buscar_tarefa_por_id(tarefa_id)

    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada.")

    tarefa.update(tarefa_atualizada.model_dump())
    return tarefa


@app.delete("/tarefas/{tarefa_id}")
def remover_tarefa(tarefa_id: int):
    tarefa = buscar_tarefa_por_id(tarefa_id)

    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada.")

    tarefas.remove(tarefa)
    return {"mensagem": "Tarefa removida com sucesso."}


if __name__ == "__main__":
    print("Execute com: uvicorn aula05_crud_em_memoria:app --reload")
