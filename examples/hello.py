from balepy import Client, filters
import asyncio


__token = '786709312:KejLTbe8HXUBDg34n9jY6iSLJrof5bCU7HJeelkB'

client = Client(__token, 10)
async def main():
    for update in client.on_message():
        print(update.message)
        if update.text == '/start':
            await client.send_message(
                chat_id=update.chat_id,
                text='Hello __from__ **balepy**',
                reply_to_message_id=update.message_id
            )

if __name__ == '__main__':
    asyncio.run(main())
