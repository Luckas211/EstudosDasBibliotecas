# fastapi/aula02_rotas_e_path_params.py

"""
Aula 2: Rotas e parametros de caminho

Nesta aula voce vai entender como o valor da URL pode virar argumento da funcao.

Execute com:
uvicorn aula02_rotas_e_path_params:app --reload
"""

from fastapi import FastAPI, HTTPException


app = FastAPI(title="Aula 02 - Rotas e path params")


produtos = {
    1: {"nome": "Notebook", "preco": 3500.0},
    2: {"nome": "Mouse", "preco": 120.0},
    3: {"nome": "Teclado", "preco": 250.0},
}


@app.get("/")
def inicio():
    return {"mensagem": "Use /produtos ou /produtos/1 para testar os endpoints."}


@app.get("/produtos")
def listar_produtos():
    return produtos


@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    produto = produtos.get(produto_id)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto nao encontrado.")

    return {"id": produto_id, "dados": produto}


@app.get("/tabuada/{numero}")
def tabuada(numero: int):
    resultado = []

    for multiplicador in range(1, 11):
        resultado.append(f"{numero} x {multiplicador} = {numero * multiplicador}")

    return {"numero": numero, "tabuada": resultado}


if __name__ == "__main__":
    print("Execute com: uvicorn aula02_rotas_e_path_params:app --reload")
