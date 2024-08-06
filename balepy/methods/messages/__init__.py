from .send_message import SendMessage
from .forward_message import ForwardMessage
from .copy_message import CopyMessage
from .delete_message import DeleteMessage
from .edit_message_text import EditMessageText
from .send_photo import SendPhoto
from .send_audio import SendAudio
from .send_document import SendDocument
from .send_video import SendVideo
from .send_animation import SendAnimation
from .send_voice import SendVoice
from .send_media_group import SendMediaGroup
from .send_location import SendLocation


class Messages(SendMessage,
               ForwardMessage,
               CopyMessage,
               DeleteMessage,
               EditMessageText,
               SendPhoto,
               SendAudio,
               SendDocument,
               SendVideo,
               SendAnimation,
               SendVoice,
               SendMediaGroup,
               SendLocation
               ):
    pass
