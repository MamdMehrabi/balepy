from balepy import Client
import asyncio


__token = 'your-token-here'

client = Client(__token, 10)
async def main():
    for update in client.on_message():
        await client.send_message(
            chat_id=update.chat_id,
            text='Hello __from__ **balepy**',
            reply_to_message_id=update.message_id
        )


if __name__ == '__main__':
    asyncio.run(main())
