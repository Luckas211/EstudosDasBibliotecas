# Material 01: fundamentos de sintaxe para estudar requests

Este material existe para responder uma duvida muito importante:
antes de entender `requests`, voce precisa entender a forma da linha de codigo.

## 1. O que significa `import requests`

```python
import requests
```

Leia assim:

- `import` pede ao Python para trazer um modulo
- `requests` e o nome do modulo

Depois disso, voce pode usar:

```python
requests.get(...)
requests.post(...)
requests.Session()
```

## 2. O que significa o ponto `.`

Exemplo:

```python
requests.get
response.json
response.status_code
```

O ponto acessa algo "dentro" de um objeto ou modulo.

- `requests.get` acessa a funcao `get` que existe no modulo `requests`
- `response.json` acessa o metodo `json` do objeto `response`
- `response.status_code` acessa um atributo da resposta

## 3. O que significam os parenteses `()`

Os parenteses aparecem muito em `requests` por dois motivos.

### 3.1 Chamada de funcao

```python
requests.get(url)
```

Aqui:

- `get` e a funcao
- `(` abre a chamada
- `url` e o argumento
- `)` fecha a chamada

### 3.2 Agrupar valores em uma tupla

```python
auth = ("user", "pass")
```

Aqui:

- `()` nao esta chamando funcao
- esta agrupando dois valores
- isso forma uma tupla

Essa tupla pode ser usada em:

```python
requests.get(url, auth=("user", "pass"))
```

## 4. O que significam as chaves `{}`

Na maior parte deste modulo, `{}` cria um dicionario.

Exemplo:

```python
headers = {"Accept": "application/json"}
```

Leia assim:

- `{}` cria um dicionario
- `"Accept"` e a chave
- `:` separa chave e valor
- `"application/json"` e o valor

Outro exemplo:

```python
params = {"page": 2, "limit": 10}
```

Aqui:

- `"page"` e `"limit"` sao chaves
- `2` e `10` sao valores
- `,` separa cada par chave-valor

## 5. O que significam os colchetes `[]`

Os colchetes aparecem de duas formas principais.

### 5.1 Criando uma lista

```python
ids = [1, 2, 3]
```

Aqui:

- `[]` cria uma lista
- dentro dela voce coloca varios itens
- `,` separa cada item

### 5.2 Acessando um item

Exemplo com lista:

```python
ids[0]
```

Aqui:

- `ids` e a lista
- `[0]` pega o primeiro item

Exemplo com dicionario:

```python
dados["origin"]
```

Aqui:

- `dados` e um dicionario
- `["origin"]` acessa o valor guardado na chave `origin`

Exemplo misto:

```python
dados["results"][0]["joke"]
```

Leia assim:

- pegue a chave `results`
- dentro dela, pegue o item `0`
- dentro desse item, pegue a chave `joke`

## 6. O que significa `=`

O sinal `=` guarda um valor em uma variavel.

```python
url = "https://httpbin.org/get"
```

Leia assim:

- crie a variavel `url`
- guarde nela esse texto

Outro exemplo:

```python
response = requests.get(url)
```

Leia assim:

- execute `requests.get(url)`
- guarde o resultado em `response`

## 7. O que significa `nome=valor` dentro de `()`

Exemplo:

```python
requests.get(url, timeout=10)
```

Aqui:

- `url` foi enviado como argumento simples
- `timeout=10` foi enviado como argumento nomeado

Outro exemplo:

```python
requests.get(url, params={"page": 2})
```

Aqui:

- `params` e o nome do argumento
- `{"page": 2}` e o valor que voce esta passando para esse argumento

## 8. O que geralmente vai dentro de cada argumento

### `url`

Uma string:

```python
url = "https://api.exemplo.com/usuarios"
```

### `params`

Um dicionario com parametros de URL:

```python
params = {"page": 1, "search": "python"}
```

### `headers`

Um dicionario com cabecalhos:

```python
headers = {"Accept": "application/json"}
```

### `json`

Um dicionario com dados para enviar como JSON:

```python
json = {"nome": "Ana", "idade": 25}
```

### `data`

Um dicionario com dados de formulario:

```python
data = {"email": "ana@email.com", "senha": "123"}
```

### `files`

Um dicionario com arquivos:

```python
files = {"arquivo": ("texto.txt", b"conteudo", "text/plain")}
```

## 9. Linha completa lida passo a passo

```python
response = requests.get(url, params=params, headers=headers, timeout=10)
```

Explicacao completa:

- `response` vai guardar o resultado
- `=` faz a atribuicao
- `requests` e o modulo
- `.` acessa a funcao `get`
- `get` faz uma requisicao HTTP GET
- `(` abre a chamada
- `url` informa para onde a requisicao vai
- `params=params` envia parametros na URL
- `headers=headers` envia cabecalhos
- `timeout=10` limita o tempo de espera
- `)` fecha a chamada

## 10. Como pensar melhor

Antes de olhar para o codigo, pergunte:

- para onde a requisicao vai
- o que ela envia
- o que ela espera receber
- onde a resposta vai ficar guardada
- como eu vou acessar os dados da resposta
