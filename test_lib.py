from bale import Client
from asyncio import run

client = Client('Your-Token')
async def main():
    async for update in client.on_message():
        print(update.message)
        #await client.send_message(update.chat_id, 'Created By lib *balepy*')
        await client.send_message(update.chat_id, "Heellllllooooooo", reply_markup={'inline_keyboard': [[{'text': "Hello World", 'callback_data': "new"}]]})

if __name__ == '__main__':
    run(main())
