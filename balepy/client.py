from requests import session

class Client:

    def __init__(self, token: str, timeout: float = 20) -> None:
        self.token = token
        self.timeout = timeout
        self.session = session()

        if not token:
            raise ValueError('`token` did\'t passed')

    @property
    def url(self):
        return f'https://tapi.bale.ai/bot{self.token}'


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
        payload = {
            'chat_id': chat_id,
            'text': text,
            'reply_markup': reply_markup,
            'reply_to_message_id': reply_to_message_id
        }
        return self.session.request(
            'post', f'{self.url}/sendmessage', timeout=self.timeout, json=payload).json()


    async def edit_message(
            self,
            chat_id: str | int,
            text: str,
            message_id: int,
            reply_markup: int = None
    ) -> dict:
        payload = {
            'chat_id': chat_id,
            'text': text,
            'reply_to_message_id': message_id,
            'reply_markup': reply_markup
        }
        return self.session.request(
            'post', f'{self.url}/editmessage', timeout=self.timeout, json=payload).json()


    async def forward_message(
            self,
            chat_id: str | int,
            from_chat_id: str | int,
            message_id: int
    ) -> dict:
        payload = {
            'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id
        }
        return self.session.request(
            'get', f'{self.url}/forwardmessage', timeout=self.timeout, json=payload).json()


    async def delete_message(self, chat_id: str | int, message_id: int) -> dict:
        payload = {
            'chat_id': chat_id, 'reply_to_message_id': message_id
        }
        return self.session.request(
            'post', f'{self.url}/deletemessage', timeout=self.timeout, json=payload).json()


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
        payload = {
            'chat_id': chat_id,
            'phone_number': phone_number,
            'first_name': first_name,
            'last_name': last_name,
            'reply_to_message_id': reply_to_message_id
        }
        return self.session.request(
            'post', f'{self.url}/sendcontact', timeout=self.timeout, json=payload).json()


    async def send_photo(
            self,
            chat_id: str | int,
            from_chat_id: str | int,
            file: str | bytes,
            caption: str = None,
            reply_to_message_id: int = None,
            reply_markup: int = None
    ) -> dict:
        '''Use this method to send images
        :param chat_id:
            Conversation ID. requirement**
        :param file:
            Photo file to be sent. requirement**
        :param caption:
            Photo file subtitle, between 0 and 1024 characters. optional**
        :param reply_to_message_id:
            The ID of the original message, if the message is a reply. optional**
        :param reply_markup:
            Additional features of the arm user interface. optional**
        :return:
            On successful execution, the sent message is returned.
        '''
        files = {'photo': open(file, 'rb')}
        values = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.session.request(
            'post', f'{self.url}/sendphoto', timeout=self.timeout, data=values, files=files).json()


    async def send_audio(
            self,
            chat_id: str | int,
            file: str | bytes,
            caption: str = None,
            reply_to_message_id: int = None,
            reply_markup: str = None
    ) -> dict:
        '''If you want yes clients to display these files in the music player, use this method to send audio files.
        :param chat_id:
            Conversation ID. requirement**
        :param file:
            Audio file to be sent. The maximum file size is 50 MB. requirement**
        :param caption:
            Audio file subtitle, between 0 and 1024 characters. optional**
        :param reply_to_message_id:
            The ID of the original message, if the message is a reply. optional**
        :param reply_markup:
            Additional features of the arm user interface. optional**
        :return:
            If successful, the sent message will be returned
        '''
        files = {'audio': open(file, 'rb')}
        values = {
            'chat_id': chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.session.request(
            'post', f'{self.url}/sendaudio', timeout=self.timeout, data=values, files=files).json()


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
        files = {
            'document': open(file, 'rb')
        }
        values = {
            'chat_id': chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.session.request(
            'post', f'{self.url}/senddocument', timeout=self.timeout, data=values, files=files).json()


    async def send_animation(
            self,
            chat_id: str | int,
            file: str | bytes,
            reply_to_message_id: int = None,
            reply_markup: int = None
    ) -> dict:
        '''This method is used to send animation files (GIF video or H.264/MPEG-4 AVC without sound).
        :param chat_id:
            Conversation ID. requirement**
        :param file:
            Animation file to be sent. The maximum file size is 50 MB. requirement**
        :param caption:
            Subtitle of the voice, between 0 and 1024 characters. optional**
        :param reply_to_message_id:
            The ID of the original message, if the message is a reply. optional**
        :param reply_markup:
            Additional features of the arm user interface. optional**
        :return:
            If successful, the sent message will be returned
        '''
        files = {
            'animation': open(file, 'rb')
        }
        values = {
            'chat_id': chat_id,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.session.request(
            'post', f'{self.url}/sendanimation', timeout=self.timeout, data=values, files=files).json()


    async def send_voice(
            self,
            chat_id: str | int,
            file: str | bytes,
            caption: str,
            reply_to_message_id: int = None,
            reply_markup: int = None
    ) -> dict:
        '''If you want yes clients to display the file as an audio message, use this method to send audio files.
        :param chat_id:
            Conversation ID. requirement**
        :param file:
            Voice file to be sent. The maximum file size is 50 MB. requirement**
        :param reply_to_message_id:
            The ID of the original message, if the message is a reply. optional**
        :param reply_markup:
            Additional features of the arm user interface. optional**
        :return:
            If successful, the sent message will be returned
        '''
        files = {
            'voice': open(file, 'rb')
        }
        values = {
            'chat_id': chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.session.request(
            'post', f'{self.url}/sendvoice', timeout=self.timeout, data=values, files=files).json()


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
        payload = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'horizontal_accuracy': horizontal_accuracy,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.session.request(
            'post', f'{self.url}/sendLocation', timeout=self.timeout, json=payload).json()


    async def set_webhook(self, url: str) -> dict:
        '''This method is used to specify an outgoing webhook URL'''
        payload = {
            'url': url
        }
        return self.session.request(
            'post', f'{self.url}/setwebhook', timeout=self.timeout, json=payload).json()


    async def delete_webhook(self) -> dict:
        return self.session.request(
            'post', f'{self.url}/deletewebhook', timeout=self.timeout).json()


    async def get_webhook_info(self) -> dict:
        '''Use this method to get the current state of the webhook'''
        return self.session.request(
            'get', f'{self.url}/getwebhookinfo', timeout=self.timeout).json()


    async def webhook_info(self, url: str) -> dict:
        '''Displays the current state of a webhook'''
        payload = {
            'url': url
        }
        return self.session.request(
            'get', f'{self.url}/webhookinfo', timeout=self.timeout, json=payload).json()


    async def get_me(self) -> dict:
        '''get bot account information'''
        return self.session.request('get', f'{self.url}/getme', timeout=self.timeout).json()


    async def get_chat(self, chat_id: str) -> dict:
        '''This method is used to get up-to-date information
        about the conversation (current username for one-to-one conversations,
        current username of a user, group or channel).
        :param chat_id:
            Conversation ID. requirement**
        :return:
            Returns a Chat object on success.
        '''
        payload = {
            'chat_id': chat_id
        }
        return self.session.request(
            'get', f'{self.url}/getchat', timeout=self.timeout, json=payload).json()


    async def leave_chat(self, chat_id: str) -> dict:
        '''This method is used for the arm to leave a group, group or channel
        :param chat_id:
            Conversation ID. requirement**
        :return:
            If successful, its output is True.
        '''
        payload = {
            'chat_id': chat_id
        }
        return self.session.request(
            'post', f'{self.url}/leavechat', timeout=self.timeout, json=payload).json()


    async def get_updates(self, offset: int = 0, limit: int = 0) -> dict:
        payload = {
            'offset': offset, 'limit': limit
        }
        return self.session.request(
            'get', f'{self.url}/getupdates', timeout=self.timeout, json=payload).json()


    async def get_chat_administrators(self, chat_id: str, just_get_id: bool = False) -> dict:
        payload = {
            'chat_id': chat_id
        }
        responce = self.session.request(
            'get', f'{self.url}/getchatadministrators', timeout=self.timeout, json=payload).json()

        if just_get_id:
            ids = []
            for user in responce['result']:
                ids.append(user['user']['id'])

            return ids
        else:
            return responce



    async def get_chat_members_count(self, chat_id: str) -> dict:
        '''This method is used to get the number of conversation members.
        :param chat_id:
            Conversation ID. requirement**
        :return:
            Returns an integer on success.
        '''
        payload = {
            'chat_id': chat_id
        }
        return self.session.request(
            'get', 'getchatmemberscount', timeout=self.timeout, json=payload).json()


    async def get_chat_member(self, chat_id: str, user_id: str) -> dict:
        payload = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return self.session.request(
            'get', f'{self.url}/getchatmember', timeout=self.timeout, json=payload).json()


    async def set_chat_photo(self, chat_id: str | int, photo = str | bytes) -> dict:
        '''This method is used to set a new profile picture for the chat
        :param chat_id:
            Conversation ID. requirement**
        :param photo:
            The new image you want to put. requirement**
        :return:
            Returns True on success.
        '''
        files = {
            'photo': open(file, 'rb')
        }
        values = {
            'chat_id': chat_id
        }
        return self.session.request(
            'post', f'{self.url}/setchatphoto', timeout=self.timeout, data=values, files=files).json()


    async def promote_chat_member(self, chat_id: str | int, user_id: str | int) -> dict:
        payload = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return self.session.request(
            'post', f'{self.url}/promoteChatMember', timeout=self.timeout, json=payload).json()


    async def ban_chat_member(self, chat_id: str | int, user_id: str | int) ->  dict:
        payload = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return self.session.request(
            'post', f'{self.url}/banchatmember', timeout=self.timeout, json=payload).json()


    async def un_ban_chat_member(self, chat_id: str | int, user_id: str | int) -> dict:
        payload = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return self.session.request(
            'post', f'{self.url}/unbanchatmember', timeout=self.timeout, json=payload).json()


    async def get_file(self, file_id: str) -> dict:
        '''This method is used to get the basic information
        of a file and prepare it for download.
        :param file_id:
            ID of the file whose information should be received. requirement**
        :return:
            Returns a File object on successful execution
        '''
        payload = {
            'file_id': file_id
        }
        return self.session.request(
            'get', f'{self.url}/getfile', timeout=self.timeout, json=payload).json()
