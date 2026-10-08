import requests


INTERACOES_URL = "http://localhost:8002"

def listar_avaliacoes(token=None):
    headers = {}

    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(
        f"{INTERACOES_URL}/api/publicacao",
        headers=headers
    )

    return response