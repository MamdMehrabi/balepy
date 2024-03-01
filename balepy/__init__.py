from .client import Client
from .util import message
from .filters import Filters
from asyncio import run

__title__: str = 'balepy'
__version__: str = '1.3.6'
__license__: str = 'MIT license'
__author__: str = 'Mamad Mehrabi Rad'
__url__: str = 'https://github.com/OnlyRad/balepy'
__author_email__: str = 'mohammadmehrabi175@gmail.com'
__description__: str = 'Optimal and practical module for building API bots in bale messengers'

app = Client("786709312:KejLTbe8HXUBDg34n9jY6iSLJrof5bCU7HJeelkB")
async def main():
    for m in app.on_message(Filters.group):
        print(m.message)

if __name__ == '__main__':
    run(main())