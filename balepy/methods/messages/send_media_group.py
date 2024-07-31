from balepy.objects import HTTPMethod

import balepy


class SendMediaGroup:

    async def send_media_group(
            self: "balepy.Client",
            chat_id: str,
            media,
            reply_to_message_id=None
    ):
        params = {
            'chat_id': chat_id,
            'media': media,
            'reply_to_message_id': reply_to_message_id
        }
        return await self.api.execute(name="sendMediaGroup", method=HTTPMethod.POST, data=params)
