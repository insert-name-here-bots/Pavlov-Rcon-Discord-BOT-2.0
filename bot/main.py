import discord 
from discord.ext import commands
from utils_commands import utils
from setup import setup_commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user} is ready.')
    await bot.add_cog(utils(bot))
    print ('util cog loaded loaded')
    await bot.add_cog(setup_commands(bot))
    print ('setup cog loaded')

def run():
    bot.run('OTY4NjcxMjUxMjA1ODYxNDE3.G3TSko.8Pb0zAc22_lByIWo3NaOaqE6LjVO1KZH9hMfVE')