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
{prefix}rcon [command] - sends a command to the server can include spaces and steamid. ex.( {prefix}rcon kick 76561198000000000) 
{prefix}rconhelp - shows the rcon commands
{prefix}kill [steamid] - kills a player
{prefix}ban [steamid] - bans a player
{prefix}unban [steamid] - unbans a player
{prefix}kick [steamid] - kicks a player
{prefix}banlist - shows the banlist
        """)