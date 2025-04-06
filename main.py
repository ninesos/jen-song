import discord
import random
import string
import os

TOKEN = os.getenv('TOKEN')

# ใส่ ID ของช่องที่อยากให้ส่งข้อความ
TARGET_CHANNEL_ID = 1358457657823989941

intents = discord.Intents.default()
intents.message_content = True  # เปิดให้บอทอ่านข้อความได้

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # อย่าให้บอทตอบตัวเอง
    if message.author == client.user:
        return

    # ถ้ามีข้อความว่า "เช็คแล้ว"
    if message.content.lower() == "เช็คแล้ว":
        # สุ่มตัวอักษรภาษาอังกฤษพิมพ์เล็ก + ตัวเลข
        characters = string.ascii_lowercase + string.digits
        random_string = ''.join(random.choices(characters, k=35))

        # หา Channel ที่กำหนด
        channel = client.get_channel(TARGET_CHANNEL_ID)
        if channel:
            await channel.send(f'https://gift.truemoney.com/campaign/?v={random_string}')
        else:
            print("ไม่พบช่องที่กำหนด!")

client.run(TOKEN)
