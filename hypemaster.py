from datetime import datetime, timedelta
from telethon import TelegramClient, events, types
import os
import random
import asyncio

# Define the list of phone numbers, API keys, and API hashes
accounts = [
    {
        "api_id": 27610862,
        "api_hash": "2b23114139c8a0deb14505ee681ebb0f",
        "phone_number": "+2349151221593",
    },
    {
        "api_id": 24930059,
        "api_hash": "36e9a5fb105156589560cb55f8bf688d",
        "phone_number": "+2348148202546",
    },
    # Add more accounts as needed
]

# Define the path to the stickers folder
STICKERS_PATH = "./stickers/"
# Get the list of sticker file names
STICKER_FILES = os.listdir(STICKERS_PATH)

# Define the list of messages to post randomly
MESSAGES = [
    "Join EFA network now, grow your portfolio!",
    "Buy Collact NOW or Regret Later!",
    "Have you invest wisely?",
    "Do Your Own Research, EFA Network to the MOON!!",
    "Anything to share with the group?",
]

# Replace the value below with the name of the group you want to post to
group_link = "https://t.me/efatah33metaverse"


async def main(account):
    # Create a new client object and connect to the Telegram API
    client = TelegramClient(
        f"my_session_{account['phone_number']}", account["api_id"], account["api_hash"]
    )
    await client.connect()

    # Log in to the client using your phone number
    await client.start(account["phone_number"])

    group = await client.get_entity(group_link)

    # Define the time interval for checking group activity
    minutes = random.randint(1, 9)
    interval = timedelta(minutes=minutes)

    # Define the time threshold for group inactivity
    minutes = random.randint(10, 15)
    threshold = timedelta(minutes=minutes)

    # Define the last active time as the current time
    last_active_time = datetime.now()

    # Listen for updates in the group
    @client.on(events.NewMessage(chats=group))
    async def handler(event):
        # Update the last active time to the current time
        nonlocal last_active_time
        last_active_time = datetime.now()

    # Post a sticker or a message to the group every minute if the group is inactive
    while True:
        # Check if the group has been inactive for the threshold time
        if datetime.now() - last_active_time > threshold:
            # Choose whether to post a sticker or a message randomly
            post_sticker = random.choice([True, False])
            if post_sticker:
                # Post a sticker to the group
                sticker_file = random.choice(STICKER_FILES)
                with open(STICKERS_PATH + sticker_file, "rb") as f:
                    await client.send_file(
                        group,
                        f,
                    )
            else:
                # Post a message to the group
                message = random.choice(MESSAGES)
                await client.send_message(group, message)
        # Wait for the interval time before checking again
        await asyncio.sleep(interval.total_seconds())


if __name__ == "__main__":
    # Get the default event loop
    loop = asyncio.get_event_loop()
    # Create a list of future objects for each task using `ensure_future`
    tasks = [asyncio.ensure_future(main(account)) for account in accounts]
    # Run the event loop until all tasks are complete
    loop.run_until_complete(asyncio.gather(*tasks))
