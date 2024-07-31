from balepy.objects import HTTPMethod

import balepy


class CopyMessage:

    async def copy_message(
            self: "balepy.Client",
            chat_id: str,
            from_chat_id: str,
            message_id: int
    ):
        params = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id
        }
        return await self.api.execute(name="copyMessage", method=HTTPMethod.POST, data=params)
