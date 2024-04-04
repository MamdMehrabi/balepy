import requests


class Network:
    def __init__(self, token: str, timeout: float):
        self.token: str = token
        self.timeout: float = timeout
        self.session: function = requests.session()

    @property
    def url(self) -> str:
        return f'https://tapi.bale.ai/bot{self.token}/'

    def disconnect(self):
        return self.session.close()

    async def connect(self, method: str, data: dict = None, files: dict = None) -> requests.Response:
        responce = (
            self.session.request(
                'post',
                url=self.url + method,
                timeout=self.timeout, data=data, files=files
            )
        )
        if responce.status_code != requests.codes.ok:
            raise Exception(responce.status_code + responce.text)

        final_value = responce.json()
        return final_value['result']
