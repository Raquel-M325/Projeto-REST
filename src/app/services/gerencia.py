import requests

GERENCIA_URL =  "http://localhost:8000"

def listar_publicacoes(token=None):
    headers = {}

    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(
        f"{GERENCIA_URL}/api/publicacao/",
        headers=headers
    )

    return response