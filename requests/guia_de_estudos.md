# Guia de estudos: requests

Este guia foi pensado para transformar as aulas em pratica de verdade.

## Meta do modulo

Ao final do estudo, voce deve conseguir:

- entender o ciclo basico de uma requisicao HTTP
- consumir APIs REST simples
- ler JSON com confianca
- tratar falhas de rede sem quebrar o programa
- montar pequenos clientes de API no terminal

## Rotina recomendada

1. Estude uma aula por vez.
2. Rode o exemplo original.
3. Faça 3 mudancas no codigo por conta propria.
4. Anote o que mudou na resposta da API.
5. Tente reescrever sem olhar.

## Perguntas de revisao

- O que muda entre `params`, `data` e `json`?
- Quando usar `response.text` e quando usar `response.json()`?
- O que o `status_code` informa?
- Por que `raise_for_status()` e util?
- Quando vale usar `stream=True`?
- Por que toda requisicao deveria ter `timeout`?

## Exercicios por etapa

### Depois da aula 2

- faca uma busca de piadas trocando o termo `cat` por outro
- adicione mais um cabecalho e imprima a URL final

### Depois da aula 4

- troque a URL por outra invalida e compare o erro
- altere o timeout para 1 segundo e observe o comportamento

### Depois da aula 6

- baixe a imagem novamente com outro nome
- imprima o tamanho do arquivo antes e depois de salvar

### Depois da aula 8

- transforme `fazer_get_json()` em uma funcao separada para outros projetos
- adicione uma mensagem diferente para erro 404 e 500

## Mini projetos sugeridos

- buscador de filmes em uma API publica
- leitor de cotacoes com API financeira
- consultor de enderecos por CEP
- monitor que verifica se varias URLs estao online

## Como saber se voce evoluiu

Voce esta avancando bem quando consegue:

- explicar o que uma API espera receber
- ler a documentacao de um endpoint e montar a chamada
- prever o formato da resposta
- organizar seu codigo em funcoes reutilizaveis
