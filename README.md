# balepy

<p align=center>
<img src="https://s8.uupload.ir/files/balethon_uvi2_esnh.png" style="width: 300px; height: 300px;" align=center alt="background">
</p>
<h3 align="center"> balepy a Library Python for create bot API in bale application <br> <h5 align=center> <a href="https://balepy.github.io"> Docs</a> | <a href="https://t.me/TheLinuxGP">Community</a> | <a href="https://t.me/TheCommit">Telegram Channel</a> | <a href="https://github.com/OnlyRad">Owner</a></h5></h3>


## Install and Update:
```bash
pip install -U balepy
```

## START:
```python
from balepy import Client
from balepy.types import Updates

from asyncio import run

bot_token = "0123456788:****************************************"

app = Client("my_bot", bot_token=bot_token)


@app.on_message
async def updates(update: Updates):
    print(update)
    await app.send_message(update.chat_id, update.text, update.message_id)


run(updates())
```

## Contributors
- [amirali irvany](https://github.com/irvanyamirali)

Thanks to all those who contributed directly or indirectly to the development of the module
