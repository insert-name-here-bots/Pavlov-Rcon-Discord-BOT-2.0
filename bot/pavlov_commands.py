from pavlov import PavlovRCON
import discord 
from discord.ext import commands

class pavlov_rcon(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
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
    

    @commands.command()
    async def kick(self, ctx, steamid = None):
        if steamid == None:
            await ctx.send("please provide a steamid")
            return
        #checks if the user has moderator role
        f = open("roles.txt", "r")
        admin_role = f.readline()
        moderator_role = f.readline()
        f.close()
        if moderator_role.strip() in [y.name for y in ctx.author.roles]:
            pass
        elif admin_role.strip() in [y.name for y in ctx.author.roles]:
            pass
        else:
            await ctx.send("you do not have permission to use this command")
            return
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()
        
        f.close()
        
        #connects to the server
        rcon = PavlovRCON(ip.strip(), port.strip(), password.strip())
        
        
        command = await rcon.send("kick " + steamid)
        if command["Successful"] == False:
            await ctx.send("failed to connect to the server")
            return
        
        else:
            await ctx.send("kicked player " + steamid)
        await rcon.close()
    @commands.command()
    async def ban(self, ctx, steamid = None):
        if steamid == None:
            await ctx.send("please provide a steamid")
            return
        #checks if the user has admin role
        f = open("roles.txt", "r")
        admin_role = f.readline()
        f.close()
        if admin_role.strip() in [y.name for y in ctx.author.roles]:
            pass
        else:
            await ctx.send("you do not have permission to use this command")
            return
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()
        
        f.close()
        
        #connects to the server
        rcon = PavlovRCON(ip.strip(), port.strip(), password.strip())
        
        
        command = await rcon.send("ban " + steamid)
        if command["Successful"] == False:
            await ctx.send("failed to connect to the server")
            return
        
        else:
            await ctx.send("banned player " + steamid)
        await rcon.close()
    @commands.command()
    async def unban(self, ctx, steamid = None):
        if steamid == None:
            await ctx.send("please provide a steamid")
            return
        #checks if the user has ADMIN role
        f = open("roles.txt", "r")
        admin_role = f.readline()
        f.close()
        if admin_role.strip() in [y.name for y in ctx.author.roles]:
            pass
        else:
            await ctx.send("you do not have permission to use this command")
            return
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()
        
        f.close()
        
        #connects to the server
        rcon = PavlovRCON(ip.strip(), port.strip(), password.strip())
        
        
        command = await rcon.send("unban " + steamid)
        if command["Successful"] == False:
            await ctx.send("failed to connect to the server")
            return
        
        else:
            await ctx.send("unbanned player " + steamid)
        await rcon.close()
    @commands.command()
    async def banlist(self, ctx):
        #checks if the user has moderator role
        f = open("roles.txt", "r")
        admin_role = f.readline()
        moderator_role = f.readline()
        f.close()
        if moderator_role.strip() in [y.name for y in ctx.author.roles]:
            pass
        elif admin_role.strip() in [y.name for y in ctx.author.roles]:
            pass
        else:
            await ctx.send("you do not have permission to use this command")
            return
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()
        
        f.close()
        
        #connects to the server
        rcon = PavlovRCON(ip.strip(), port.strip(), password.strip())
        
        
        command = await rcon.send("banlist")
        if command["Successful"] == False:
            await ctx.send("failed to connect to the server")
            return
        
        else:
            await ctx.send(command["BanList"])
        await rcon.close()
    @commands.command()
    async def kill(self, ctx, steamid = None):
        if steamid == None:
            await ctx.send("please provide a steamid")
            return
        #checks if the user has moderator role
        f = open("roles.txt", "r")
        admin_role = f.readline()
        moderator_role = f.readline()
        f.close()
        if moderator_role.strip() in [y.name for y in ctx.author.roles]:
            pass
        elif admin_role.strip() in [y.name for y in ctx.author.roles]:
            pass
        else:
            await ctx.send("you do not have permission to use this command")
            return
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()
        
        f.close()
        
        #connects to the server
        rcon = PavlovRCON(ip.strip(), port.strip(), password.strip())
        
        
        command = await rcon.send("kill " + steamid)
        if command["Successful"] == False:
            await ctx.send("failed to connect to the server")
            return
        
        else:
            await ctx.send("killed player " + steamid)
        await rcon.close()
    @commands.command()
    @commands.is_owner()
    async def addmod(self, ctx, *, steamid = None):
        if steamid == None:
            await ctx.send("please provide a steamid")
            return
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()
        
        f.close()
        
        #connects to the server
        rcon = PavlovRCON(ip.strip(), port.strip(), password.strip())
        
        
        command = await rcon.send("AddMod " + steamid)
        if command["Successful"] == False:
            await ctx.send("failed to connect to the server")
            return
        
        else:
            await ctx.send("added moderator " + steamid)
        await rcon.close()

    @commands.command()
    @commands.is_owner()
    async def removemod(self, ctx, *, steamid = None):
        if steamid == None:
            await ctx.send("please provide a steamid")
            return
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()
        
        f.close()
        
        #connects to the server
        rcon = PavlovRCON(ip.strip(), port.strip(), password.strip())
        
        
        command = await rcon.send("RemoveMod " + steamid)
        if command["Successful"] == False:
            await ctx.send("failed to connect to the server")
            return
        else:
            await ctx.send("Removed moderator " + steamid)
        await rcon.close()
    @commands.command()
    async def rotatemap(self, ctx):
        #checks if the user has asmin role
        f = open("roles.txt", "r")
        admin_role = f.readline()
        f.close()
        
        if admin_role.strip() in [y.name for y in ctx.author.roles]:
            pass
        else:
            await ctx.send("you do not have permission to use this command")
            return
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()
        
        f.close()
        
        #connects to the server
        rcon = PavlovRCON(ip.strip(), port.strip(), password.strip())
        
        
        command = await rcon.send("RotateMap")
        if command["Successful"] == False:
            await ctx.send("failed to connect to the server")
            return
        
        else:
            await ctx.send("Rotated map")
        await rcon.close()
    @commands.command()
    async def maplist(self, ctx):
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()
        
        f.close()
        
        #connects to the server
        rcon = PavlovRCON(ip.strip(), port.strip(), password.strip())
        
        
        command = await rcon.send("MapList")
        if command["Successful"] == False:
            await ctx.send("failed to connect to the server")
            return
        
        else:
            await ctx.send(command["MapList"])
        await rcon.close()
    @commands.command()
    @commands.is_owner()
    async def switcmap(self, ctx , mapid = None, gamemode = None):
        if mapid == None:
            await ctx.send("please provide a mapid")
            return
        if gamemode == None:
            await ctx.send("please provide a gamemode")
            return
        f = open("server.txt", "r")
        ip = f.readline()
        port = f.readline()
        password = f.readline()

        f.close()

        #connects to the server
        rcon = PavlovRCON(ip.strip(), port.strip(), password.strip())


        command = await rcon.send("SwitchMap " + mapid + " " + gamemode)
        if command["Successful"] == False:
            await ctx.send("failed to connect to the server")
            return
        
        else:
            await ctx.send("Switched map to " + mapid + " " + gamemode)
        await rcon.close()


