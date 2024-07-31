from balepy.objects import HTTPMethod

import balepy


class EditMessageText:

    async def edit_message_text(
            self: "balepy.Client",
            text: str,
            chat_id: str = None,
            message_id: int = None,
            reply_markup=None
    ):
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
            'text': text,
            'reply_markup': reply_markup
        }
        return await self.api.execute(name='editMessageText', method=HTTPMethod.POST, data=params)
