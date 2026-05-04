# Modulo: requests

A biblioteca `requests` ajuda o Python a conversar com a web.
Com ela, voce aprende a:

- enviar requisicoes HTTP
- consumir APIs
- ler respostas em JSON
- baixar arquivos
- tratar erros de rede
- montar pequenos clientes de API

Este modulo foi reorganizado para ficar mais didatico e mais profundo.
Agora ele esta dividido em:

- materiais de apoio teoricos
- aulas basicas
- aulas intermediarias
- aulas avancadas
- projeto guiado
- desafio final

## O que estudar antes das aulas

Leia estes materiais primeiro:

1. `material_01_fundamentos_de_sintaxe.md`
2. `material_02_http_json_e_api.md`
3. `material_03_argumentos_mais_usados.md`
4. `material_04_accept_content_type_e_formatos.md`
5. `material_05_requests_em_estudo_profissional.md`

Esses arquivos explicam com calma:

- o que faz `import requests`
- o que significa `requests.get(...)`
- para que servem `()`, `{}`, `[]`, `.` e `=`
- o que colocar dentro de `params`, `headers`, `json`, `data`, `files`
- o que e uma requisicao, uma resposta, uma API e um JSON
- como pensar em `Accept`, `Content-Type`, JSON, XML, HTML e texto puro
- como estudar `requests` de um jeito mais profissional

## Trilha por nivel

### Basico

1. `01_introducao_e_get.py`
2. `02_parametros_e_headers.py`
3. `03_post_e_outros_metodos.py`
4. `04_tratamento_de_erros.py`
5. `10_explorando_response_e_json_na_pratica.py`

### Intermediario

6. `05_sessoes_e_autenticacao.py`
7. `06_downloads_e_arquivos.py`
8. `07_consumindo_apis_reais.py`
9. `08_boas_praticas_e_cliente_reutilizavel.py`
10. `11_upload_de_arquivos_e_formularios.py`
11. `12_timeout_retry_e_resiliencia.py`

### Avancado

12. `13_cliente_de_api_com_classe.py`
13. `09_projeto_guiado_consultor_web.py`
14. `14_monitorando_varias_urls.py`
15. `15_formatos_e_content_types_na_pratica.py`
16. `desafio_final_cliente_de_apis.py`

## APIs usadas no estudo

- `https://httpbin.org`
- `https://jsonplaceholder.typicode.com`
- `https://viacep.com.br`
- `https://icanhazdadjoke.com`

## Como estudar bem este modulo

1. Leia a teoria antes do codigo.
2. Rode uma aula por vez.
3. Observe a saida do terminal com calma.
4. Compare a linha do codigo com a resposta da API.
5. Troque valores dentro de `[]`, `{}` e `()` para ver o efeito.
6. Reescreva uma chamada sem copiar.
7. Explique em voz alta o que cada argumento faz.

## Dependencia

Instale com:

```bash
pip install requests
```
