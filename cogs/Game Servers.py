import asyncio

from discord.ext import commands
import discord
import cogs.PterodactylAPI as ptero
import json


class Game_Servers(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.file = "Whitelist.txt"

    def check(self, FILE, ID,):
        with open(FILE, "r") as file:
            if ID in file.read():
                return True
            else:
                return False

    def add(self, FILE, ID, USER=None):
        with open(FILE, "w") as file:
            file.write(ID + " Whitelisted: /" + USER + "\n")

    def delete(self,FILE, ID):
        done = False
        with open(FILE, "r") as file:
            d = file.readlines()
        with open(FILE, "w") as file:
            for i in d:
                if ID not in i:
                    file.writelines(i)
                    print("No")
                else:
                    i = str(i)
                    ptero.removewhitelist(i.split("/", 1)[1])
                    done = True
                    pass
        if done == True:
            return True
        else:
            return False

    @commands.command(alias="rwl")
    async def removewhitelist(self, ctx):
        t1 = discord.utils.get(ctx.guild.roles, name="Twitch Subscriber: Tier 1")  # Gets the role "Mod" from the server
        t2 = discord.utils.get(ctx.guild.roles, name="Twitch Subscriber: Tier 2")  # Gets the role ":)" from the server
        t3 = discord.utils.get(ctx.guild.roles, name="Twitch Subscriber: Tier 3")  # Gets the role ":)" from the server
        mod = discord.utils.get(ctx.guild.roles, name="Mods")
        await ctx.message.delete()
        if t1 in ctx.author.roles or t2 in ctx.author.roles or t3 in ctx.author.roles or mod in ctx.author.roles:  # Checks if the user that sent the command has the correct role
            author = ctx.author.mention
            if self.delete(self.file, author):
                response = await ctx.send("I have removed you from the whitelist")
            else:
                response = await ctx.send("You are not in the whitelist")
            await asyncio.sleep(2)
            await response.delete()

    @commands.command()
    async def whitelist(self, ctx, *, Name):
        t1 = discord.utils.get(ctx.guild.roles, name="Twitch Subscriber: Tier 1")  # Gets the role "Mod" from the server
        t2 = discord.utils.get(ctx.guild.roles, name="Twitch Subscriber: Tier 2")  # Gets the role ":)" from the server
        t3 = discord.utils.get(ctx.guild.roles, name="Twitch Subscriber: Tier 3")  # Gets the role ":)" from the server
        mod = discord.utils.get(ctx.guild.roles, name="Mods")
        await ctx.message.delete()
        if t1 in ctx.author.roles or t2 in ctx.author.roles or t3 in ctx.author.roles or mod in ctx.author.roles:  # Checks if the user that sent the command has the correct role
            file = self.file
            author = ctx.author.mention
            if self.check(file, author):
                response = await ctx.send("You have already whitelisted an account")
                pass
            elif not self.check(file, author):
                ptero.whitelist(Name)
                response = await ctx.send(f"{ctx.author.mention} I have whitelisted {Name}")
                self.add(file, author, Name)

        else:
            response = await ctx.send("You are not subbed to Demomute")
        await asyncio.sleep(2)
        await response.delete()


def setup(client):
    client.add_cog(Game_Servers(client))
