from balepy.objects import HTTPMethod

import balepy


class SendDocument:

    async def send_document(
            self: 'balepy.Client',
            chat_id: str,
            document: str,
            caption=None,
            reply_to_message_id=None,
            reply_markup=None
    ):
        params = {
            'chat_id': chat_id,
            'document': document,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }

        return await self.api.execute(name="sendDocument", method=HTTPMethod.POST, data=params)
