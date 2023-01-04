import discord 
from discord.ext import commands
from utils_commands import utils
from setup_commands import setup_commands
from pavlov_commands import pavlov_rcon
#gets the token from the token.txt file
with open("token.txt", "r") as f:
    token = f.read()
    f.close()



intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Use .help for help"))    
    print(f'{bot.user} is ready.')
    await bot.add_cog(utils(bot))
    print ('util cog loaded loaded')
    await bot.add_cog(setup_commands(bot))
    print ('setup cog loaded')
    await bot.add_cog(pavlov_rcon(bot))
    print ('pavlov cog loaded')

def run():
    bot.run(token)