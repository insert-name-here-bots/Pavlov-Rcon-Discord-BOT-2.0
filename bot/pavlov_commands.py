from pavlov import PavlovRCON
import discord 
from discord.ext import commands

class pavlov_rcon(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def rcon(self, ctx, *, args):
        #gets the ip port and password from the server.txt file
        
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()
        
        f.close()
        
        #connects to the server
        rcon = PavlovRCON(ip.strip(), port.strip(), password.strip())
        
        
        command = await rcon.send(args)
        if command["Successful"] == False:
            await ctx.send("failed to connect to the server")
            return
        #sends the command to the server
        await ctx.send(command)
        await rcon.close()

