import os

import discord
from secret  import DISCORD_TOKEN

TOKEN = os.getenv(DISCORD_TOKEN)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(DISCORD_TOKEN)