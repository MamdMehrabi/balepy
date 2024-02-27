from balepy import Client
from asyncio import run

bot = Client("1441486284:cPrIulYXdRkkpyxDX5L7qWueOJubOcHYI11fYSYn")

async def main():
    for m in bot.on_message():
        await bot.send_message(
            chat_id=m.chat_id,
            text=m.text,
            reply_to_message_id=m.message_id
        )
        print(m.message)


if __name__ == '__main__':
    run(main())