from discord.ext import commands

##This file is to deal with all of the private message issues
class Private(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.channel.id == message.author.dm_channel.id: #Checks to see if the message was sent in a private message
                channel = self.client.get_channel(834920642096529408)#Sends message to a channel which the bot has access to
                send = message.author.mention + " Needs help with:  " + message.content # The message to send
                print(send) #Out puts message to console for logging reasons
                await channel.send(send) #Sends the help request to the channel variable
            else:
                pass
        except Exception as e:##Catches exceptions so the bot doesn't crash out
            pass


def setup(client):
    client.add_cog(Private(client))
