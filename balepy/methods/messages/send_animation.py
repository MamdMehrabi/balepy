from balepy.objects import HTTPMethod

import balepy


class SendAnimation:

    async def send_animation(
            self: "balepy.Client",
            chat_id: str,
            animation: str,
            reply_to_message_id=None,
            reply_markup=None
    ):
        params = {
            'chat_id': chat_id,
            'animation': animation,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }

        return await self.api.execute(name='sendAnimation', method=HTTPMethod.POST, data=params)
