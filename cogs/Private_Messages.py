from datetime import datetime

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
                send = message.author.mention + " Needs help with: " + message.content
                print(send)  # Out puts message to console for logging reasons

                embedvar = discord.Embed(title="Help Request")
                embedvar.add_field(name="Help request", value=send)
                await channel.send("<@&833822769048977409>")
                await channel.send(embed=embedvar)
            else:
                return
        except Exception as e:  # Catches exceptions so the bot doesn't crash out
            with open("Private_Messages.py Error.txt", "a") as f:
                e = str(e)
                if e == "'ClientUser' object has no attribute 'dm_channel'":
                    pass
                else:
                    f.write(str(datetime.now()) + "   " + e + "\n")
            pass



def setup(client):
    client.add_cog(Private(client))
