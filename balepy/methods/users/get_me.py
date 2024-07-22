from balepy.objects import HTTPMethod
from balepy.types import Results

import balepy


class GetMe:

    async def get_me(self: "balepy.Client"):
        return await self.api.execute(name="getme", method=HTTPMethod.GET)
