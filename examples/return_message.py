from balepy import Client
from asyncio import run

bot = Client("1441486284:cPrIulYXdRkkpyxDX5L7qWueOJubOcHYI11fYSYn")

async def main():
    for m in bot.on_message():
        send_message(
            m.chat_id,
            m.text,
            m.update_id
        )

if __name__ == '__main__':
    run(main())