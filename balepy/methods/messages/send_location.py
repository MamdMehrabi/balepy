from balepy.objects import HTTPMethod

import balepy


class SendLocation:

    async def send_location(
            self: "balepy.Client",
            chat_id: str,
            latitude: float,
            longitude: float,
            horizontal_accuracy=None,
            reply_to_message_id=None,
            reply_markup=None
    ):
        params = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'horizontal_accuracy': horizontal_accuracy,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }

        await self.api.execute(name="sendLocation", method=HTTPMethod.POST, data=params)
