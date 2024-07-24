from balepy import Client
from balepy.types import Updates

from asyncio import run

# bot_token = "0123456788:****************************************"
bot_token = "786709312:NubluZVlb29oRs1MxwUI14XGKTA5dnxCpp5bOzgR"

app = Client("my_bot", bot_token=bot_token)


@app.on_message
async def updates(update: Updates):
    await app.send_message(update.chat_id, update.text, update.message_id)
    print(update.message)

run(updates())
