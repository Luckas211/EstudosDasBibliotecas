# Material 04: Accept, Content-Type e formatos de dados

Este material responde uma duvida muito importante:
`application/json` existe, mas e o unico formato? Nao.

Em integracoes reais, voce pode encontrar:

- JSON
- XML
- HTML
- texto puro
- formulario
- multipart para upload

## 1. O que e `Accept`

O header `Accept` diz:

"Servidor, eu prefiro receber a resposta neste formato."

Exemplo:

```python
headers = {"Accept": "application/json"}
```

Isso significa:

- `Accept` e a chave do header
- `application/json` e o formato que o cliente prefere receber

## 2. O que e `Content-Type`

O header `Content-Type` diz:

"O conteudo que estou enviando ou recebendo esta neste formato."

Exemplo:

```python
headers = {"Content-Type": "application/json"}
```

Isso significa:

- o corpo enviado esta em JSON

## 3. Diferenca mental entre os dois

Pense assim:

- `Accept` = o que eu gostaria de receber
- `Content-Type` = o que eu estou enviando ou o que realmente chegou

## 4. Formatos comuns

### `application/json`

Formato mais comum em APIs modernas.

Use quando:

- a API trabalha com objetos e listas
- voce quer converter a resposta com `response.json()`

Exemplo:

```python
headers = {"Accept": "application/json"}
```

## `application/xml`

Formato comum em sistemas legados, integracoes corporativas e alguns webservices.

Use quando:

- a documentacao da API pede XML
- o sistema antigo trabalha com XML
- a integracao e com padroes antigos ou empresariais

Exemplo:

```python
headers = {"Accept": "application/xml"}
```

## `text/xml`

Tambem representa XML.
Costuma aparecer em sistemas mais antigos.

Regra pratica:

- `application/xml` costuma ser a escolha mais moderna
- `text/xml` ainda pode aparecer em integracoes antigas

## `text/html`

Usado quando a resposta e uma pagina HTML.

Use quando:

- voce esta acessando uma pagina web
- quer inspecionar HTML
- esta estudando scraping

Exemplo:

```python
headers = {"Accept": "text/html"}
```

## `text/plain`

Usado para texto puro.

Use quando:

- a API devolve mensagens simples
- o endpoint retorna logs, tokens ou textos pequenos

Exemplo:

```python
headers = {"Accept": "text/plain"}
```

## `application/x-www-form-urlencoded`

Muito comum em formularios simples.

Em `requests`, geralmente aparece quando voce usa:

```python
requests.post(url, data={"email": "ana@email.com"})
```

## `multipart/form-data`

Muito comum quando voce envia arquivos.

Em `requests`, geralmente aparece quando voce usa:

```python
requests.post(url, files=files)
```

## 5. Exemplo pratico de escolha

### Caso 1: API moderna

```python
response = requests.get(url, headers={"Accept": "application/json"})
```

Por que fazer isso:

- APIs modernas quase sempre respondem em JSON
- o Python trabalha muito bem com dicionarios e listas

### Caso 2: sistema legado

```python
xml = "<pedido><id>10</id></pedido>"
headers = {"Content-Type": "application/xml", "Accept": "application/xml"}
response = requests.post(url, data=xml, headers=headers)
```

Por que fazer isso:

- alguns sistemas antigos exigem XML
- a API pode rejeitar JSON se a documentacao pedir XML

### Caso 3: pagina web

```python
response = requests.get(url, headers={"Accept": "text/html"})
```

Por que fazer isso:

- voce esta buscando uma pagina HTML, nao um JSON de API

## 6. Regra profissional importante

Nao confie apenas no que voce pediu no `Accept`.
Confira sempre o que realmente chegou:

```python
response.headers.get("Content-Type")
```

Por que isso e importante:

- o servidor pode ignorar o `Accept`
- a documentacao pode estar incompleta
- um endpoint pode mudar

## 7. Leitura profissional simples

Sempre pergunte:

- o que estou enviando
- em que formato estou enviando
- o que espero receber
- em que formato realmente recebi
