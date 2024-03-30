import requests

class Network:
    def __init__(self, token: str, timeout: float):
        self.token: str = token
        self.timeout: float = timeout
        self.session = requests.session()

    @property
    def url(self) -> str:
        return f'https://tapi.bale.ai/bot{self.token}/'

    def connect(self, method: str, data: dict = None, request_method: str = 'post') -> requests.Response:
        with self.session.request(method=request_method, url= self.url + method, timeout=self.timeout, data=data) as response:
            return response.json()
