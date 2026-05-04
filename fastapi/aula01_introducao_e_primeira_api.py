# fastapi/aula01_introducao_e_primeira_api.py

"""
Aula 1: Introducao ao FastAPI e primeira API

Para executar:
1. Abra o terminal dentro da pasta `fastapi`
2. Rode: uvicorn aula01_introducao_e_primeira_api:app --reload
3. Abra: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI


app = FastAPI(
    title="Aula 01 - Minha primeira API",
    description="Exemplo inicial para entender rotas e respostas JSON.",
)


@app.get("/")
def pagina_inicial():
    return {"mensagem": "Bem-vindo ao estudo de FastAPI!"}


@app.get("/saudacao")
def saudacao():
    return {
        "mensagem": "O FastAPI converte dicionarios Python em JSON automaticamente."
    }


@app.get("/sobre")
def sobre():
    return {
        "biblioteca": "FastAPI",
        "tipo": "Framework para criar APIs",
        "proximo_passo": "Abrir /docs para explorar a documentacao automatica",
    }


if __name__ == "__main__":
    print("Execute com: uvicorn aula01_introducao_e_primeira_api:app --reload")
