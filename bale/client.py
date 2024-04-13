from network import Network
from util import message
from exceptions import *

from typing import Optional
import asyncio


class Client:

    def __init__(self, token: str, timeout: Optional[float] = 20) -> None:
        self.loop = asyncio.get_event_loop()
        self.network = Network(token=token, timeout=timeout)

        if not token:
            raise TokenNotInvalid('`token` did\'t passed')

    async def request(self, method: str, data: dict = None, files: dict = None) -> dict:
        # try:
            return await self.network.connect(method=method, data=data, files=files)
        # except Exception as err:
        #     print(__file__, err, __file__)

    async def on_message(self):
        '''Use this method to receive updates
        Example:
            from bale import Client
            import asyncio

            client = Client('token', timeout=10)
            async def main():
                async for update in client.on_message():
                    print(update.text)
                    await update.reply('hello __from__ **balepy**')

            asyncio.run(main())
        '''
        payload: dict = {
            'offset': -1, 'limit': 100
        }
        while True:
            update = await self.request('getupdates', payload)
            payload['offset'] = 1
            if update != None and update != []:
                break

        payload['offset'], payload['limit'] = update[len(update)-1]['update_id'], 1
        while True:
            responce = await self.request('getupdates', payload)
            if responce != None and responce != []:
                payload['offset'] += 1
                yield message(responce[0], self.network.token, self.network.timeout)

    async def on_command(self, commands: list):
        async for message in self.on_message():
            if message.text in commands:
                yield message

    async def send_message(
            self,
            chat_id: int,
            text: str,
            reply_markup: Optional[int] = None,
            reply_to_message_id: Optional[int] = None,
            auto_delete: Optional[int] = None
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
        responce = await self.request('sendmessage', data=payload)
        if isinstance(auto_delete, int):
            message_id: int = responce['message_id']
            await asyncio.sleep(delay=auto_delete)
            callback_data = asyncio.create_task(
                self.delete_message(
                    chat_id=chat_id, message_id=message_id
                )
            )
            return callback_data

        return responce


    async def edit_message(
            self,
            chat_id: int,
            text: str,
            message_id: int,
            reply_markup: Optional[int] = None
    ) -> dict:
        payload: dict = {
            'chat_id': chat_id,
            'text': text,
            'reply_to_message_id': message_id,
            'reply_markup': reply_markup
        }
        return await self.request('editmessage', data=payload)


    async def forward_message(self, chat_id: int, from_chat_id: int, message_id: int) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id
        }
        return await self.request('forwardmessage', data=payload)


    async def copy_message(self, chat_id: int, from_chat_id: int, message_id: int) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id
        }
        return self.request('copymessage', data=payload)


    async def send_media_group(
            self,
            chat_id: int,
            media: list,
            reply_to_message_id: Optional[int] = None
    ) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'media': media, 'reply_to_message_id': reply_to_message_id
        }
        return self.request('sendmediagroup', data=payload)


    async def delete_message(self, chat_id: int, message_id: int) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'message_id': message_id
        }
        return await self.request('deletemessage', data=payload)


    async def auto_delete_message(self, chat_id: int, message_id: int, time: int) -> dict:
        await asyncio.sleep(delay=time)
        await asyncio.create_task(
            self.delete_message(
                chat_id=chat_id, message_id=message_id
            )
        )


    async def send_contact(
            self,
            chat_id: int,
            phone_number: int,
            first_name: str,
            last_name: Optional[str] = None,
            reply_to_message_id: Optional[int] = None
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
            chat_id: int,
            from_chat_id: int,
            file: str | bytes,
            caption: Optional[str] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[int] = None
    ) -> dict:
        files: dict = {
            'photo': open(file, 'rb')
        }
        payload: dict = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return await self.request('sendphoto', data=payload, files=files)


    async def send_audio(
            self,
            chat_id: int,
            file: str | bytes,
            caption: Optional[str] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[int] = None
    ) -> dict:
        files: dict = {
            'audio': open(file, 'rb')
        }
        payload: dict = {
            'chat_id': chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return await self.request('sendaudio', data=payload, files=files)


    async def send_document(
            self,
            chat_id: int,
            file: str | bytes,
            caption: Optional[str] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[int] = None
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
        payload: dict = {
            'chat_id': chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return await self.request('senddocument', data=payload, files=files)


    async def send_animation(
            self,
            chat_id: int,
            file: str | bytes,
            caption: Optional[str] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[int] = None
    ) -> dict:
        '''This method is used to send animation files (GIF video or H.264/MPEG-4 AVC without sound)'''
        files: dict = {
            'animation': open(file, 'rb')
        }
        payload: dict = {
            'chat_id': chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return await self.request('sendanimation', data=payload, files=files)



    async def send_voice(
            self,
            chat_id: int,
            file: str | bytes,
            caption: Optional[str] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[int] = None
    ) -> dict:
        files: dict = {
            'voice': open(file, 'rb')
        }
        payload: dict = {
            'chat_id': chat_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return await self.request('sendvoice', data=payload, files=files)


    async def send_location(
            self,
            chat_id: int,
            latitude: float,
            longitude: float,
            horizontal_accuracy: float,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[int] = None
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
        return self.request('setwebhook', data=payload)


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


    async def get_chat(self, chat_id: int) -> dict:
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


    async def leave_chat(self, chat_id: int) -> dict:
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


    async def get_chat_invite_link(self, chat_id: int) -> str:
        chat_data = await self.get_chat(chat_id=chat_id)
        return chat_data['invite_link']


    async def get_updates(self, offset: Optional[int] = 0, limit: Optional[int] = 0) -> dict:
        payload: dict = {
            'offset': offset, 'limit': limit
        }
        return await self.request('getupdates', data=payload)


    async def get_chat_administrators(self, chat_id: int, just_get_id: Optional[bool] = False) -> dict:
        payload: dict = {
            'chat_id': chat_id
        }
        responce = await self.request('getchatadministrators', data=payload)

        if just_get_id:
            chat_admins = list()
            for admin in responce:
                chat_admins.append(admin['user']['id'])

            return chat_admins
        return responce


    async def get_chat_members_count(self, chat_id: int) -> dict:
        payload: dict = {
            'chat_id': chat_id
        }
        return await self.request('getchatmemberscount', data=payload)


    async def get_chat_member(self, chat_id: int, user_id: int) -> dict:
        payload: dict = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return await self.request('getchatmember', data=payload)


    async def set_chat_photo(self, chat_id: int, file = str | bytes) -> dict:
        files: dict = {
            'photo': open(file, 'rb')
        }
        payload: dict = {
            'chat_id': chat_id,
        }
        return await self.request('setchatphoto', data=payload, files=files)


    async def ban_chat_member(self, chat_id: int, user_id: int) ->  dict:
        payload: dict = {
            'chat_id': chat_id, 'user_id': user_id
        }
        return await self.request('banchatmember', data=payload)


    async def un_ban_chat_member(self, chat_id: int, user_id: int) -> dict:
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
