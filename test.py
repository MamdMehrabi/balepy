from balepy import Client
from balepy.types import Updates

from asyncio import run

# bot_token = "0123456788:****************************************"
bot_token = "1472180488:ha6K87ty7NnnnWeSIGkfpuiK56DcV23Tv89Q6gvZ"

app = Client("my_bot", bot_token=bot_token)


@app.on_message
async def updates(update: Updates):
    print(update.text)
    await app.send_message(update.chat_id, update.text, update.message_id)


run(updates())
