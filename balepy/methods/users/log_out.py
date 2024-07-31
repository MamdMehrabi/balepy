from balepy.objects import HTTPMethod

import balepy


class LogOut:

    async def log_out(self: 'balepy.Client'):
        return await self.api.execute(name="logout", method=HTTPMethod.GET)
