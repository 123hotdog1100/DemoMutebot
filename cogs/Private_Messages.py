import discord
from discord.ext import commands


#This file is to deal with all of the private message issues
class Private(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        guild = self.client.get_guild(833822533136416808)
        try:
            if message.channel.id == message.author.dm_channel.id:  # Checks to see if the message was sent in a
                # private message
                dm = message.channel.id
                channel = self.client.get_channel(834920642096529408)  # Sends message to a channel which the bot has
                # access to
                dms = self.client.get_channel(dm)
                username = message.author.display_name
                name = f'Help for {username}'
                await guild.create_text_channel(name, category=851963274694230066)
                serverchan = discord.utils.get(guild.channels, name=name)
                print(serverchan)
                senddm = "We will look in to this for you"
                await dms.send(senddm)
                send = message.author.mention + " Needs help with: " + message.content + ": Please help them " + \
                       "<@&833822769048977409>"  # The message to send
                print(send)  # Out puts message to console for logging reasons
                await channel.send(send)  # Sends the help request to the channel variable
            else:
                return
        except Exception as e:  # Catches exceptions so the bot doesn't crash out
            print(e)
            pass



def setup(client):
    client.add_cog(Private(client))
