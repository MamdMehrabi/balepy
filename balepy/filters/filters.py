from balepy.util import message

class Filters(message):

    def __init__(self):
        self.data = self.data

    @property
    def private(self):
        if self.data['chat']['type'] == 'private':
            return self.data
    
    @property
    def group(self):
        if self.data['chat']['type'] == 'group':
            return self.data
    
    @property
    def Channel(self):
        if self.data['chat']['type'] == 'channel':
            return self.data
        
    @property
    def new_chat_members(self):
        if self.data['new_chat_members']:
            return self.data