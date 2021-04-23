from discord.ext import commands
from discord.ext.commands import Cog


##This file is to deal with all of the welcoming things
class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_member_join(self, member):
        print(member, " has joined the server")
        await self.client.get_channel(834075240790622209).send(f"Welcome {member.mention} to the server")


def setup(client):
    client.add_cog(Welcome(client))
