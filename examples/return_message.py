from bale import Client
import asyncio


client = Client('YOUR_TOKEN_HERE')
async def main():
    for upadte in client.on_message():
        await client.send_message(
            chat_id=upadte.chat_id,
            text=upadte.text,
            reply_to_message_id=upadte.message_id
        )


if __name__ == '__main__':
    asyncio.run(main())
