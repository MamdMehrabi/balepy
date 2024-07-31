from balepy.objects import HTTPMethod

import balepy


class SendPhoto:

    async def send_photo(
            self: "balepy.Client",
            chat_id: str,
            from_chat_id: str,
            photo: str,
            caption=None,
            reply_to_message_id=None,
            reply_markup=None
    ):
        params = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'photo': photo,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return await self.api.execute(name="sendPhoto", method=HTTPMethod.POST, data=params)
