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
client = commands.Bot(command_prefix=prefix, intents=intents,case_insensitive=True)


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
    await send("I have started successfully", 834074140284813333)


@client.command()
async def shutdown(ctx):  # Turns the bot off
    botmin = discord.utils.get(ctx.guild.roles, name="Bot Admin")##Gets the role "Bot Admin" from the server
    if botmin in ctx.author.roles:#Checks if the user that sent the command has the correct role
        print("Recieved shutdown command")
        await ctx.send("Shutting the bot down")
        Youtube.stop()
        Twitch.stop()
        await client.close()
    else:
        await ctx.send("You're not a Bot Admin!")
        print("Someone tried to shut me down", ctx.author.mention)


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

@tasks.loop(seconds=60)
async def Twitch():
    global done
    if done == 1:
        check = TwitchAPI.checkUser("demomute", AUTH)
        print("Is there still a live stream? ", check)
        if check == False:
            done = 0
            print("Recieved no live stream starting to check for one again")

    elif TW == "True":
        print("Checking for twtich livestream")
        username = 'demomute'
        if TwitchAPI.checkUser(username, AUTH) == True:
            done = 1
            name = TwitchAPI.getstream(username, AUTH) +' <@&834095415707041805>'
            print(name)
            await send(name, 834094513944920124)

    else:
        pass


@client.command(pass_context=True)
async def BadDog(ctx):
    mod = discord.utils.get(ctx.guild.roles, name="Mod")#Gets the role "Mod" from the server
    admin = discord.utils.get(ctx.guild.roles, name=":)")#Gets the role ":)" from the server
    if mod or admin in ctx.author.roles:#Checks if the user that sent the command has the correct role
        await ctx.send("<:FeelsSadFrogoman:834217399662149662>")
    else:
        await ctx.send("You're not my owner!")


@client.command(pass_context=True)
async def Goodboi(ctx):
    mod = discord.utils.get(ctx.guild.roles, name="Mod")#Gets the role "Mod" from the server
    admin = discord.utils.get(ctx.guild.roles, name=":)")#Gets the role ":)" from the server
    if mod or admin in ctx.author.roles:#Checks if the user that sent the command has the correct role
        await ctx.send("<:FeelsHappyFrogoman:834217354560274482>")
    else:
        await ctx.send("I am a good boi but you're clearly not ")
client.load_extension("cogs.welcome")
client.load_extension("cogs.Private_Messages")  # Loads the Private_messages.py as a "cog"

try:
    client.run(dotenv.get_key(".env", "APIKEY"))  ##Starts the bot
except discord.errors.LoginFailure:
    print("Please add a token to the .env")
