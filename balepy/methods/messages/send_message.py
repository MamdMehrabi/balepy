from balepy.objects import HTTPMethod

import balepy


class SendMessage:

    async def send_message(
            self: "balepy.Client",
            chat_id: str,
            text: str,
            reply_to_message_id: int = None,
            reply_markup=None
    ):
        params = {
            "chat_id": chat_id,
            "text": text,
            "reply_to_message_id": reply_to_message_id,
            "reply_markup": reply_markup
        }
        return await self.api.execute(name="sendMessage", method=HTTPMethod.POST, data=params)
