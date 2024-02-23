from .util import message
import requests


class Client:

    def __init__(self, token: str, timeout: float = 20) -> None:
        self.token: str = token
        self.timeout: float = timeout

        if not token:
            raise ValueError('`token` did\'t passed')

    def execute(self, method: str, data: dict = None) -> dict:
        url: str = f'https://tapi.bale.ai/bot{self.token}/{method}'
        with requests.session() as session:
            with session.request('post', url=url, data=data, timeout=self.timeout) as r:
                return r.json()

    def request(self, method: str, data: dict = None) -> dict:
        try:
            return self.execute(method=method, data=data)
        except Exception as err:
            print(__file__, err, __file__)

    def on_message(self):
        '''Use this method to receive updates
        Example:
            from balepy import Client

            client = Client('token', timeout=10)
            def main():
                for update in client.on_message():
                    print(update.text)

            main()
        '''
        payload: dict = {
            'offset': -1, 'limit': 100
        }
        while True:
            update = self.request('getupdates', data=payload)
            payload['offset'] = 1
            if (update != None) and (update['ok']) and (update['result'] != []):
                break

        payload['offset'] = update['result'][len(update['result'])-1]['update_id'] + 1
        payload['limit'] = 1
        while True:
            responce = self.request('getupdates', data=payload)
            if responce != None and responce['result'] != []:
                payload['offset'] += 1
                yield message(responce['result'][0])


    async def send_message(
            self,
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
        return self.request('sendmessage', data=payload)

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
        return self.request('editmessage', data=payload)


    async def forward_message(
            self,
            chat_id: str | int,
            from_chat_id: str | int,
            message_id: int
    ) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id
        }
        return self.request('forwardmessage', json=payload)


    async def delete_message(self, chat_id: str | int, message_id: int) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'reply_to_message_id': message_id
        }
        return self.request('deletemessage', data=payload)


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
        return self.request('sendcontact', data=payload)


    async def send_photo(
            self,
            chat_id: str | int,
            from_chat_id: str | int,
            file: str | bytes,
            caption: str = None,
            reply_to_message_id: int = None,
            reply_markup: int = None
    ) -> dict:
        files: dict = {
            'photo': open(file, 'rn')
        }
        values: dict = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return requests.request(
            'post',
            url=f'https://tapi.bale.ai/bot{self.token}/sendphoto',
            data=values, files=files, timeout=self.timeout
        )


    async def send_audio(
            self,
            chat_id: str | int,
            file: str | bytes,
            caption: str = None,
            reply_to_message_id: int = None,
            reply_markup: str = None
    ) -> dict:
        files: dict = {
            'audio': open(file, 'rb')
        }
        values: dict = {
            'chat_id': chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return requests.request(
            'post',
            url=f'https://tapi.bale.ai/bot{self.token}/audio',
            data=values, files=files, timeout=self.timeout
        )


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
        files: dict = {
            'document': open(file, 'rb')
        }
        values: dict = {
            'chat_id': chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return requests.request(
            'post',
            url=f'https://tapi.bale.ai/bot{self.token}/senddocument',
            data=values, files=files, timeout=self.timeout
        )


    async def send_animation(
            self,
            chat_id: str | int,
            file: str | bytes,
            reply_to_message_id: int = None,
            reply_markup: int = None
    ) -> dict:
        '''This method is used to send animation files (GIF video or H.264/MPEG-4 AVC without sound)'''
        files: dict = {
            'animation': open(file, 'rb')
        }
        values: dict = {
            'chat_id': chat_id,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return requests.request(
            'post',
            url=f'https://tapi.bale.ai/bot{self.token}/sendanimation',
            data=values, files=files, timeout=self.timeout
        )


    async def send_voice(
            self,
            chat_id: str | int,
            file: str | bytes,
            caption: str,
            reply_to_message_id: int = None,
            reply_markup: int = None
    ) -> dict:
        files: dict = {
            'voice': open(file, 'rb')
        }
        values: dict = {
            'chat_id': chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return requests.request(
            'post',
            url=f'https://tapi.bale.ai/bot{self.token}/sendvoice',
            data=values, files=files, timeout=self.timeout
        )


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
        return requests.request(
            'post',
            url=f'https://tapi.bale.ai/bot{self.token}/sendlocation',
            data=values, files=files, timeout=self.timeout
        )


    async def set_webhook(self, url: str) -> dict:
        '''This method is used to specify an outgoing webhook URL'''
        payload: dict = {
            'url': url
        }
        return self.request('setwebhook', data=payload)


    async def delete_webhook(self) -> dict:
        return self.request(method='deletewebhook')


    async def get_webhook_info(self) -> dict:
        '''Use this method to get the current state of the webhook'''
        return self.request(data='getwebhookinfo')


    async def webhook_info(self, url: str) -> dict:
        '''Displays the current state of a webhook'''
        payload: dict = {
            'url': url
        }
        return self.request('webhookinfo', data=payload)


    async def get_me(self) -> dict:
        '''get bot account information'''
        return self.request(method='getme')


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
        return self.request('getchat', data=payload)


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
        return self.request('leavechat', data=payload)


    async def get_updates(self, offset: int = 0, limit: int = 0) -> dict:
        payload: dict = {
            'offset': offset, 'limit': limit
        }
        return self.request('getupdates', data=payload)


    async def get_chat_administrators(self, chat_id: str, just_get_id: bool = False) -> dict:
        payload: dict = {
            'chat_id': chat_id
        }
        responce = self.request('getchatadministrators', data=payload)

        if just_get_id:
            ids = []
            for user in responce['result']:
                ids.append(user['user']['id'])

            return ids
        else:
            return responce



    async def get_chat_members_count(self, chat_id: str) -> dict:
        payload: dict = {
            'chat_id': chat_id
        }
        return self.request('getchatmemberscount', data=payload)


    async def get_chat_member(self, chat_id: str, user_id: str) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return self.request('getchatmember', data=payload)


    async def set_chat_photo(self, chat_id: str | int, photo = str | bytes) -> dict:
        files: dict = {
            'photo': open(file, 'rb')
        }
        values: dict = {
            'chat_id': chat_id
        }
        return self.request('setchatphoto', data=values, files=files)


    async def ban_chat_member(self, chat_id: str | int, user_id: str | int) ->  dict:
        payload: dict = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return self.request('banchatmember', data=payload)


    async def un_ban_chat_member(self, chat_id: str | int, user_id: str | int) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return self.request('unbanchatmember', data=payload)


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
        return self.request('getfile', data=payload)
