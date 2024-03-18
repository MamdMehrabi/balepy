from balepy.util import message

from asyncio import run
import requests
import aiohttp

class Client(message):

    def __init__(self, token: str, timeout: float = 20) -> None:
        self.token: str = token
        self.timeout: float = timeout
        self.form_data = aiohttp.FormData()

        if not token:
            raise ValueError('`token` did\'t passed')
    

    async def execute(self, method: str, data: dict = None) -> dict:
        url: str = f'https://tapi.bale.ai/bot{self.token}/{method}'
        async with aiohttp.ClientSession() as session:
            async with session.request('post', url=url, data=data, timeout=self.timeout) as r:
                return await r.json()

    def _get_updates(self, data: dict) -> dict:
        url: str = f'https://tapi.bale.ai/bot{self.token}/getupdates'
        with requests.session() as session:
            with session.request('post', url=url, data=data, timeout=self.timeout) as r:
                return r.json()

    async def request(self, method: str, data: dict = None) -> dict:
        try:
            return await self.execute(method=method, data=data)
        except Exception as err:
            print(__file__, err, __file__)

    def on_message(self, Filters = None):
        '''Use this method to receive updates
        Example:
            from balepy import Client
            import asyncio

            client = Client('token', timeout=10)
            def main():
                for update in client.on_message():
                    print(update.text)

            asyncio.run(main())
        '''
        payload: dict = {
            'offset': -1, 'limit': 100
        }
        while True:
            update = self._get_updates(data=payload)
            payload['offset'] = 1
            if (update != None) and (update['ok']) and (update['result'] != []):
                break

        payload['offset'], payload['limit'] = update['result'][len(update['result'])-1]['update_id'], 1
        while True:
            responce = self._get_updates(data=payload)
            if responce != None and responce['result'] != []:
                payload['offset'] += 1
                yield message(responce['result'][0])

    @staticmethod
    async def send_message(
            chat_id: str | int,
            text: str,
            reply_markup: int = None,
            reply_to_message_id: int = None
    ) -> dict:
        '''Use this method to send text messages
        :param chat_id:
            The ID of the group you can send messages to. requirement**
        :param text:
            You can only send between 1 and 4096 characters*. requirement**
        :param reply_markup:
            Additional features of the arm user interface. optional**
        :param reply_to_message_id:
            The ID of the original message, if the message is a reply. optional**
        :return:
            If successful, the sent message will be returned.
        '''
        payload: dict = {
            'chat_id': chat_id,
            'text': text,
            'reply_markup': reply_markup,
            'reply_to_message_id': reply_to_message_id
        }
        return await self.request('sendmessage', data=payload)

    async def edit_message(
            self,
            chat_id: str | int,
            text: str,
            message_id: int,
            reply_markup: int = None
    ) -> dict:
        payload: dict = {
            'chat_id': chat_id,
            'text': text,
            'reply_to_message_id': message_id,
            'reply_markup': reply_markup
        }
        return await self.request('editmessage', data=payload)


    async def forward_message(
            self,
            chat_id: str | int,
            from_chat_id: str | int,
            message_id: int
    ) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id
        }
        return await self.request('forwardmessage', data=payload)


    async def delete_message(self, chat_id: str | int, message_id: int) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'reply_to_message_id': message_id
        }
        return await self.request('deletemessage', data=payload)


    async def send_contact(
            self,
            chat_id: str | int,
            phone_number: int,
            first_name: str,
            last_name: str = None,
            reply_to_message_id: int = None
    ) -> dict:
        '''This method is used to send a phone contact
        :param chat_id:
            The ID of the group you can send messages to. requirement**
        :param phone_number:
            contact number. requirement**
        :param first_name:
            Contact's first name. requirement**
        :param last_name:
            Last name of the addressee. optional**
        :param reply_to_message_id:
            The ID of the original message, if the message is a reply. optional**
        :return:
            On successful execution, the sent message is returned as output.
        '''
        payload: dict = {
            'chat_id': chat_id,
            'phone_number': phone_number,
            'first_name': first_name,
            'last_name': last_name,
            'reply_to_message_id': reply_to_message_id
        }
        return await self.request('sendcontact', data=payload)


    async def send_photo(
            self,
            chat_id: str | int,
            from_chat_id: str | int,
            file: str | bytes,
            caption: str = None,
            reply_to_message_id: int = None,
            reply_markup: int = None
    ) -> dict:
        self.form_data.add_field('photo', open(file, 'rb'))
        self.form_data.add_field('chat_id', str(chat_id))
        self.form_data.add_field('caption', caption) if caption != None else caption
        self.form_data.add_field(
            'reply_to_message_id', str(reply_to_message_id)
        ) if reply_to_message_id != None else reply_to_message_id
        return await self.request('sendphoto', data=self.form_data)


    async def send_audio(
            self,
            chat_id: str | int,
            file: str | bytes,
            caption: str = None,
            reply_to_message_id: int = None,
            reply_markup: str = None
    ) -> dict:
        self.form_data.add_field('audio', open(file, 'rb'))
        self.form_data.add_field('chat_id', str(chat_id))
        self.form_data.add_field('caption', caption) if caption != None else caption
        self.form_data.add_field(
            'reply_to_message_id', str(reply_to_message_id)
        ) if reply_to_message_id != None else reply_to_message_id
        return await self.request('sendaudio', data=self.form_data)


    async def send_document(
            self,
            chat_id: str | int,
            file: str | bytes,
            caption: str = None,
            reply_to_message_id: int = None,
            reply_markup: int = None
    ) -> dict:
        '''This method is used to send public files.
        :param chat_id:
            Conversation ID. requirement**
        :param file:
            Document file to be sent. The maximum file size is 50 MB. requirement**
        :param caption:
            Subtitle of the document, between 0 and 1024 characters. optional**
        :param reply_to_message_id:
            The ID of the original message, if the message is a reply. optional**
        :param reply_markup:
            Additional features of the arm user interface. optional**
        :return:
            If successful, the sent message will be returned
        '''
        self.form_data.add_field('document', open(file, 'rb'))
        self.form_data.add_field('chat_id', str(chat_id))
        self.form_data.add_field('caption', caption) if caption != None else caption
        self.form_data.add_field(
            'reply_to_message_id', str(reply_to_message_id)
        ) if reply_to_message_id != None else reply_to_message_id
        return await self.request('senddocument', data=self.form_data)


    async def send_animation(
            self,
            chat_id: str | int,
            file: str | bytes,
            reply_to_message_id: int = None,
            caption: str = None,
            reply_markup: int = None
    ) -> dict:
        '''This method is used to send animation files (GIF video or H.264/MPEG-4 AVC without sound)'''
        self.form_data.add_field('animation', open(file, 'rb'))
        self.form_data.add_field('chat_id', str(chat_id))
        self.form_data.add_field('caption', caption) if caption != None else caption
        self.form_data.add_field(
            'reply_to_message_id', str(reply_to_message_id)
        ) if reply_to_message_id != None else reply_to_message_id
        return await self.request('sendanimation', data=self.form_data)



    async def send_voice(
            self,
            chat_id: str | int,
            file: str | bytes,
            caption: str,
            reply_to_message_id: int = None,
            reply_markup: int = None
    ) -> dict:
        self.form_data.add_field('voice', open(file, 'rb'))
        self.form_data.add_field('chat_id', str(chat_id))
        self.form_data.add_field('caption', caption) if caption != None else caption
        self.form_data.add_field(
            'reply_to_message_id', str(reply_to_message_id)
        ) if reply_to_message_id != None else reply_to_message_id
        return await self.request('sendvoice', data=self.form_data)


    async def send_location(
            self,
            chat_id: str | int,
            latitude: float,
            longitude: float,
            horizontal_accuracy: float,
            reply_to_message_id: int = None,
            reply_markup: int = None
    ) -> dict:
        '''This method is used to send a map point
        :param chat_id:
            Conversation ID. requirement**
        :param latitude:
            The latitude of the location. requirement**
        :param longitude
            The longitude of the location. requirement**
        :param horizontal_accuracy
            The radius of uncertainty for a spatial point
            is measured in meters and is a number between 0 and 1500. optional**
        :param reply_to_message_id:
            The ID of the original message, if the message is a reply. optional**
        :param reply_markup:
            Additional features of the arm user interface. optional**
        :return:
            On successful execution, the sent message is returned as output.
        '''
        payload: dict = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'horizontal_accuracy': horizontal_accuracy,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return await self.request('sendlocation', data=payload)


    async def set_webhook(self, url: str) -> dict:
        '''This method is used to specify an outgoing webhook URL'''
        payload: dict = {
            'url': url
        }
        return await self.request('setwebhook', data=payload)


    async def delete_webhook(self) -> dict:
        return await self.request(method='deletewebhook')


    async def get_webhook_info(self) -> dict:
        '''Use this method to get the current state of the webhook'''
        return await self.request(data='getwebhookinfo')


    async def webhook_info(self, url: str) -> dict:
        '''Displays the current state of a webhook'''
        payload: dict = {
            'url': url
        }
        return await self.request('webhookinfo', data=payload)

    async def get_me(self) -> dict:
        '''get bot account information'''
        return await self.request(method='getme')


    async def get_chat(self, chat_id: str) -> dict:
        '''This method is used to get up-to-date information
        about the conversation (current username for one-to-one conversations,
        current username of a user, group or channel).
        :param chat_id:
            Conversation ID. requirement**
        :return:
            Returns a Chat object on success.
        '''
        payload: dict = {
            'chat_id': chat_id
        }
        return await self.request('getchat', data=payload)


    async def leave_chat(self, chat_id: str) -> dict:
        '''This method is used for the arm to leave a group, group or channel
        :param chat_id:
            Conversation ID. requirement**
        :return:
            If successful, its output is True.
        '''
        payload: dict = {
            'chat_id': chat_id
        }
        return await self.request('leavechat', data=payload)


    async def get_updates(self, offset: int = 0, limit: int = 0) -> dict:
        payload: dict = {
            'offset': offset, 'limit': limit
        }
        return await self.request('getupdates', data=payload)


    async def get_chat_administrators(self, chat_id: str, just_get_id: bool = False) -> dict:
        payload: dict = {
            'chat_id': chat_id
        }
        responce = self.request('getchatadministrators', data=payload)

        if just_get_id:
            ids = []
            for user in responce['result']:
                ids.append(user['user']['id'])

            return await ids
        else:
            return await responce


    async def get_chat_members_count(self, chat_id: str) -> dict:
        payload: dict = {
            'chat_id': chat_id
        }
        return await self.request('getchatmemberscount', data=payload)


    async def get_chat_member(self, chat_id: str, user_id: str) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return await self.request('getchatmember', data=payload)


    async def set_chat_photo(self, chat_id: str | int, photo = str | bytes) -> dict:
        files: dict = {
            'photo': open(photo, 'rb')
        }
        values: dict = {
            'chat_id': chat_id
        }
        return await self.request('setchatphoto', data=values, files=files)


    async def ban_chat_member(self, chat_id: str | int, user_id: str | int) ->  dict:
        payload: dict = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return await self.request('banchatmember', data=payload)


    async def un_ban_chat_member(self, chat_id: str | int, user_id: str | int) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return await self.request('unbanchatmember', data=payload)


    async def get_file(self, file_id: str) -> dict:
        '''This method is used to get the basic information
        of a file and prepare it for download.
        :param file_id:
            ID of the file whose information should be received. requirement**
        :return:
            Returns a File object on successful execution
        '''
        payload: dict = {
            'file_id': file_id
        }
        return await self.request('getfile', data=payload)