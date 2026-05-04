# Material 03: argumentos mais usados em requests

Este material existe para responder:
"o que eu coloco dentro dos parenteses da funcao?"

## Estrutura geral

Uma chamada comum pode ser assim:

```python
response = requests.get(url, params=params, headers=headers, timeout=10)
```

Nem sempre voce usa tudo.
Voce escolhe apenas os argumentos necessarios.

## 1. `url`

E o endereco que sera acessado.

Exemplo:

```python
url = "https://httpbin.org/get"
```

Quase sempre sera uma string.

## 2. `params`

Usado para query params.

Voce geralmente coloca um dicionario:

```python
params = {
    "page": 1,
    "limit": 5,
    "search": "python",
}
```

Resultado mental:

```text
...?page=1&limit=5&search=python
```

## 3. `headers`

Usado para enviar metadados.

Voce geralmente coloca um dicionario:

```python
headers = {
    "Accept": "application/json",
    "User-Agent": "MeuScriptDeEstudo/1.0",
}
```

Exemplos de headers comuns:

- `Accept: application/json` -> prefiro JSON
- `Accept: application/xml` -> prefiro XML
- `Accept: text/html` -> espero HTML
- `User-Agent: MeuSistema/1.0` -> identifica meu sistema
- `Authorization: Bearer ...` -> envia token

Por que isso importa:

- algumas APIs respondem em formatos diferentes
- algumas APIs exigem autenticacao
- um header bem escolhido deixa sua intencao mais clara

## 4. `timeout`

Usado para limitar quanto tempo o programa vai esperar.

Exemplo:

```python
timeout=10
```

Sem `timeout`, seu programa pode demorar demais em algumas falhas.

## 5. `data`

Usado para enviar dados de formulario.

Exemplo:

```python
data = {
    "email": "ana@email.com",
    "senha": "123456",
}
```

Normalmente aparece em:

```python
requests.post(url, data=data)
```

## 6. `json`

Usado para enviar dados como JSON.

Exemplo:

```python
payload = {
    "nome": "Ana",
    "idade": 25,
}
```

Uso:

```python
requests.post(url, json=payload)
```

## 7. `auth`

Usado para autenticacao simples.

Exemplo:

```python
auth = ("user", "pass")
```

Uso:

```python
requests.get(url, auth=auth)
```

## 8. `stream`

Usado quando voce quer processar a resposta em partes,
especialmente em downloads.

Exemplo:

```python
requests.get(url, stream=True)
```

## 9. `files`

Usado para upload de arquivos.

Exemplo:

```python
files = {
    "arquivo": ("relatorio.txt", b"conteudo do arquivo", "text/plain")
}
```

Uso:

```python
requests.post(url, files=files)
```

Quando voce usa `files=`, a `requests` normalmente monta um
`Content-Type` do tipo `multipart/form-data` automaticamente.

Isso e util porque:

- voce nao precisa montar esse header manualmente na maioria dos casos

## 10. `allow_redirects`

Controla se a requisicao deve seguir redirecionamentos automaticamente.

Exemplo:

```python
requests.get(url, allow_redirects=True)
```

Uso mental:

- `True` -> segue o redirecionamento
- `False` -> nao segue

## 11. `cookies`

Permite enviar cookies manualmente.

Exemplo:

```python
cookies = {"sessao": "abc123"}
requests.get(url, cookies=cookies)
```

## 12. `verify`

Controla a verificacao do certificado SSL.

Exemplo:

```python
requests.get(url, verify=True)
```

Regra pratica:

- normalmente deixe `verify=True`
- so mexa nisso quando souber exatamente por que esta mudando

## 13. Exemplo completo

```python
response = requests.post(
    url,
    params={"debug": "true"},
    headers={"Accept": "application/json"},
    json={"nome": "Ana"},
    timeout=10,
)
```

Leia assim:

- `post` porque estamos enviando dados
- `url` define o destino
- `params` adiciona informacoes na URL
- `headers` manda metadados
- `json` manda o corpo principal
- `timeout` limita a espera

## 14. Exemplo mais profissional

```python
response = requests.post(
    url,
    headers={
        "Accept": "application/json",
        "User-Agent": "MeuSistemaDeEstudo/1.0",
    },
    json={"nome": "Ana", "perfil": "aluna"},
    timeout=10,
)
```

Por que esse exemplo e melhor:

- deixa claro o formato esperado
- identifica seu sistema
- organiza melhor a intencao da chamada
- nao esquece `timeout`
