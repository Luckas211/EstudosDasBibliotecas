# Manual das bibliotecas em Python

Este diretorio foi organizado como uma trilha de estudos didatica para iniciantes.
A ideia e transformar cada biblioteca em um mini curso com aulas progressivas,
explicacoes em portugues simples, exemplos comentados e pequenos projetos.

## Como a trilha esta organizada

- cada biblioteca tem sua propria pasta
- cada pasta pode ter um `README.md` com a visao geral do modulo
- as aulas seguem uma ordem progressiva
- notebooks `.ipynb` aparecem quando o estudo pede exploracao passo a passo
- scripts `.py` aparecem quando o melhor formato e pratica executavel
- alguns modulos tambem possuem guias de estudo e desafios finais

## Modulos disponiveis

- `os`
- `re`
- `pdf2image`
- `pytesseract`
- `sqlite3`
- `requests`
- `streamlit`
- `fastapi`

## Ordem sugerida de estudo

1. `os`
2. `re`
3. `sqlite3`
4. `requests`
5. `fastapi`
6. `streamlit`
7. `pdf2image`
8. `pytesseract`

## Intencao pedagogica

Os materiais foram escritos pensando em alguem leigo ou em fase inicial de consolidacao.
Por isso, cada modulo tenta responder sempre estas perguntas:

- o que esta funcao faz
- o que este objeto representa
- quais parametros ela recebe
- o que ela devolve
- quando usar
- como variar o mesmo conceito em exemplos diferentes
- como transformar teoria em pratica

## Antes de executar os materiais

Para `os`, `re` e `sqlite3`, basta ter Python instalado.

Para outros modulos, algumas dependencias podem ser necessarias:

- `requests` exige a biblioteca `requests`
- `fastapi` exige `fastapi` e `uvicorn`
- `streamlit` exige `streamlit`
- `pdf2image` depende de `pdf2image`, `Pillow` e Poppler no Windows
- `pytesseract` depende de `pytesseract` e do Tesseract OCR no sistema

## Arquivo de apoio

O arquivo `requirements-estudos.txt` reune dependencias Python uteis para a trilha.
Bibliotecas da padrao, como `os`, `re` e `sqlite3`, nao entram nele.

## Forma recomendada de estudo

1. Leia o `README.md` da biblioteca antes de comecar.
2. Estude uma aula por vez.
3. Execute os exemplos e observe a saida.
4. Leia os comentarios com calma.
5. Modifique valores, rotas, URLs e parametros.
6. Reescreva partes sem copiar.
7. Use os desafios finais para fixar o conteudo.
