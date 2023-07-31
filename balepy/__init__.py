from requests import get , post

print(f"""Wellcome to balepy library v1.0
Mohammad Mehrabi Rad and Erfan Bafandeh <github.com/OnlyRad/balepy>\n\n""")


class Client:

    def __init__(self, token):
        self.token = token
        self.connection = None

    def polling(self):
        seen = [u["update_id"] for u in (self.get_updates())["result"]]
        while True:
            updates = (self.get_updates())["result"]
            for update in updates:
                if update["update_id"] in seen:
                    continue
                seen.append(update["update_id"])
                self.dispatcher(self, update)

    # messages
    def send_message(self, chat_id, text, reply_markup=None, reply_to_message_id=None):
        json = {"chat_id": chat_id, "text": text, "reply_markup": reply_markup, "reply_to_message_id": reply_to_message_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/sendMessage" , json=json)
    # messages
    def edit_message_text(self, chat_id, message_id, text, reply_markup=None):
        json = {"chat_id": chat_id, "message_id": message_id, "text": text, "reply_markup": reply_markup}
        return post(f"https://tapi.bale.ai/bot{self.token}/EditMessageText" , json=json)

    # messages
    def delete_message(self, chat_id, message_id):
        json = {"chat_id": chat_id, "message_id": message_id}
        return post(f"https://tapi.bale.ai/bot{self,token}/deletemessage" , json=json)

    # updates
    def get_updates(self, offset=0, limit=0):
        json = {"offset": offset, "limit": limit}
        return get(f"https://tapi.bale.ai/bot{self,token}/getupdates" , json=json)

    # updates
    def set_webhook(self, url):
        json = {"url": url}
        return post(f"https://tapi.bale.ai/bot{self.token}/setWebhook" , json=json)

    # updates
    def delete_webhook(self):
        return post(f"https://tapi.bale.ai/bot{self.token}/deleteWebhook" , json=json)

    # users
    def get_me(self):
        return get(f"https://tapi.bale.ai/bot{self.token}/getme")

    # attachments
    def send_photo(self, chat_id, photo, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "photo": photo, "caption": caption, "reply_to_message_id": reply_to_message_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/SendPhoto" , json=json)

    # attachments
    def send_audio(self, chat_id, audio, caption=0, duration=0, title=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "audio": audio, "caption": caption, "duration": duration, "title": title, "reply_to_message_id": reply_to_message_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/Sendaudio" , json=json)

    # attachments
    def send_document(self, chat_id, document, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "document": document, "caption": caption, "reply_to_message_id": reply_to_message_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/Senddocument" , json=json)

    # attachments
    def send_video(self, chat_id, video, duration=0, width=0, height=0, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "video": video, "duration": duration, "width": width, "height": height, "caption": caption, "reply_to_message_id": reply_to_message_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/Sendvideo" , json=json)

    # attachments
    def send_voice(self, chat_id, voice, caption=0, duration=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "voice": voice, "caption": caption, "duration": duration, "reply_to_message_id": reply_to_message_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/Sendvoice" , json=json)

    # attachments
    def send_location(self, chat_id, latitude, longitude, reply_to_message_id=0):
        json = {"chat_id": chat_id, "latitude": latitude, "longitude": longitude, "reply_to_message_id": reply_to_message_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/sendLocation" , json=json)

    # attachments
    def send_contact(self, chat_id, phone_number, first_name, last_name=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "phone_number": phone_number, "first_name": first_name, "last_name": last_name, "reply_to_message_id": reply_to_message_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/sendContact" , json=json)

    # attachments
    def get_file(self, file_id):
        json = {"file_id": file_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/getfile" , json=json)

    # chats
    def get_chat(self, chat_id):
        json = {"chat_id": chat_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/getchat" , json=json)

    # chats
    def get_chat_administrators(self, chat_id):
        json = {"chat_id": chat_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/getChatAdministrators" , json=json)

    # chats
    def get_chat_members_count(self, chat_id):
        json = {"chat_id": chat_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/getChatMembersCount" , json=json)

    # chats
    def get_chat_member(self, chat_id, user_id):
        json = {"chat_id": chat_id, "user_id": user_id}
        return post(f"https://tapi.bale.ai/bot{self.token}/getChatMember" , json=json)

    # payments
    def send_invoice(self, chat_id, title, description, provider_token, prices):
        json = {"chat_id": chat_id, "title": title, "description": description, "provider_token": provider_token, "prices": prices}
        return post(f"https://tapi.bale.ai/bot{self.token}/sendInvoice" , json=json)
