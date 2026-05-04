# fastapi/aula03_query_params_e_filtros.py

"""
Aula 3: Query params e filtros

Query params sao os valores enviados depois do `?` na URL.
Exemplo:
/cursos?nivel=iniciante&limite=2

Execute com:
uvicorn aula03_query_params_e_filtros:app --reload
"""

from typing import Optional

from fastapi import FastAPI


app = FastAPI(title="Aula 03 - Query params")


cursos = [
    {"id": 1, "nome": "Python", "nivel": "iniciante", "gratuito": True},
    {"id": 2, "nome": "APIs com requests", "nivel": "iniciante", "gratuito": True},
    {"id": 3, "nome": "FastAPI", "nivel": "intermediario", "gratuito": True},
    {"id": 4, "nome": "SQL", "nivel": "intermediario", "gratuito": False},
]


@app.get("/cursos")
def listar_cursos(
    nivel: Optional[str] = None,
    gratuito: Optional[bool] = None,
    limite: int = 10,
):
    resultado = cursos

    if nivel is not None:
        resultado = [curso for curso in resultado if curso["nivel"] == nivel]

    if gratuito is not None:
        resultado = [curso for curso in resultado if curso["gratuito"] == gratuito]

    return resultado[:limite]


@app.get("/busca")
def busca_rapida(termo: str = "", pagina: int = 1):
    return {
        "termo_recebido": termo,
        "pagina": pagina,
        "mensagem": "Use este endpoint para observar como query params chegam na funcao.",
    }


if __name__ == "__main__":
    print("Execute com: uvicorn aula03_query_params_e_filtros:app --reload")
