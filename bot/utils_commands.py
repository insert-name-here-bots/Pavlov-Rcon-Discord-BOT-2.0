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
{prefix}rcon [command] - sends a command to the server can include spaces and steamid. ex.( {prefix}rcon kick 76561198000000000) (owner only) 
{prefix}rconhelp - shows the rcon commands


        """)
    @commands.command()
    async def rconhelp(self, ctx):
        await ctx.send(f"""RCON Commands:
{prefix}kill [steamid] - kills a player (moderators only)
{prefix}ban [steamid] - bans a player (Admins only)
{prefix}unban [steamid] - unbans a player (Admins only)
{prefix}kick [steamid] - kicks a player (moderators only)
{prefix}banlist - shows the banlist (everyone)
{prefix}addmod [steamid] - adds a moderator (owner only)
{prefix}removemod [steamid] - removes a moderator (owner only)
{prefix}maplist - shows the maplist (everyone)
{prefix}rotatemap - rotates the map (admins only)
{prefix}switchmap [mapid] [gamemode] - switches the map (owner only)
""")