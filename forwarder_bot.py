from telethon.sync import TelegramClient, events

# Your Telethon API credentials
api_id = 9784025  # Replace with your API ID
api_hash = "26c6ffdcb2da4a7f35000d9b551af040"  # Replace with your API hash
session_name = "forwarder_bot"  # Session file

# Source & Destination
SOURCE_CHANNEL = "@Technicaljs_ShoppingOffers"  # Replace with the public channel ID (where messages come from)
DESTINATION_BOT = "@link_conversion_bot"  # Replace with your bot's username (without @)

# Initialize client
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def forward_message(event):
    """ Forward message without changes """
    try:
        await client.send_message(DESTINATION_BOT, event.message)
        print(f"✅ Forwarded: {event.message.text[:50]}...")
    except Exception as e:
        print(f"❌ Error forwarding: {e}")

with client:
    print("🚀 Bot is running and forwarding messages...")
    client.run_until_disconnected()
