from .send_message import SendMessage
from .forward_message import ForwardMessage
from .copy_message import CopyMessage
from .delete_message import DeleteMessage
from .edit_message_text import EditMessageText
from .send_photo import SendPhoto
from .send_audio import SendAudio
from .send_document import SendDocument


class Messages(SendMessage, ForwardMessage, CopyMessage, DeleteMessage, EditMessageText, SendPhoto, SendAudio, SendDocument):
    pass
