from main import Client

class messages(Client):

    def __init__(self, method_for_get_updates):
        self.method = method_for_get_updates

    def chatID(self):
        pass