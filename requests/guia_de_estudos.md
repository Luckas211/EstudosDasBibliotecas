# Guia de estudos: requests

Este guia foi feito para voce estudar `requests` com mais clareza e menos decoracao.
O foco nao e apenas "fazer funcionar", mas entender o que cada parte da linha quer dizer.

## Objetivo final do modulo

Ao terminar este estudo, voce deve conseguir:

- ler uma linha com `requests.get(...)` e explicar cada simbolo
- consumir APIs simples e intermediarias
- entender a diferenca entre `params`, `headers`, `data` e `json`
- diferenciar `Accept` de `Content-Type`
- reconhecer quando a resposta pode ser JSON, XML, HTML ou texto
- tratar erros sem deixar o programa quebrar
- organizar funcoes reutilizaveis
- criar pequenos clientes de API com boa estrutura

## Como ler uma linha de requests

Exemplo:

```python
response = requests.get(url, params=parametros, timeout=10)
```

Leia assim:

- `response` e a variavel que vai guardar o resultado
- `=` significa "recebe"
- `requests` e o modulo importado
- `.` acessa algo dentro do modulo
- `get` e a funcao usada para requisicao GET
- `(` inicia a chamada da funcao
- `url` e o primeiro argumento enviado
- `params=parametros` e um argumento nomeado
- `timeout=10` e outro argumento nomeado
- `)` fecha a chamada

## Como estudar por nivel

### Basico

Objetivo:
entender o que e uma requisicao, uma resposta e um JSON.

Foque em:

- `01_introducao_e_get.py`
- `02_parametros_e_headers.py`
- `03_post_e_outros_metodos.py`
- `04_tratamento_de_erros.py`
- `10_explorando_response_e_json_na_pratica.py`

### Intermediario

Objetivo:
usar `requests` com mais autonomia e menos repeticao.

Foque em:

- `05_sessoes_e_autenticacao.py`
- `06_downloads_e_arquivos.py`
- `07_consumindo_apis_reais.py`
- `08_boas_praticas_e_cliente_reutilizavel.py`
- `11_upload_de_arquivos_e_formularios.py`
- `12_timeout_retry_e_resiliencia.py`

### Avancado

Objetivo:
estruturar clientes de API mais proximos de projetos reais.

Foque em:

- `13_cliente_de_api_com_classe.py`
- `09_projeto_guiado_consultor_web.py`
- `14_monitorando_varias_urls.py`
- `15_formatos_e_content_types_na_pratica.py`
- `desafio_final_cliente_de_apis.py`

## Perguntas que voce deve responder sozinho

- O que eu coloco dentro de `params={...}`?
- O que eu coloco dentro de `headers={...}`?
- O que muda entre `Accept` e `Content-Type`?
- Quando eu esperaria XML em vez de JSON?
- Quando uso `dados["chave"]` e quando uso `lista[0]`?
- O que muda entre `data=` e `json=`?
- Por que `timeout=` e importante?
- Quando vale usar `raise_for_status()`?
- Qual parte da resposta e metadado e qual parte e conteudo?

## Exercicio de leitura de codigo

Pegue esta linha:

```python
headers = {"Accept": "application/json"}
```

Explique assim:

- `headers` e o nome da variavel
- `=` guarda um valor nela
- `{}` cria um dicionario
- `"Accept"` e a chave
- `:` separa chave e valor
- `"application/json"` e o valor

Agora faca o mesmo com:

```python
dados["results"][0]["joke"]
```

Leia assim:

- `dados` e um dicionario
- `["results"]` acessa a chave `results`
- `[0]` pega o primeiro item da lista
- `["joke"]` acessa a chave `joke` dentro do item escolhido

## Rotina recomendada

1. Leia o material teorico.
2. Rode a aula sem alterar nada.
3. Rode a aula alterando 3 valores.
4. Tente prever a saida antes de executar.
5. Reescreva o exemplo sem olhar.
6. Crie uma variacao propria.

## Sinal de progresso real

Voce esta evoluindo quando para de apenas copiar e passa a:

- prever o formato da resposta
- olhar o `Content-Type` antes de assumir que tudo e JSON
- escolher sozinho entre `params` e `json`
- ler um JSON e navegar por ele com seguranca
- montar uma funcao de consulta reaproveitavel
