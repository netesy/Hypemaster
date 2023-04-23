from telethon import TelegramClient, events, types
import os
import random

# Replace the values below with your own API key and phone number
api_id = 27610862
api_hash = "2b23114139c8a0deb14505ee681ebb0f"
phone_number = "+2349151221593"
# Define the path to the stickers folder
STICKERS_PATH = "./stickers/"
# Get the list of sticker file names
STICKER_FILES = os.listdir(STICKERS_PATH)

# Replace the value below with the name of the group you want to post to
group_link = "https://t.me/efatah33metaverse"

# Create a new client object and connect to the Telegram API
client = TelegramClient("my_session", api_id, api_hash)


async def main():
    await client.connect()

    # Log in to the client using your phone number
    await client.start(phone_number)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, "has ID", dialog.id)

    group = await client.get_entity(group_link)

    # You can, of course, use markdown in your messages:
    message = await client.send_message(
        "me",
        "This message has **bold**, `code`, __italics__ and "
        "a [nice website](https://example.com)!",
        link_preview=False,
    )

    # You can reply to messages directly if you have a message object
    await message.reply("Cool!")

    # Or send files, songs, documents, albums...
    # Post a sticker to the group
    sticker_file = random.choice(STICKER_FILES)
    with open(STICKERS_PATH + sticker_file, "rb") as f:
        await client.send_file(
            group,
            f,
        )


with client:
    client.loop.run_forever(main())
