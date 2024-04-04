from bale import Client
import asyncio


client = Client('YOUR_TOKEN_HERE')
async def main():
    async for message in client.on_message():
        await message.reply("Hello World")


if __name__ == '__main__':
    asyncio.run(main())
