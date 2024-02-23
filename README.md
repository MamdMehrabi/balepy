# balepy

<h3 align="center"> balepy a Library Python for create bot API in bale application </h3>

## Install and Update:
```bash
pip install -U balepy
```

## For See Docs:
- <a href="https://balepy.github.io">WebSite</a>
- <a href="https://t.me/TheCommit">TELEGRAM</a>

## START:
```python
from balepy import Client
import asyncio

__token = 'your-token-here'
client = Client(__token, timeout=10)

async def main():
    for update in client.on_message():
        await client.send_message(
            chat_id=update.chat_id,
            text='Hello __from__ *balepy*',
            reply_to_message_id=update.update_id
        )

if __name__ == '__main__':
    asyncio.run(main())
```

## Social Media:
#### <a href="https://t.me/TheCommit">TELEGRAM</a>
#### <a href="https://rubika.ir/TheBalepy">RUBIKA</a>
