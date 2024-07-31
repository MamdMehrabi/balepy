from balepy.objects import HTTPMethod

import balepy


class Updates:

    def __init__(self, data: dict):
        self.data = data

    @property
    def message(self):
        if "callback_query" in self.data:
            return self.data["callback_query"]["message"]
        elif "message" in self.data:
            return self.data["message"]

    @property
    def is_callback(self):
        if "callback_query" in self.data:
            return True
        else:
            return False

    @property
    def update_id(self):
        return self.data["update_id"]

    @property
    def message_id(self):
        return self.message["message_id"]

    @property
    def author_id(self):
        return self.message["from"]["id"]

    @property
    def callback_author_id(self):
        if self.is_callback:
            return self.data["callback_query"]["from"]["id"]
        else:
            return None

    @property
    def is_bot(self):
        return self.message["from"]["is_bot"]

    @property
    def callback_is_bot(self):
        if self.is_callback:
            return self.data["callback_query"]["from"]["is_bot"]
        else:
            return None

    @property
    def author_first_name(self):
        return self.message["from"]["first_name"]

    @property
    def callback_author_first_name(self):
        if self.is_callback:
            return self.data["callback_query"]["from"]["first_name"]
        else:
            return None

    @property
    def author_last_name(self):
        return self.message["from"]["last_name"]

    @property
    def callback_author_last_name(self):
        if self.is_callback:
            return self.data["callback_query"]["from"]["last_name"]
        else:
            return None

    @property
    def author_username(self):
        if "username" in self.message["from"]:
            return self.message["from"]["username"]
        else:
            return None

    @property
    def callback_author_username(self):
        if self.is_callback:
            if "username" in self.data["callback_query"]:
                return self.data["callback_query"]["from"]["username"]
            else:
                return None
        else:
            return None

    @property
    def chat_id(self):
        return self.message["chat"]["id"]

    @property
    def chat_type(self):
        return self.message["chat"]["type"]

    @property
    def chat_title(self):
        return self.message["chat"]["title"]

    @property
    def new_member(self):
        if "new_chat_members" in self.message:
            return True
        else:
            return False

    @property
    def new_member_id(self):
        if self.new_member:
            return self.message["new_chat_members"][0]["id"]
        else:
            return None

    @property
    def new_member_is_bot(self):
        if self.new_member:
            return self.message["new_chat_members"][0]["is_bot"]
        else:
            return None

    @property
    def new_member_first_name(self):
        if self.new_member:
            return self.message["new_chat_members"][0]["first_name"]
        else:
            return None

    @property
    def new_member_last_name(self):
        if self.new_member:
            return self.message["new_chat_members"][0]["last_name"]
        else:
            return None

    @property
    def new_member_username(self):
        if self.new_member and "username" in self.message["new_chat_members"][0]:
            return self.message["new_chat_members"][0]["username"]
        else:
            return None

    @property
    def left_member(self):
        if "left_chat_member" in self.message:
            return True
        else:
            return False

    @property
    def left_member_id(self):
        if self.left_member:
            return self.message["left_chat_member"]["id"]
        else:
            return None

    @property
    def left_member_is_bot(self):
        if self.left_member:
            return self.message["left_chat_member"]["is_bot"]
        else:
            return None

    @property
    def left_member_first_name(self):
        if self.left_member:
            return self.message["left_chat_member"]["first_name"]
        else:
            return None

    @property
    def left_member_last_name(self):
        if self.left_member:
            return self.message["left_chat_member"]["last_name"]
        else:
            return None

    @property
    def left_member_username(self):
        if self.left_member and "username" in self.message["left_chat_member"]:
            return self.message["left_chat_member"]["username"]
        else:
            return None

    @property
    def is_reply(self):
        if "reply_to_message" in self.message:
            return True
        else:
            return False

    @property
    def reply_message_id(self):
        if "reply_to_message" in self.message:
            return self.message["reply_to_message"]["message_id"]
        else:
            return False

    @property
    def reply_data(self):
        if "reply_to_message" in self.message:
            return self.message["reply_to_message"]
        else:
            return False

    @property
    def is_forward(self):
        if "forward_from" in self.message:
            return True
        elif "forward_from_chat" in self.message:
            return True
        else:
            return False

    @property
    def forward_from_id(self):
        if "forward_from" in self.message:
            return self.message["forward_from"]["id"]
        elif "forward_from_chat" in self.message:
            return self.message["forward_from_chat"]["id"]
        else:
            return None

    @property
    def forward_from_message_id(self):
        if "forward_from_message_id" in self.message:
            return self.message["forward_from_message_id"]
        else:
            return None

    @property
    def forward_from_is_bot(self):
        if "forward_from" in self.message:
            return self.message["forward_from"]["is_bot"]
        else:
            return None

    @property
    def forward_from_is_bot(self):
        if self.is_forward:
            return self.message["forward_from"]["is_bot"]
        else:
            return None

    @property
    def text(self):
        if "text" in self.message:
            return self.message["text"]
        elif "caption" in self.message:
            return self.message["caption"]
        else:
            return None

    @property
    def callback_data_send(self):
        if self.is_callback:
            return self.data["callback_query"]["data"]
        else:
            return None

    @property
    def file_data(self):
        if "photo" in self.message:
            return self.message["photo"]
        elif "video" in self.message:
            return self.message["video"]
        elif "document" in self.message:
            return self.message["document"]
        elif "audio" in self.message:
            return self.message["audio"]
        else:
            return None

    @property
    def message_type(self):
        if "text" in self.message:
            return "text"
        elif "photo" in self.message:
            if "caption" in self.message:
                return "photoCaption"
            else:
                return "photo"
        elif "video" in self.message:
            if "caption" in self.message:
                return "videoCaption"
            else:
                return "video"
        elif "document" in self.message:
            if "caption" in self.message:
                return "documentCaption"
            else:
                return "document"
        elif "audio" in self.message:
            if "caption" in self.message:
                return "audioCaption"
            else:
                return "audio"
        else:
            return None

    async def reply(self: "balepy.Client", text: str) -> dict:
        payload: dict = {
            "text": text,
            "chat_id": Updates.chat_id,
            "reply_to_message_id": Updates.message_id
        }
        return await self.api.execute(name="sendMessage", method=HTTPMethod.POST, data=payload)

    @property
    def is_groups(self):
        if self.message["chat"]["type"] == "group":
            return self.message

    @property
    def is_channel(self):
        if self.message["chat"]["type"] == "channel":
            return self.message

    @property
    def is_private(self):
        if self.message["chat"]["type"] == "private":
            return self.message
