from bale import Client
import asyncio


client = Client('Your-Token')
async def main():
    for update in client.on_message():
        if update.groups:
            await client.send_message(update.chat_id, "test", reply_to_message_id=update.message_id)
        print(update.message)

if __name__ == '__main__':
    asyncio.run(main())
