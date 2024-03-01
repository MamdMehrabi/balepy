
class message:

    def __init__(self, data: dict) -> str:
        self.data: dict = data

    @property
    def message(self):
        if 'callback_query' in self.data:
            return self.data['callback_query']['message']
        elif 'message' in self.data:
            return self.data['message']

    @property
    def update_id(self):
        return self.data['update_id']

    @property
    def message_id(self):
        return self.message['message_id']

    @property
    def author_id(self):
        return self.message['from']['id']

    @property
    def is_bot(self):
        return self.message['from']['is_bot']

    @property
    def author_first_name(self):
        return self.message['from']['first_name']

    @property
    def author_last_name(self):
        return self.message['from']['last_name']

    @property
    def author_username(self):
        if 'username' in self.message['from']:
            return self.message['from']['username']
        else:
            return None

    @property
    def chat_id(self):
        return self.message['chat']['id']

    @property
    def chat_type(self):
        return self.message['chat']['type']

    @property
    def chat_title(self):
        return self.message['chat']['title']

    @property
    def is_reply(self):
        if 'reply_to_message' in self.message:
            return True
        else:
            return False

    @property
    def message_id(self):
        # if 'reply_to_message' in self.message:
        #     return self.message['reply_to_message']['message_id']
        # else:
        #     return False
        return self.message['message_id']

    @property
    def forward_from_id(self):
        if 'forward_from' in self.message:
            return self.message['forward_from']['id']
        elif 'forward_from_chat' in self.message:
            return self.message['forward_from_chat']['id']
        else:
            return None

    @property
    def text(self):
        try:
            return self.message['text']
        except KeyError:
            return self.message['caption']
        except:
            return None

    @property
    def message_type(self):
        if 'text' in self.message:
            return 'text'
        elif 'photo' in self.message:
            if 'caption' in self.message:
                return 'photoCaption'
            else:
                return 'photo'
        elif 'video' in self.message:
            if 'caption' in self.message:
                return 'videoCaption'
            else:
                return 'video'
        elif 'document' in self.message:
            if 'caption' in self.message:
                return 'documentCaption'
            else:
                return 'document'
        elif 'audio' in self.message:
            if 'caption' in self.message:
                return 'audioCaption'
            else:
                return 'audio'
        else:
            return None
