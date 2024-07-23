from .send_message import SendMessage
from .forward_message import ForwardMessage
from .copy_message import CopyMessage
from .delete_message import DeleteMessage
from .edit_message_text import EditMessageText


class Messages(SendMessage, ForwardMessage, CopyMessage, DeleteMessage, EditMessageText):
    pass
