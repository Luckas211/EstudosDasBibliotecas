# requests/06_downloads_e_arquivos.py

"""
Aula 6: Download de arquivos e resposta em binario

Nem toda resposta da web vira texto ou JSON.
Muitas vezes precisamos baixar imagens, PDFs, planilhas ou outros arquivos.

Nesta aula, voce vai aprender:
- a diferenca entre `.text`, `.content` e `iter_content()`
- como baixar um arquivo pequeno
- como salvar um arquivo no disco
- por que `stream=True` ajuda em arquivos maiores

Para executar este arquivo:
python requests/06_downloads_e_arquivos.py
"""

import os

import requests


url_imagem = "https://httpbin.org/image/png"
nome_arquivo = "arquivo_baixado.png"

print(f"Baixando arquivo de: {url_imagem}")

with requests.get(url_imagem, stream=True, timeout=10) as response:
    response.raise_for_status()

    print(f"Status code: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")

    with open(nome_arquivo, "wb") as arquivo:
        for bloco in response.iter_content(chunk_size=1024):
            if bloco:
                arquivo.write(bloco)

print(f"Arquivo salvo com sucesso: {nome_arquivo}")
print(f"Tamanho final: {os.path.getsize(nome_arquivo)} bytes")

print("\nQuando usar cada abordagem:")
print("- response.text -> para texto ou HTML")
print("- response.json() -> para APIs JSON")
print("- response.content -> para bytes de arquivos pequenos")
print("- response.iter_content() -> para arquivos maiores")
