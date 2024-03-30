from client import Client

import requests
import asyncio


client = Client('YOUR_TOKEN_HERE')
async def main():
    for update in client.on_message():
        responce = requests.request(
            method='post', url='https://sharkapi.liara.run/api/bard?prompt=%s' % update.text).json()

        await client.send_message(
            chat_id=update.chat_id,
            text=responce['data'],
            reply_to_message_id=update.message_id
        )


if __name__ == '__main__':
    asyncio.run(main())
