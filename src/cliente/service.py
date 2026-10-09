
import requests
from django.conf import settings


class ClienteService:
    BASE_URL = getattr(
        settings,
        "GATEWAY_URL",
        "http://127.0.0.1:8000",
    )

    @classmethod
    def requisicao(
        cls,
        metodo,
        endpoint,
        token=None,
        dados=None,
        arquivos=None,
    ):
        headers = {}

        if token:
            token = token.strip()

            if token.lower().startswith("bearer "):
                headers["Authorization"] = token
            else:
                headers["Authorization"] = f"Bearer {token}"

        try:
            resposta = requests.request(
                method=metodo,
                url=f"{cls.BASE_URL.rstrip('/')}/{endpoint.lstrip('/')}",
                headers=headers,
                json=dados if dados is not None and not arquivos else None,
                data=dados if arquivos else None,
                files=arquivos,
                timeout=10,
            )

            if resposta.status_code == 204:
                return {
                    "dados": None,
                    "status": 204,
                }

            try:
                conteudo = resposta.json()
            except ValueError:
                conteudo = {"mensagem": resposta.text}

            return {
                "dados": conteudo,
                "status": resposta.status_code,
            }

        except requests.Timeout:
            return {
                "dados": {
                    "erro": "Tempo limite ao acessar o Gateway."
                },
                "status": 504,
            }

        except requests.RequestException:
            return {
                "dados": {
                    "erro": "Não foi possível acessar o Gateway."
                },
                "status": 502,
            }