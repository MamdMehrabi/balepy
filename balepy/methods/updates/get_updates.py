from balepy.objects import HTTPMethod

import balepy

from typing import Optional


class GetUpdates:

    async def get_updates(
            self: "balepy.Client",
            offset: Optional[int] = -1,
            limit: Optional[int] = 1
    ):
        params: dict = {
            "offset": offset,
            "limit": limit
        }
        response_data = await self.api.execute(name="getUpdates", method=HTTPMethod.POST, data=params)
        return response_data["result"]
