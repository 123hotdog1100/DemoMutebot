import discord
from discord.ext import commands, tasks
import dotenv
import os
import sys
intents = discord.Intents.default()
intents.members = True
global store, done
done = 0
store = 0
prefix = '$'  # Sets the prefix that the bot will use
client = commands.Bot(command_prefix=prefix, intents=intents)


if os.path.isfile(".env"):  ##Checks to see if there is a .env file and if there isn't it will create it
    print("Discovered .env File")
else:
    print(".env file not found creating now")
    key = input("Please input your API key for the bot: ")
    with open(".env", "a") as f:  ##Adds all the relevent keys to the .env file it is creating
        f.write("APIKEY=")
        f.write(key + "\n")
        f.write("LIVENOT=\n")
        f.write("YTVIDNOT=\n")
        f.write("GOOGLEAPI=\n")
        f.write("TWITCHAPI=\n")
        f.write("TWITCHAPISECRET=\n")
        f.close()
        print("Please enter all your values in to the .env file and restart")

from cogs import TwitchAPI as TwitchAPI  # Imports custom twitchAPI libary
from cogs import YoutubeAPI as YoutubeAPI  # Imports custom YoutubeAPI libary


AUTH = TwitchAPI.getOauth()

@client.event
async def on_ready():  ##Waits for login and prints to the console that it has logged in and displays the user
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(
        activity=discord.Game("Message me for help"))  # Changes the bot's status to the string specified
    Twitch.start()
    Youtube.start()  ##Starts the youtube loop


@client.command()
async def shutdown(ctx):  # Turns the bot off
    print("Recieved shutdown command")
    await ctx.send("Shutting the bot down")
    Youtube.stop()
    Twitch.stop()
    await client.close()


@client.command()
async def notlive(ctx):
    global done
    print("Recieved not live")
    await ctx.send("Recieved beging to check again")
    done = 0

async def send(message, channelid):  ##Send function which some other functions use
    channel = client.get_channel(channelid)
    await channel.send(message)


YT = dotenv.get_key(".env", "YTVIDNOT")  ##Gets the YT Notification option
print("Youtube video Notifications set to: " + YT)  # Prints what the option was set to


@tasks.loop(seconds=30)
async def Youtube():  ##Checks youtube for a new upload
    global store
    username = 'demomute'
    if YT == "True":
        print("Checking Youtube")
        num = YoutubeAPI.check(username)
        num = int(num)
        print("Checked value: ", num, "Cached Value: ", store)
        if num > store:
            test = "Demomute Just uploaded!! ", YoutubeAPI.conversion(username), " <@&834169017480642572>"
            str = ''.join(test)
            await send(str, 834168559843147816)
            store = num
        elif num < store:
            store = num
        else:
            pass


TW = dotenv.get_key(".env", "LIVENOT")
print("Twitch video notifications set to:", TW)

@tasks.loop(seconds=30)
async def Twitch():
    global done
    if done == 1:
        pass

    elif TW == "True":
        print("Checking for twtich livestream")
        done = 1
        username = 'demomute'
        if TwitchAPI.checkUser(username, AUTH) == True:
            name = TwitchAPI.getstream(username, AUTH) +' <@&834095415707041805>'
            print(name)
            await send(name, 834094513944920124)

    else:
        pass


client.load_extension("cogs.welcome")
client.load_extension("cogs.Private_Messages")  # Loads the Private_messages.py as a "cog"

try:
    client.run(dotenv.get_key(".env", "APIKEY"))  ##Starts the bot
except discord.errors.LoginFailure:
    print("Please add a token to the .env")
