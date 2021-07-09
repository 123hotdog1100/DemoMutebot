from datetime import datetime

import discord
from discord.ext import commands

class Vote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener
    async def on_reaction_add(self,reaction, user : discord.member):
        pass



    @commands.command()
    async def Vote(self,ctx ,*, vote):
        embed = discord.Embed(title="Voting")
        embed.add_field(name="Please vote on", value=vote)
        message = await ctx.send(embed=embed)
        await message.add_reaction("\N{white_check_mark}")
        await message.add_reaction("\N{no_entry_sign}")



def setup(client):
    client.add_cog(Vote(client))