from balepy import Client
from asyncio import run


__token = '786709312:KejLTbe8HXUBDg34n9jY6iSLJrof5bCU7HJeelkB'

client = Client(__token)
async def main():
    for m in client.on_message():
        if m.group:
            print(m)

if __name__ == '__main__':
    run(main())