from typing import Optional

from balepy.http import API
from balepy.types import Updates
from balepy.methods import Methods


class Client(Methods):

    def __init__(
            self,
            name: str,
            bot_token: str,
            timeout: Optional[int] = 20,
            max_retry: Optional[int] = 3,
            base_url: Optional[str] = None,
            proxies: Optional[str] = None
    ):
        """
        Initialize the Client instance.

        :param name: The name of the bot.
        :param bot_token: The bot token for authentication.
        :param base_url: The base URL for the Bale API.
        :param max_retry: The number of attempts by the client to send the request to the server.
        """
        self.name = name
        self.bot_token = bot_token
        self.timeout = timeout
        self.max_retry = max_retry
        self.base_url = base_url
        self.proxies = proxies
        self.api = API(client=self)

    def on_message(self, func):
        async def decorator():
            async for update in self.process_update():
                await func(update)
        return decorator

    async def process_update(self):
        offset = -1

        while True:
            update = await self.get_updates(offset=offset)

            offset = 1
            if not isinstance(update, str) and not len(update) == 0:
                break

        offset = update[-1]["update_id"] + 1
        while True:
            last_update = await self.get_updates(offset=offset)

            if not isinstance(last_update, str) and not len(last_update) == 0:
                offset += 1
                yield Updates(last_update[0])
