from balepy.objects import HTTPMethod

import balepy


class SendVideo:

    async def send_video(
            self: 'balepy.Client',
            chat_id: str,
            video: str,
            caption=None,
            reply_to_message_id=None,
            reply_markup=None
    ):
        params = {
            'chat_id': chat_id,
            'video': video,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }

        return await self.api.execute(name='sendVideo', method=HTTPMethod.POST, data=params)
