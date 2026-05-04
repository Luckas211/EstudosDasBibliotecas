# fastapi/aula04_body_e_pydantic.py

"""
Aula 4: Body da requisicao e modelos com Pydantic

Agora vamos receber dados enviados no corpo da requisicao.
O FastAPI usa modelos Pydantic para validar automaticamente os campos.

Execute com:
uvicorn aula04_body_e_pydantic:app --reload
"""

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Aula 04 - Body e Pydantic")


class Aluno(BaseModel):
    nome: str
    email: str
    idade: int
    ativo: bool = True
    curso: Optional[str] = None


class Produto(BaseModel):
    nome: str
    preco: float = Field(gt=0, description="Preco deve ser maior que zero.")
    estoque: int = Field(ge=0, description="Estoque nao pode ser negativo.")


@app.post("/alunos")
def criar_aluno(aluno: Aluno):
    return {
        "mensagem": "Aluno recebido com sucesso.",
        "dados": aluno.model_dump(),
    }


@app.post("/produtos")
def criar_produto(produto: Produto):
    return {
        "mensagem": "Produto validado com sucesso.",
        "dados": produto.model_dump(),
    }


if __name__ == "__main__":
    print("Execute com: uvicorn aula04_body_e_pydantic:app --reload")
