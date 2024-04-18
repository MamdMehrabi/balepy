from bale import Client
from asyncio import run


client = Client('YOUR_TOKEN_HERE')
async def main():
    for update in client.on_message():
        await client.send_message(
            chat_id=update.chat_id,
            text='hello __from__ *balepy*',
            reply_to_message_id=update.message_id
        )


if __name__ == '__main__':
    run(main())
