import discord 
from discord.ext import commands
from utils_commands import utils
from setup_commands import setup_commands
#gets the token from the token.txt file
with open("token.txt", "r") as f:
    token = f.read()
    f.close()

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
    bot.run(token)