# Manual das bibliotecas em Python

Este diretorio foi organizado como uma trilha de estudos didatica para iniciantes.
A proposta e que cada biblioteca funcione como um pequeno curso, com aulas progressivas, explicacoes em portugues simples e exemplos comentados linha por linha.

## Como a trilha esta organizada

- Cada biblioteca ganhou sua propria pasta.
- Dentro de cada pasta existe um `README.md` com a visao geral do modulo.
- As aulas seguem o padrao `Aula01`, `Aula02`, `Aula03` e assim por diante.
- O que puder ser estudado passo a passo foi criado em `.ipynb`.
- O que fizer mais sentido como script executavel foi criado em `.py`.

## Bibliotecas estudadas

- `os`
- `re`
- `pytesseract`
- `pdf2image`

## Ordem sugerida

1. `os`
2. `re`
3. `pdf2image`
4. `pytesseract`

## Intencao pedagogica

Os materiais foram escritos pensando em alguem leigo.
Por isso, cada modulo tenta responder sempre estas perguntas:

- o que esta funcao faz
- o que este objeto representa
- quais parametros ela recebe
- o que ela devolve
- quando usar
- como variar o mesmo conceito em exemplos diferentes

## Antes de executar os notebooks

Para `os` e `re`, basta ter Python instalado.

Para `pdf2image` e `pytesseract`, alem das bibliotecas Python, voce tambem precisa instalar ferramentas externas:

- `pdf2image` depende do Poppler no Windows
- `pytesseract` depende do Tesseract OCR instalado no sistema

## Arquivo de apoio

O arquivo `requirements-estudos.txt` reune as dependencias Python mais importantes para esta pasta de estudos.

## Forma recomendada de estudo

1. Leia o `README.md` da biblioteca.
2. Estude uma aula por vez.
3. Execute cada bloco.
4. Leia os comentarios de todas as linhas.
5. Modifique os exemplos.
6. Tente repetir sem copiar.
7. Anote duvidas e compare uma aula com a outra.
