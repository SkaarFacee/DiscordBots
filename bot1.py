import os

import discord,random
#from secret  import DISCORD_TOKEN
TOKEN = os.getenv(os.environ['DISCORD_TOKEN'])
client = discord.Client()
import requests
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the super secret server, Stay happy till you get kicked ;)'
    )
@client.event
async def on_message(message):
    if(message.author.bot == False):
        if 'happy birthday' in message.content.lower():
            await message.channel.send('Happy Birthday!🎈🎉')
        if message.content == 'ping':
            panel = await message.channel.send('pong')
            await panel.add_reaction('\U0001F3D3')
        if(message.author.bot):
         return
        if message.content == 'gn':
            r = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
            text=r.json()
            print(text['insult'])
            user = random.choice(message.channel.guild.members)
            author=message.author
            print(user==message.author)
            for i in range(1000):
                if not user.bot and not user==message.author:
                    response = str(text['insult']) + " {0.mention} ".format(user)
                    break
                else:
                    user = random.choice(message.channel.guild.members)
            panel = await message.channel.send(response)
            await panel.add_reaction('\U0001F44D')
            await panel.add_reaction('\U0001F44E')
        elif message.content == 'raise-exception':
            raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
    
client.run(os.environ['DISCORD_TOKEN'])