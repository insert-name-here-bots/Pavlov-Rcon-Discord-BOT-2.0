import discord
from discord.ext import commands

class setup_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def setup(self, ctx):
        #saves ip port and password to a file
        await ctx.send("starting setup")
        await ctx.send("what is the ip of the server?")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        ip = await self.bot.wait_for('message', check=check)
        await ctx.send("what is the port of the server?")
        port = await self.bot.wait_for('message', check=check)
        await ctx.send("what is the password of the server?")
        password = await self.bot.wait_for('message', check=check)
        #saves the ip port and password to a file
        f = open("server.txt", "w+")
        f.write(ip.content + "\n")
        f.write(port.content + "\n")
        f.write(password.content + "\n")
        f.close()
        await ctx.send("setup complete")
         
      