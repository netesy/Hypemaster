from datetime import datetime, timedelta
from telethon import TelegramClient, events, types
import os
import random
import asyncio

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

    group = await client.get_entity(group_link)

    # Define the time interval for checking group activity
    interval = timedelta(minutes=1)

    # Define the time threshold for group inactivity
    threshold = timedelta(minutes=5)

    # Define the last active time as the current time
    last_active_time = datetime.now()

    # Listen for updates in the group
    @client.on(events.NewMessage(chats=group))
    async def handler(event):
        # Update the last active time to the current time
        nonlocal last_active_time
        last_active_time = datetime.now()

    # Post a sticker to the group every minute if the group is inactive
    while True:
        # Check if the group has been inactive for the threshold time
        if datetime.now() - last_active_time > threshold:
            # Post a sticker to the group
            sticker_file = random.choice(STICKER_FILES)
            with open(STICKERS_PATH + sticker_file, "rb") as f:
                await client.send_file(
                    group,
                    f,
                )
        # Wait for the interval time before checking again
        await asyncio.sleep(interval.total_seconds())


with client:
    client.loop.run_until_complete(main())
