from datetime import datetime

import discord
from discord.ext import commands


# This file is to deal with all of the private message issues
class Help_Requests(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        guild = self.client.get_guild(833822533136416808)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.read_messages = True
        senddm = "I have created a help channel for you mods will talk to you in there"
        category = discord.utils.get(guild.categories, name="Help")
        try:
            if message.channel.id == message.author.dm_channel.id:  # Checks to see if the message was sent in a
                # private message
                dm = message.channel.id
                dms = self.client.get_channel(dm)
                username = message.author.display_name
                channame = f'Help for {username}'
                channamecheck = f'help-for-{username}'
                for channels in guild.channels:
                    if channels.name == channamecheck:
                        check = True
                        break
                    elif channels.name is not channamecheck:
                        check = False

                if check == True:
                    await dms.send("You already have a support case please message in that channel")
                elif check == False:
                    await guild.create_text_channel(channame, category=category)
                    await dms.send(senddm)

                for channel in guild.channels:
                    if channel.name == channamecheck:
                        chan = self.client.get_channel(channel.id)
                        await chan.set_permissions(message.author, overwrite=overwrite)

                send = "Please Help with: " + message.content
                if check == True:
                    embedvar = discord.Embed(title="Help Request")
                    embedvar.add_field(name="Issue", value=send)
                    await channel.send(embed=embedvar)
                    pass
                else:

                    embedvar = discord.Embed(title="Help Request")
                    embedvar.add_field(name="Issue", value=send)
                    await channel.send("<@&833822769048977409>")
                    await channel.send(f"Mods will be with you shortly, {message.author.mention}")
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

    @commands.command(brief="Closes a help channel")
    async def close(self, ctx):
        channamecheck = "help-for-"
        if channamecheck in ctx.channel.name:
            await ctx.channel.delete()
            print(f"Closing {ctx.channel.name}")
        else:
            await ctx.send("I can only close Help channels")
            pass


def setup(client):
    client.add_cog(Help_Requests(client))