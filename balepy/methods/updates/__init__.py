from .get_updates import GetUpdates
from .get_webhook_info import GetWebhookInfo
from .set_webhook import SetWebhook

class Updates(GetUpdates, GetWebhookInfo, SetWebhook):
    pass
