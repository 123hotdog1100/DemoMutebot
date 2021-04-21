import discord

from discord.ext import commands, tasks
import cogs.TwitchAPI as TwitchAPI

prefix = '$'

client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game("Message me for help"))


@client.command()
async def shutdown(ctx):
    print("Recieved shutdown command")
    await ctx.send("Shutting the bot down")
    await client.close()


async def send(message):
    await client.send_message(client.get_channel("834168559843147816", message))


@tasks.loop(seconds=30)
async def Youtube():
    print("Checking Youtube")
    num = YoutubeAPI.check('123hotdog1100')
    num = int(num)
    print(num)
    if num > store:
        store = num
        await send(num)


# client.load_extension("cogs.loop")


store = 0
client.run('ODM0MjA0MDg1MzU0NzU4MTY1.YH9fGA.niuPLQf2pf00IpQApzqvofvHt_k')
