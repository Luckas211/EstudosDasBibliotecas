# Material 02: HTTP, JSON e API sem misterio

## O que e HTTP

HTTP e a linguagem basica da web.
Quando seu navegador abre um site ou quando seu script usa `requests`,
existe uma conversa entre cliente e servidor.

## O que e cliente

Cliente e quem pede algo.

Exemplos:

- navegador
- aplicativo no celular
- script Python com `requests`

## O que e servidor

Servidor e quem recebe o pedido e devolve uma resposta.

Exemplos:

- site
- API
- sistema online

## O que e uma requisicao

Requisicao e o pedido enviado pelo cliente.

Ela costuma ter:

- metodo
- URL
- headers
- parametros
- body

## O que e uma resposta

Resposta e o retorno do servidor.

Ela costuma ter:

- status code
- headers
- body

## Metodos HTTP mais comuns

### GET

Usado para buscar dados.

Exemplo mental:
"servidor, me mostre os dados"

### POST

Usado para enviar dados novos.

Exemplo mental:
"servidor, crie isso para mim"

### PUT

Usado para atualizar um recurso inteiro.

### PATCH

Usado para atualizar uma parte do recurso.

### DELETE

Usado para remover algo.

## O que e URL

URL e o endereco do recurso.

Exemplo:

```text
https://jsonplaceholder.typicode.com/posts/1
```

## O que sao query params

Sao informacoes depois do `?` na URL.

Exemplo:

```text
https://api.exemplo.com/usuarios?page=2&ativo=true
```

Nesse caso:

- `page=2`
- `ativo=true`

Em `requests`, voce normalmente nao monta isso manualmente.
Voce faz:

```python
params = {"page": 2, "ativo": "true"}
```

## O que sao headers

Headers sao metadados da requisicao ou da resposta.

Exemplos de uso:

- dizer que voce quer JSON
- enviar token
- identificar seu programa

Exemplo:

```python
headers = {"Accept": "application/json"}
```

## O que e body

Body e o conteudo principal enviado na requisicao.

Em `POST`, `PUT` e `PATCH`, e comum mandar dados no body.

## O que e JSON

JSON e um formato de texto muito usado para troca de dados.

Exemplo:

```json
{
  "nome": "Ana",
  "idade": 25,
  "ativo": true
}
```

Quando `requests` recebe JSON, voce pode converter assim:

```python
dados = response.json()
```

Depois disso, voce costuma trabalhar com:

- dicionarios
- listas
- strings
- numeros
- booleanos

## O que e status code

Status code e um numero que resume o resultado da requisicao.

### Codigos comuns

- `200`: deu certo
- `201`: criado com sucesso
- `204`: sucesso sem corpo de resposta
- `400`: requisicao invalida
- `401`: sem autenticacao
- `403`: proibido
- `404`: nao encontrado
- `500`: erro no servidor

## O que e API

API e uma interface de comunicacao entre sistemas.
No nosso contexto, e um endereco web que aceita requisicoes e devolve dados.

Exemplos:

- API de CEP
- API de posts
- API de pagamentos
- API do seu proprio sistema

## Forma simples de pensar em uma chamada

Quando voce escreve:

```python
response = requests.get(url)
```

voce esta fazendo esta pergunta:

"Servidor, voce pode me devolver os dados desse endereco?"

Quando voce escreve:

```python
response = requests.post(url, json=payload)
```

voce esta dizendo:

"Servidor, crie ou processe isso com estes dados."
