import discord

from discord.ext import commands, tasks
from discord.utils import get
from cogs import TwitchAPI as TwitchAPI
from cogs import YoutubeAPI as YoutubeAPI
import dotenv
import os

global store
store = 0
prefix = '$'

client = commands.Bot(command_prefix=prefix)

if os.path.isfile(".env"):
    print("Discovered .env File")
else:
    print(".env file not found creating now")
    #key = input("Please input your API key for the bot: ")
    with open(".env", "a") as f:
        f.write("APIKEY=")
        f.write(key + "\n")
        f.write("LIVENOT=\n")
        f.close()


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


YT = dotenv.get_key(".env","YTVIDNOT")
print("Youtube video Notifications set to: " + YT)


@tasks.loop(seconds=30)
async def Youtube():
    global store
    if YT == "True":
        print("Checking Youtube")
        num = YoutubeAPI.check('123hotdog1100')
        num = int(num)
        print("Checked value: ", num, "Cached Value: ", store)
        if num > store:
            test = "Demomute Just uploaded!! ", YoutubeAPI.conversion("demomute"), " <@&834169017480642572>"
            str = ''.join(test)
            await send(str)
            store = num
        elif num < store:
            store = num
        else:
            pass


# client.load_extension("cogs.loop")
async def on_message(message):
    await client.process_commands(message)
    if message.channel.id == message.author.dm_channel:
        await message.author.send("Received your message")
    elif not message.guid:
        await message.author.send("Received your message")


try:
    client.run(dotenv.get_key(".env", "APIKEY"))
except discord.errors.LoginFailure:
    print("Please add a token to the .env")
