# fastapi/aula06_status_code_validacao_e_erros.py

"""
Aula 6: Status code, validacao e tratamento de erros

Aqui o foco e aprender a devolver respostas mais corretas e previsiveis.

Execute com:
uvicorn aula06_status_code_validacao_e_erros:app --reload
"""

from typing import Optional

from fastapi import FastAPI, HTTPException, Path, Query, status


app = FastAPI(title="Aula 06 - Validacao e erros")


pedidos = {
    1: {"cliente": "Ana", "valor": 120.0},
    2: {"cliente": "Bruno", "valor": 89.9},
}


@app.get("/pedidos/{pedido_id}")
def buscar_pedido(
    pedido_id: int = Path(gt=0, description="O ID precisa ser maior que zero."),
):
    pedido = pedidos.get(pedido_id)

    if not pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pedido nao encontrado.",
        )

    return pedido


@app.get("/relatorios")
def gerar_relatorio(
    pagina: int = Query(default=1, ge=1),
    limite: int = Query(default=10, ge=1, le=50),
    filtro: Optional[str] = Query(default=None, min_length=3),
):
    return {
        "pagina": pagina,
        "limite": limite,
        "filtro": filtro,
    }


@app.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login(usuario: str, senha: str):
    if usuario != "admin" or senha != "1234":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais invalidas.",
        )

    return {"mensagem": "Login aceito para processamento."}


if __name__ == "__main__":
    print("Execute com: uvicorn aula06_status_code_validacao_e_erros:app --reload")
