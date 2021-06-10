import discord

from discord.ext import commands


# This file is to deal with all of the private message issues
class User_Management(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(alias="kick")
    async def Kick(self, ctx, member : discord.Member):
        pass



def setup(client):
    client.add_cog(User_Management(client))
