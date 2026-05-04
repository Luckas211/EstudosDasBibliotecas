# fastapi/aula07_response_model_e_documentacao.py

"""
Aula 7: Response model e documentacao automatica

Response model ajuda a controlar o que sai da sua API.
Isso e util para esconder campos internos e organizar melhor a documentacao.

Execute com:
uvicorn aula07_response_model_e_documentacao:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Aula 07 - Response model")


class PerfilPublico(BaseModel):
    nome: str
    area: str
    nivel: str


class PerfilInterno(BaseModel):
    nome: str
    area: str
    nivel: str
    senha: str


@app.get(
    "/perfil",
    response_model=PerfilPublico,
    tags=["Perfil"],
    summary="Retorna apenas os dados publicos do perfil",
)
def ler_perfil():
    perfil = PerfilInterno(
        nome="Maria",
        area="Back-end",
        nivel="junior",
        senha="segredo123",
    )
    return perfil


@app.get("/health", tags=["Infra"])
def healthcheck():
    return {"status": "ok"}


if __name__ == "__main__":
    print("Execute com: uvicorn aula07_response_model_e_documentacao:app --reload")
