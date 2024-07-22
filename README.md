# BalePy

<p align=center>
<img src="https://s8.uupload.ir/files/balethon_uvi2_esnh.png" style="width: 200px; height: 200px; border: 1px solid red;" align=center alt="background">
</p>
<h3 align="center"> Balepy a Python Library for create bot API in bale messenger  <br> <h5 align=center> <a href="https://balepy.github.io"> Docs</a> | <a href="https://t.me/TheLinuxGP">Community</a> | <a href="https://t.me/TheCommit">Telegram Channel</a></h3>


### Install and Update:
```bash
pip install -U balepy
```

### Start:
```python
from balepy import Client
from balepy.types import Updates

from asyncio import run

bot_token = "0123456788:****************************************"

app = Client("my_bot", bot_token=bot_token)


@app.on_message
async def updates(update: Updates):
    print(update.text)
    await app.send_message(update.chat_id, update.text, update.message_id)


run(updates())
```

### Contributors
Contributions to the project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

### License
BalePy is released under the MIT License. See the bundled [LICENSE](https://github.com/mamdmehrabi/balepy/blob/main/LICENSE) file for details.

