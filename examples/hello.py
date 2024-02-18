from balepy import Client

client = Client('token', timeout=10)
def main():
    for update in client.on_message():
        client.send_message(
            chat_id=update.chat_id,
            text='Hello __from__ **balepy**',
            reply_to_message_id=update.update_id
        )


if __name__ == '__main__':
    main()
