from .util import message

class filters(message):

    @property
    def group(self):
        if message.message['chat']['type'] == 'group':
            return message.message
        else:
            return None
    
    @property
    def Channel(self):
        if message.message['chat']['type'] == 'channel':
            return message.message
        else:
            None
    @property
    def new_chat_members(self):
        if message.message['new_chat_members']:
            return message.message
        else:
            None