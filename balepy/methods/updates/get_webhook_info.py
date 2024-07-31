from balepy.objects import HTTPMethod

import balepy


class GetWebhookInfo:

    """
    for get status webhook
    """

    async def get_webhook_info(
            self: "balepy.Client",
            url: str
    ):
        params = {
            'url': url
        }
        return await self.api.execute(name="getWebhookInfo", method=HTTPMethod.POST, data=params)
