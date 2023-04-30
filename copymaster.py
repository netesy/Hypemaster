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

# Replace the values below with the links to the source and target groups
source_group_link = "https://t.me/efatah33metaverse"
target_group_link = "https://t.me/target_group"


async def main(account):
    # Create a new client object and connect to the Telegram API
    client = TelegramClient(
        f"my_session_{account['phone_number']}", account["api_id"], account["api_hash"]
    )
    await client.connect()

    # Log in to the client using your phone number
    await client.start(account["phone_number"])

    source_group = await client.get_entity(source_group_link)
    target_group = await client.get_entity(target_group_link)

    # Copy members from the source group to the target group
    async for member in client.iter_participants(source_group):
        try:
            await client(InviteToChannelRequest(target_group, [member]))
        except Exception as e:
            print(f"Error copying member {member.id} ({member.username}): {e}")


# Create a list of tasks for each account
tasks = [asyncio.create_task(main(account)) for account in accounts]

# Run the tasks
asyncio.gather(*tasks)
