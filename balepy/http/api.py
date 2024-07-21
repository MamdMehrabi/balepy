from balepy.objects import HTTPMethod, APIResult
from balepy.types import Results, Updates
from balepy.errors import APIError

from typing import Optional

import aiohttp


class API:

    BASE_URL = "https://tapi.bale.ai"

    def __init__(self, client=None):
        self.client = client

    async def execute(
            self,
            name: str,
            method: Optional[str] = "GET",
            data: Optional[dict] = None,
    ):
        """
        Execute asynchronous request to BaleAPI
        """
        base_url = self.client.base_url or self.BASE_URL
        path = f"/bot{self.client.bot_token}/" + name
        timeout = aiohttp.ClientTimeout(total=self.client.timeout)
        for _ in range(self.client.max_retry):
            async with aiohttp.ClientSession(base_url=base_url, timeout=timeout) as self.session:
                async with self.session.request(method=method, url=path) as response:
                    response_data = await response.json()
                    if response_data.get("ok"):
                        response_data.pop("ok")
                        return response_data
                    error_code = response_data.get("error_code")
                    description = response_data.get("description")
                    raise APIError(description, error_code)
