import discord 
from discord.ext import commands
import asyncio
prefix = "."
class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong {round(self.bot.latency * 1000)}ms')
        print('pong')
    @commands.command()
    async def help(self, ctx):
        await ctx.send(f"""Commands:
{prefix}ping - shows the bots ping
{prefix}help - shows this message
{prefix}setup - sets up the bot
{prefix}rcon - sends a command to the server
        """)