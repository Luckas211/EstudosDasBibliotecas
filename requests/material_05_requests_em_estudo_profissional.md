# Material 05: requests para um estudo mais profissional

Este material nao foi feito para complicar.
Ele foi feito para te ensinar a estudar com uma mentalidade mais proxima do mercado.

## 1. Estudar profissionalmente nao e decorar

No uso profissional, o importante nao e decorar tudo.
O importante e saber fazer perguntas corretas:

- qual e a URL
- qual metodo HTTP devo usar
- quais parametros essa API aceita
- qual formato devo enviar
- qual formato vou receber
- como tratar erro
- como validar a resposta

## 2. O que observar numa documentacao de API

Antes de escrever codigo, procure:

- metodo: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- endpoint: a URL exata
- autenticacao: token, chave, usuario e senha
- query params disponiveis
- body esperado
- formato esperado: JSON, XML, formulario
- status codes comuns
- exemplo de resposta

## 3. Regras praticas para escrever melhor

### Sempre use `timeout`

```python
requests.get(url, timeout=10)
```

Por que:

- evita travar esperando para sempre

### Sempre considere erro

```python
response.raise_for_status()
```

Por que:

- 404, 401 e 500 sao comuns em integracoes reais

### Use nomes claros

Melhor:

```python
url_usuarios = "https://api.exemplo.com/usuarios"
parametros_busca = {"page": 1}
```

Pior:

```python
u = "https://api.exemplo.com/usuarios"
p = {"page": 1}
```

### Centralize logica repetida

Melhor criar uma funcao:

```python
def buscar_json(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()
```

Por que:

- reduz repeticao
- melhora manutencao
- deixa o projeto mais organizado

## 4. O que muda do estudo basico para o profissional

### No estudo basico

Voce aprende:

- como fazer uma chamada
- como imprimir a resposta

### No estudo profissional

Voce passa a pensar em:

- reutilizacao
- tratamento de erro
- padrao de nomes
- validacao da resposta
- seguranca
- leitura de documentacao

## 5. Coisas que profissionais observam

### `User-Agent`

Ajuda a identificar seu sistema.

Exemplo:

```python
headers = {"User-Agent": "MeuSistemaDeEstudos/1.0"}
```

### `Accept`

Ajuda a deixar claro o formato esperado.

### `Content-Type`

Ajuda a deixar claro o formato enviado.

### `status_code`

Ajuda a entender se a requisicao foi aceita, criada, negada ou falhou.

## 6. Erros comuns de iniciantes

- esquecer `timeout`
- usar `response.json()` sem saber se a resposta e JSON
- nao checar `status_code`
- misturar `data=` e `json=` sem entender a diferenca
- confiar demais que toda API sempre devolve o mesmo formato

## 7. Perguntas profissionais para toda chamada

Antes da chamada:

- por que estou chamando esse endpoint
- o que preciso enviar
- que resposta espero

Depois da chamada:

- o status veio certo
- o formato veio certo
- os campos que eu preciso realmente existem

## 8. Exemplo de raciocinio maduro

Em vez de pensar apenas:

"quero fazer um GET"

pense:

"quero consultar uma API, espero JSON, vou usar timeout, validar o status e so depois acessar os dados."
