from balepy.objects import HTTPMethod

import balepy


class SendAudio:

    async def send_audio(
            self: 'balepy.Client',
            chat_id: str,
            audio: str,
            caption=None,
            reply_to_message_id=None,
            reply_markup=None
    ):
        params = {
            'chat_id': chat_id,
            'audio': audio,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }

        return await self.api.execute(name="sendAudio", method=HTTPMethod.POST, data=params)
