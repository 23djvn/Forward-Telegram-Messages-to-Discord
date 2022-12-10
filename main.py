import discord
from telethon import TelegramClient, events

Dcclient = discord.Client()

# Telegram Stuff
api_id = #Telegram API ID
api_hash = '#API HASH'
TeleClient = TelegramClient('1', api_id, api_hash)
TeleClient.start()

@Dcclient.event
async def on_ready():
    @TeleClient.on(events.NewMessage(chats={'#Telgram Channel Name'}))
    async def my_event_handler(event):
        message = event.raw_text
        channel = Dcclient.get_guild(#DISCORD SERVER ID).get_channel(#DISCORD CHANNEL ID)
        await channel.send(message)

TeleClient.run_until_disconnected()

Dcclient.run('#Discord Bot Token')
