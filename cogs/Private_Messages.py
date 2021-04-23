from discord.ext import commands


#This file is to deal with all of the private message issues
class Private(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.channel.id == message.author.dm_channel.id:  # Checks to see if the message was sent in a
                # private message
                dm = message.channel.id
                channel = self.client.get_channel(834920642096529408)  # Sends message to a channel which the bot has
                # access to
                dms = self.client.get_channel(dm)
                senddm = "We will look in to this for you"
                await dms.send(senddm)
                send = message.author.mention + " Needs help with: " + message.content + " Please help them " + \
                       "<@&833822769048977409>"  # The message to send
                print(send)  # Out puts message to console for logging reasons
                await channel.send(send)  # Sends the help request to the channel variable
            else:
                return
        except Exception as e:  # Catches exceptions so the bot doesn't crash out
            pass


    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.client.get_channel(834920642096529408)
        if message.channel.id == 834920642096529408:
            history = await channel.history(limit=2).flatten()
            for msg in history:
                if 'help' in msg.content:
                    content = msg.content
                    mention = content[:content.find(">") + len(">")]
                    print("WORKING")





def setup(client):
    client.add_cog(Private(client))
