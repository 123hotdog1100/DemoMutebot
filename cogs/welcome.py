import discord
from discord.ext import commands
from discord.ext.commands import Cog
import dotenv
debug = dotenv.get_key(".env", "DEBUG")
##This file is to deal with all of the welcoming things
class Welcome(Cog):
    def __init__(self, client):
        self.client = client


    @Cog.listener()
    async def on_member_join(self,member: discord.Member):
        print(member, " has joined the server")
        if debug == "False":
            await self.client.get_channel(834075240790622209).send(f"Welcome {member.mention} to the server")
        else:
            pass

def setup(client):
    client.add_cog(Welcome(client))
