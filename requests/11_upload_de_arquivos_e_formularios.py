# requests/11_upload_de_arquivos_e_formularios.py

"""
Aula 11: upload de arquivos e envio combinado de formulario

Objetivo:
- entender o argumento `files=`
- ver o que vai dentro da tupla do arquivo
- combinar `data=` com `files=`

Execute com:
python requests/11_upload_de_arquivos_e_formularios.py
"""

import requests


url = "https://httpbin.org/post"

# `files` recebe um dicionario.
# A chave e o nome do campo do formulario.
# O valor e uma tupla com:
# - nome do arquivo
# - conteudo em bytes
# - tipo do arquivo
files = {
    "arquivo": ("anotacoes.txt", b"linha 1\nlinha 2\nlinha 3", "text/plain")
}

# `data` manda outros campos do formulario junto com o arquivo.
data = {
    "descricao": "Arquivo de exemplo para estudo",
    "categoria": "texto",
}

response = requests.post(url, data=data, files=files, timeout=10)
dados = response.json()

print("=== AULA 11: UPLOAD ===")
print(f"Status code: {response.status_code}")

print("\nCampos de formulario recebidos:")
print(dados["form"])

print("\nArquivos recebidos:")
print(dados["files"])

print("\n=== COMO LER A TUPLA DO ARQUIVO ===")
print("('anotacoes.txt', b'conteudo', 'text/plain')")
print("- primeiro item: nome do arquivo")
print("- segundo item: conteudo em bytes")
print("- terceiro item: content type")

print("\n=== OBSERVACAO PROFISSIONAL ===")
print("Quando voce usa `files=`, a requests costuma montar")
print("um Content-Type do tipo multipart/form-data automaticamente.")
