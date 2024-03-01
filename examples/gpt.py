from balepy import Client, Filters
from asyncio import run

app = Client("786709312:KejLTbe8HXUBDg34n9jY6iSLJrof5bCU7HJeelkB")

async def main():
    for m in app.on_message(Filters.group):
        print(m.message)
        
if __name__ == '__main__':
    run(main())