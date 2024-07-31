from balepy.objects import HTTPMethod

import balepy

class SendVoice:

    async def send_voice(
            self: "balepy.Client",
            chat_id: str,
            voice: str,
            caption=None,
            reply_to_message_id=None,
            reply_markup=None
    ):
        params = {
            'chat_id': chat_id,
            'voic': voice,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }

        return await self.api.execute(name='sendVoice', method=HTTPMethod.POST, data=params)
