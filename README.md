# balepy

<h3 align="center"> balepy a Library Python for create bot API in bale application </h3>

<img src="https://s8.uupload.ir/files/balethon_uvi2.png" alt="Profile" dir="ltr" style="width: 150px; height:150px;">

## Install and Update:
```bash
pip install -U balepy
```

## For See Docs:
- <a href="https://balepy.github.io">Docs</a>
- <a href="https://t.me/TheCommit">Telegram</a>

## START:
```python
from bale import Client
from asyncio import run


__token = 'your-token-here'
client = Client(__token, timeout=10)

async def main():
    async for message in client.on_message():
        await message.reply('hello __from__ **balepy**')


if __name__ == '__main__':
    run(main())
```


## Thanks To:
### <a href="https://github.com/metect">AmirAli</a>

## Social Media:
#### <a href="https://t.me/TheCommit">TELEGRAM</a>
#### <a href="https://github.com/balepy">GITHUB</a>
