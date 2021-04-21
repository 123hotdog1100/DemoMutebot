import discord

from discord.ext import commands, tasks
from discord.utils import get
import cogs.TwitchAPI as TwitchAPI
import cogs.YoutubeAPI as YoutubeAPI

global store
store = 0
prefix = '$'

client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game("Message me for help"))
    Youtube.start()


@client.command()
async def shutdown(ctx):
    print("Recieved shutdown command")
    await ctx.send("Shutting the bot down")
    Youtube.stop
    await client.close()


async def send(message):
    channel = client.get_channel(834168559843147816)
    await channel.send(message)


@tasks.loop(seconds=30)
async def Youtube():
    global store
    # mentionYT = get(client. name="YT Alerts")
    print("Checking Youtube")
    num = YoutubeAPI.check('123hotdog1100')
    num = int(num)
    print(num)
    if num > store:
        test = "Demomute Just uploaded!! ", YoutubeAPI.conversion("demomute"), " <@&834169017480642572>"
        str = ''.join(test)

        await send(str)


# client.load_extension("cogs.loop")


client.run('ODM0MjA0MDg1MzU0NzU4MTY1.YH9fGA.niuPLQf2pf00IpQApzqvofvHt_k')
