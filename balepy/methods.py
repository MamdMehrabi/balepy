from requests import post, get


class Methods:

    async def _send_message(self, chat_id: str, text: str, reply_markup: int = None, reply_to_message_id: int = None) -> dict:
        json = {
            'chat_id': chat_id,
            'text': text,
            'reply_markup': reply_markup,
            'reply_to_message_id': reply_to_message_id
        }
        responce = post(f'{self.url}{self.token}/sendMessage', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])
        else:
            return responce


    async def _edit_message(
            self,
            chat_id: str,
            text: str,
            message_id: int,
            reply_markup: int = None
    ):
        json = {
            'chat_id': chat_id,
            'text': text,
            'reply_to_message_id': message_id,
            'reply_markup': reply_markup
        }
        responce = post(f'{self.url}{self.token}/EditMessageText', json=json).json()
        if not responcep['ok']:
            raise Exception(responce['description'])
        else:
            return responce


    async def _delete_message(self, chat_id: str, message_id: int):
        json = {
            'chat_id': chat_id, 'reply_to_message_id': message_id
        }
        responce = post(f'{self.url}{self.token}/deleteMessage', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])
        else:
            return responce


    async def _send_contact(
            self,
            chat_id: str,
            phone_number: int,
            first_name: str,
            last_name: str = None,
            reply_to_message_id: int = None
    ):
        json = {
            'chat_id': chat_id,
            'phone_number': phone_number,
            'first_name': first_name,
            'last_name': last_name,
            'reply_to_message_id': reply_to_message_id
        }
        responce = post(f'{self.url}{self.token}/sendContact', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])
        else:
            return responce


    async def _set_webhook(self, url: str):
        json = {
            'url': url
        }
        responce = post(f'{self.url}{self.token}/setWebhook', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])
        else:
            return responce


    async def _delete_webhook(self):
        responce = post(f'{self.url}{self.token}/deleteWebhook').json()
        return responce


    async def _get_me(self):
        responce = get(f'{self.url}{self.token}/getme').json()
        return responce


    async def _get_username_by_id(self, chat_id: str, user_id: str):
        json = {
            'chat_id': chat_id, 'user_id': user_id
        }
        responce = get(f'{self.url}{self.token}/getChatMember', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])
        return responce


    async def _get_chat(self, chat_id: str):
        json = {
            'chat_id': chat_id
        }
        responce = get(f'{self.url}{self.token}/getchat', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])
        else:
            return responce


    async def _get_chat_join_link(self, chat_id: str):
        json = {
            'chat_id': chat_id
        }
        responce = get(f'{self.url}{self.token}/getchat', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])
        else:
            return responce['result']['invite_link']


    async def _get_updates(self, offset: int = 0, limit: int = 0):
        json = {
            'offset': offset, 'limit': limit
        }
        responce = get(f'{self.url}{self.token}/getupdates', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])
        else:
            return responce


    async def _get_chat_administrators(self, chat_id: str, just_get_id: bool = False):
        json = {
            'chat_id': chat_id
        }
        responce = get(f'{self.url}{self.token}/getChatAdministrators', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])

        elif just_get_id:
            results = []
            for user in responce['result']:
                results.append(user['user']['id'])
            return results
        else:
            return responce


    async def _get_chat_creator(self, chat_id: str, just_get_id: str):
        json = {
            'chat_id': chat_id
        }
        responce = get(f'{self.url}{self.token}/getChatAdministrators', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])
        elif just_get_id:
            return responce['result'][0]['user']['id']
        else:
            return responce


    async def _get_chat_members_count(self, chat_id: str):
        json = {
            'chat_id': chat_id
        }
        responce = get(f'{self.url}{self.token}/getChatMembersCount', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])
        else:
            return responce['result']


    async def _get_chat_member(self, chat_id: str, user_id: str):
        json = {
            'chat_id': chat_id, 'user_id': user_id
        }
        responce = get(f'{self.url}{self.token}/getChatMember', json=json).json()
        if not responce['ok']:
            raise Exception(responce['description'])
        else:
            return responce
