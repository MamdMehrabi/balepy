from bale import Client
import datetime
import asyncio


chat_id = 5944972955
chat_admins = list()

async def update_admin_chat(client: Client, chat_id: int) -> list:
    admins_id = await client.get_chat_administrators(chat_id=chat_id, just_get_id=True)
    for admin in admins_id:
        chat_admins.append(admin)


async def check_allowed_message(client: Client, chat_id: int, text: str, user_id: int, message_id: int):
    if user_id not in chat_admins:
        if text in ['@', 'ble.ir', 'join']:
            await client.delete_message(chat_id=chat_id, message_id=message_id)


async def get_chat_invite_link(client: Client, chat_id: int):
    invite_link = await client.get_chat(chat_id=chat_id)
    return invite_link['invite_link']


async def startup_bot(client: Client, chat_id: int):
    await update_admin_chat(client=client, chat_id=chat_id)
    data_time = datetime.datetime.now()
    data_time.strftime('%d/%m/%Y %H:%M:%S')
    await client.send_message(
        chat_id=chat_id,
        text='The bot has been successfully activated in your chat\n- TIME %s' % data_time
    )


__token = '1472180488:ha6K87ty7NnnnWeSIGkfpuiK56DcV23Tv89Q6gvZ'
client = Client(__token, 20)
async def main():
    # starting bot and send welcome message
    await startup_bot(client=client, chat_id=chat_id)
    async for update in client.on_message():
        await check_allowed_message(
            client=client, chat_id=update.chat_id, text=update.text,
            user_id=update.author_id, message_id=update.message_id
        )
        if update.text.lower() == '/test':
            await update.reply('The bot is now active in your chat')

        elif update.text.lower() == '/update-admins':
            await update.reply('*Updating the list of admins...*')
            await update_admin_chat(client=client, chat_id=update.chat_id)
            await update.reply('*The list of admins has been successfully updated*')

        elif update.text.lower() == '/link':
            invite_link = await get_chat_invite_link(client=client, chat_id=update.chat_id)
            await update.reply('Your chat link:\n\n```%s```' % invite_link)


if __name__ == '__main__':
    asyncio.run(main())
