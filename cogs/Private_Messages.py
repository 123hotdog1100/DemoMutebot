from discord.ext import commands
import discord
channel = 0

class Private(commands.Cog):
    def __init__(self, client):
        global channel
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.channel.id == message.author.dm_channel.id:
                channel = self.client.get_channel(834920642096529408)
                send = message.author.mention + "Has requested Help because of " + message.content
                print(send)
                await channel.send(send)
            else:
                pass
        except Exception as e:
            pass


def setup(client):
    client.add_cog(Private(client))
