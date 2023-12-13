from .methods import Methods


class Client():

    def __init__(self, token: str):
        '''Refer to this ID to receive the token >>> @botfather'''
        self.token = token.split(':')[-1]
        self.url = 'https://tapi.bale.ai/bot'


    # ---------------- Messages Methods ----------------

    async def send_message(
            self,
            chat_id: str,
            text: str,
            reply_markup: int = None,
            reply_to_message_id: int = None
    ) -> dict:
        '''
        :param chat_id (str):
            The ID of the group you can send messages to

        :param text:
            The text you want to send

        :param reply_markup:
            pass

        :param reply_to_message_id (str):
            reply to message id Defaults to None.

        :return:
            status: True or False
        '''
        return await Methods._send_message(self, chat_id, text, reply_markup, reply_to_message_id)


    async def edit_message(
            self,
            chat_id: str,
            text: str,
            message_id: int,
            reply_markup: int = None
    ) -> dict:
        return await Methods._edit_message(self, chat_id, text, message_id, reply_markup)


    async def delete_message(self, chat_id: str, message_id: int) -> dict:
        return await Methods._delete_message(self, chat_id, message_id)


    async def send_contact(
            self,
            chat_id: str,
            phone_number: int,
            first_name: str,
            last_name: str = None,
            reply_to_message_id:int = None
    ) -> dict:
        return await Methods._send_contact(self, chat_id, phone_number, first_name, last_name, reply_to_message_id)


    async def set_webhook(self, url: str) -> dict:
        return await Methods._set_webhook(self, url)


    async def delete_webhook(self) -> dict:
        return await Methods._delete_webhook(self)


    # ---------------- Users Methods ----------------

    async def get_me(self) -> dict:
        '''Get bot account information'''
        return await Methods._get_me(self)


    async def get_username_by_id(self, chat_id: str, user_id: str) -> dict:
        return await Methods._get_username_by_id(self, chat_id, user_id)


    # ---------------- Chats Methods ----------------

    async def get_chat(self, chat_id: str) -> dict:
        return await Methods._get_chat(self, chat_id)


    async def get_chat_join_link(self, chat_id: str) -> dict:
        return await Methods._get_chat_join_link(self, chat_id)


    async def get_updates(self, offset: int = 0, limit: int = 0) -> dict:
        return await Methods._get_updates(self, offset, limit)


    async def get_chat_administrators(self, chat_id: str, just_get_id: bool = False) -> dict:
        return await Methods._get_chat_administrators(self, chat_id, just_get_id)


    async def get_chat_creator(self, chat_id: str, just_get_id: str) -> dict:
        return await Methods._get_chat_creator(self, chat_id, just_get_id)


    async def get_chat_members_count(self, chat_id: str) -> dict:
        return await Methods._get_chat_members_count(self, chat_id)


    async def get_chat_member(self, chat_id: str, user_id: str) -> dict:
        return await Methods._get_chat_member(self, chat_id, user_id)
