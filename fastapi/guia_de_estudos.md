# Guia de estudos: FastAPI

Este guia ajuda voce a estudar `FastAPI` com mais intencao e menos pressa.

## Meta do modulo

Ao final, voce deve conseguir:

- criar endpoints simples
- entender como a URL conversa com os argumentos da funcao
- validar dados recebidos com Pydantic
- usar `GET`, `POST`, `PUT` e `DELETE`
- construir uma API pequena e testar com `requests`

## Rotina recomendada

1. Suba apenas uma aula por vez.
2. Leia o codigo inteiro antes de testar.
3. Teste pelo navegador e pelo `/docs`.
4. Force erros de proposito para ver a validacao.
5. Reescreva uma rota sem copiar.

## Checklist por aula

### Aula 1

- entender o que e uma rota
- abrir `/docs`
- observar que a resposta ja sai em JSON

### Aula 2

- testar valores diferentes na URL
- provocar um `404`
- entender por que o parametro virou `int`

### Aula 3

- filtrar cursos por `nivel`
- testar `gratuito=true`
- mudar o `limite`

### Aula 4

- enviar JSON valido
- enviar JSON invalido
- observar as mensagens automáticas de erro

### Aula 5

- criar varias tarefas
- atualizar uma delas
- remover outra

## Perguntas de revisao

- O que diferencia path param de query param?
- O que o Pydantic faz por voce?
- Quando usar `HTTPException`?
- O que significa `status_code=201`?
- Para que serve o `response_model`?

## Mini projetos sugeridos

- API de livros
- API de filmes
- API de tarefas
- API de contatos
- API para registrar habitos de estudo

## Ponte com o modulo requests

Depois da aula 5, rode `cliente_tarefas_com_requests.py`.
Esse arquivo mostra algo muito importante: agora voce nao esta apenas consumindo APIs,
voce tambem esta criando uma API para ser consumida.
