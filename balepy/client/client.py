from typing import Optional

from balepy.http import API
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
        :param max_retry:
        """
        self.bot_token = bot_token
        self.timeout = timeout
        self.max_retry = max_retry
        self.base_url = base_url
        self.proxies = proxies
        self.api = API(client=self)
