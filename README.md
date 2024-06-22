# balepy

<p align=center>
<img src="https://s8.uupload.ir/files/balethon_uvi2_esnh.png" style="width: 200px; height: 200px; border: 1px solid red;" align=center alt="background">
</p>
<h3 align="center"> Balepy a Python Library for create bot API in bale messenger  <br> <h5 align=center> <a href="https://balepy.github.io"> Docs</a> | <a href="https://t.me/TheLinuxGP">Community</a> | <a href="https://t.me/TheCommit">Telegram Channel</a></h3>


## Install and Update:
```bash
pip install -U balepy
```

## START:
```python
from balepy import Client
from asyncio import run


__token = 'your-token-here'
client = Client(__token, timeout=10)

@client.on_message
async def main(message):
    if message.text == "/start":
        await message.reply('hello __from__ **balepy**')


if __name__ == '__main__':
    run(main())
```

Thanks to all those who contributed directly or indirectly to the development of the module
