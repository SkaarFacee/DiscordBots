import os

import discord,random
from secret  import DISCORD_TOKEN,DISCORD_GUILD

TOKEN = os.getenv(DISCORD_TOKEN)
GUILD = os.getenv(DISCORD_GUILD)
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
   

@client.event
async def on_message(message):
    if(message.author.bot == False):
        brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
        if message.content == '99!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)
        if 'happy birthday' in message.content.lower():
            await message.channel.send('Happy Birthday! for the last time!🎈🎉')
        if message.content == 'ping':
            await message.channel.send('pong')
        if(message.author.bot):
         return
        if message.content == '101!':
            response = "Just kiss vivek already{0.author.mention}".format(message)
            await message.channel.send(response)
        elif message.content == 'raise-exception':
            raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


    
client.run(DISCORD_TOKEN)