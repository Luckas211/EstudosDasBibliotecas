# Modulo: FastAPI

`FastAPI` e um framework moderno para criar APIs em Python.
Ele ajuda voce a construir rotas web, validar dados, documentar endpoints
automaticamente e montar backends de forma organizada.

## O que voce vai aprender

- criar sua primeira API
- entender rotas e metodos HTTP
- receber dados por path params e query params
- validar dados com Pydantic
- montar um CRUD em memoria
- usar status HTTP e tratar erros com `HTTPException`
- documentar melhor respostas e testar sua API com `requests`

## Antes de estudar este modulo

Instale as dependencias:

```bash
pip install fastapi uvicorn requests
```

## Como executar as aulas

Como esta pasta se chama `fastapi`, a forma mais segura e abrir o terminal
dentro dela antes de subir o servidor.

Exemplo:

```bash
cd fastapi
uvicorn aula01_introducao_e_primeira_api:app --reload
```

Depois, abra:

- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Ordem sugerida

1. `aula01_introducao_e_primeira_api.py`
2. `aula02_rotas_e_path_params.py`
3. `aula03_query_params_e_filtros.py`
4. `aula04_body_e_pydantic.py`
5. `aula05_crud_em_memoria.py`
6. `aula06_status_code_validacao_e_erros.py`
7. `aula07_response_model_e_documentacao.py`
8. `cliente_tarefas_com_requests.py`
9. `desafio_final_api_de_tarefas.py`
10. `guia_de_estudos.md`

## Como estudar melhor

1. Suba uma aula por vez com `uvicorn`.
2. Teste no navegador e no `/docs`.
3. Mude os dados manualmente.
4. Repare no que o FastAPI valida sozinho.
5. Teste respostas corretas e incorretas.

## Resultado esperado ao final

Voce deve sair deste modulo conseguindo criar uma API simples do zero,
entender o fluxo de requisicao e resposta e consumir a propria API com `requests`.
