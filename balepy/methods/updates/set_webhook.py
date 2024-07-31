from balepy.objects import HTTPMethod

import balepy


class SetWebhook:

    '''
    this method for get updates on webhook
    '''

    async def set_webhook(
            self: "balepy.Client",
            url: str
    ):
        params = {
            'url': url
        }
        return await self.api.execute(name="setWebhook", method=HTTPMethod.POST, data=params)
