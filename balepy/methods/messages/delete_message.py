from balepy.objects import HTTPMethod

import balepy


class DeleteMessage:

    async def delete_message(
            self: "balepy.Client",
            chat_id: str,
            message_id: str
    ):
        params = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        return await self.api.execute(name="deleteMessage", method=HTTPMethod.POST, data=params)
