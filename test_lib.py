from balepy import Client
from asyncio import run

client = Client('786709312:KejLTbe8HXUBDg34n9jY6iSLJrof5bCU7HJeelkB')
async def main():
    async for update in client.on_message():
        if update.text == '/send_message':
            await client.send_message("@user_name", "از دستور سند مسیج استفاده شده است...")

if __name__ == '__main__':
    run(main())
