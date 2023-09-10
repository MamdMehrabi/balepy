from aiohttp import ClientSession

class Connection:

    async def __init__(self , token , time_out):
        self.client_session = None
        self.base_url = "https://tapi.bale.ai/bot"
        self.token = token
        self.time_out = time_out
        self.is_started = False

    async def start(self):
        if self.is_started:
            raise ConnectionError("Connection is STARTED")
        self.is_started = True
        self.client_session = ClientSession()

    async def stop(self):
        if not self.is_started:
            raise ConnectionError("Connection is STOPED")

    @property
    async def url(self):
        return f"{self.base_url}{self.token}"

    async def execute(self , method , service , jspn=None):
        async with self.client_session.request(
            method,
            url=f"{self.url}/{service}",
            json=json,
            timeout=self.time_out
        ) as response:
            response_json = await response.json()
            return response_json['result']