import discord
import random
import string
import os
from flask import Flask
import threading

TOKEN = os.getenv('TOKEN')
TARGET_CHANNEL_ID = 123456789012345678

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    server = threading.Thread(target=run)
    server.start()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "เช็คแล้ว":
        characters = string.ascii_lowercase + string.digits
        random_string = ''.join(random.choices(characters, k=35))
        channel = client.get_channel(TARGET_CHANNEL_ID)
        if channel:
            await channel.send(f'https://gift.truemoney.com/campaign/?v={random_string}')

keep_alive()
client.run(TOKEN)
