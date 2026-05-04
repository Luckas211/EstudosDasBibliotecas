# requests/13_cliente_de_api_com_classe.py

"""
Aula 13: cliente de API com classe

Objetivo:
- organizar melhor o acesso a uma API
- reaproveitar `base_url` e `Session`
- criar metodos com responsabilidade clara

Execute com:
python requests/13_cliente_de_api_com_classe.py
"""

import requests


class ClienteJSONPlaceholder:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.session = requests.Session()

    def _get(self, caminho, params=None):
        url = f"{self.base_url}{caminho}"
        response = self.session.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    def listar_posts(self, user_id=None):
        params = {}

        if user_id is not None:
            params["userId"] = user_id

        return self._get("/posts", params=params or None)

    def buscar_post(self, post_id):
        return self._get(f"/posts/{post_id}")


cliente = ClienteJSONPlaceholder()

print("=== AULA 13: CLIENTE COM CLASSE ===")

posts = cliente.listar_posts(user_id=1)
print(f"Quantidade de posts recebidos para user_id=1: {len(posts)}")
print(f"Primeiro titulo: {posts[0]['title']}")

post = cliente.buscar_post(1)
print("\nPost 1:")
print(post)

print("\n=== COMO LER A IDEIA ===")
print("self.base_url guarda a base da API.")
print("self.session reaproveita a sessao.")
print("_get centraliza a logica de GET.")
print("listar_posts e buscar_post sao metodos especificos do cliente.")
