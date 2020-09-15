import os
import random
import discord 

from discord import Embed, Emoji
from discord.ext import commands
from secret  import DISCORD_TOKEN,DISCORD_GUILD

TOKEN = os.getenv(DISCORD_TOKEN)
GUILD = os.getenv(DISCORD_GUILD)
client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
'''if message.content == "!sos":
            response = "Just kiss vivek already{0.author.mention}".format(message)
            panel = await message.channel.send(response)
            await panel.add_reaction('\U0001F44D')
            await panel.add_reaction('\U0001F44E')
'''
@bot.command(name='11', help='Embed text')
async def create(ctx):
    embed = discord.Embed(color=discord.Color(15105570),title=f"{ctx.guild.name}",description="Test am embed", )
    embed.set_footer(
            text = "Bot Is Among Us",)
    embed.add_field(name=f"Question 1",value=f"Created at :{ctx.guild.created_at}") 
    panel = await ctx.channel.send(embed=embed)
    await panel.add_reaction('\U0001F44D')
    await panel.add_reaction('\U0001F44E')


@bot.command(name='1', help='Embed text')
async def test(ctx):
    print(102)    
    for guild in client.guilds:
        print(103)
        for member in guild.members:
            print(104)
            await ctx.send(', '.join(member))



@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice, number_of_sides):
    dice = [
        str(random.choice(range(1, int(number_of_sides) + 1)))
        for _ in range(int(number_of_dice))
    ]
    await ctx.send(', '.join(dice))




bot.run(DISCORD_TOKEN)
