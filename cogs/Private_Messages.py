import discord
from discord import PermissionOverwrite
from discord.ext import commands


#This file is to deal with all of the private message issues
class Private(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        guild = self.client.get_guild(833822533136416808)
        overwrite = PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.read_messages = True
        try:
            if message.channel.id == message.author.dm_channel.id:  # Checks to see if the message was sent in a
                # private message
                dm = message.channel.id
                dms = self.client.get_channel(dm)
                username = message.author.display_name
                channame = f'Help for {username}'
                channamecheck = f'help-for-{username}'
                category = discord.utils.get(guild.categories, name="Help")
                await guild.create_text_channel(channame, category=category)
                for channel in guild.channels:
                    if channel.name == channamecheck:
                        print(channel.id)
                        chan = self.client.get_channel(channel.id)
                        await chan.set_permissions(message.author, overwrite=overwrite)

                senddm = "I have created a help channel for you mods will talk to you in there"
                await dms.send(senddm)
                send = message.author.mention + " Needs help with: " + message.content + ": Please help them " + \
                       "<@&833822769048977409>"  # The message to send
                print(send)  # Out puts message to console for logging reasons
                await channel.send(send)  # Sends the help request to the channel variable
            else:
                return
        except Exception as e:  # Catches exceptions so the bot doesn't crash out
            pass



def setup(client):
    client.add_cog(Private(client))
