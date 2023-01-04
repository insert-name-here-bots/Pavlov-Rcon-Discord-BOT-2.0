from pavlov import PavlovRCON
import discord 
from discord.ext import commands


class pavlov_rcon(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def rcon(self, ctx, *args):
        #gets the ip port and password from the server.txt file
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()
        f.close()
        #connects to the server
        rcon = PavlovRCON(ip, port, password)
        #sends the command to the server
        await ctx.send(rcon.send_command(args))
        rcon.close()
