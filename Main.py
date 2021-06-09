import discord
from discord.ext import commands, tasks
import dotenv
import os


intents = discord.Intents.default()
intents.members = True
global store, done
done = 0
store = 0


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
        f.write("PREFIX=%\n")
        f.write("DEBUG=False\n")
        f.close()
        print("Please enter all your values in to the .env file and restart")

prefix = dotenv.get_key(".env", "PREFIX")  # Sets the prefix that the bot will use
print("Prefix set to", prefix)
client = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True)

debug = dotenv.get_key(".env", "DEBUG")

from cogs import TwitchAPI as TwitchAPI  # Imports custom twitchAPI libary
from cogs import YoutubeAPI as YoutubeAPI  # Imports custom YoutubeAPI libary

AUTH = TwitchAPI.getOauth()


@client.event
async def on_ready():  ##Waits for login and prints to the console that it has logged in and displays the user
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game("Message me for help"))  # Changes the bot's status to the string specified
    Twitch.start()
    Youtube.start()  ##Starts the youtube loop
    await send("I am in debug mode i will not check for twitch streams", 834074140284813333)
    await send("I have started successfully", 834074140284813333)


@client.command(alias="Shutdown", brief="Turns the bot off", description="Turns the bot off but requires bot admin role")
async def shutdown(ctx):  # Turns the bot off
    botmin = discord.utils.get(ctx.guild.roles, name="Bot Admin")  ##Gets the role "Bot Admin" from the server
    if botmin in ctx.author.roles:  # Checks if the user that sent the command has the correct role
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


if debug == "False":
    YT = "False"
else:
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


if debug == "True":
    TW = "False"
else:
    TW = dotenv.get_key(".env", "LIVENOT")
print("Twitch video notifications set to:", TW)


@tasks.loop(seconds=15)
async def Twitch():
    global done
    if done == 1:
        check = TwitchAPI.checkUser("demomute", AUTH)
        print("Is there still a live stream?", check)
        if not check:
            done = 0
            chan = client.get_channel(834094513944920124)
            await chan.edit(name="Stream-Offline")
            print("Recieved no live stream starting to check for one again")

    elif TW == "True":
        print("Checking for twtich livestream")
        username = 'demomute'
        if TwitchAPI.checkUser(username, AUTH) == True:
            done = 1
            name = TwitchAPI.getstream(username, AUTH) + ' <@&834095415707041805>'
            print(name)
            chan = client.get_channel(834094513944920124)
            await send(name, 834094513944920124)
            await chan.edit(name="Now-Live!")
        else:
            print("No Stream detected")
    else:
        pass


@client.command(pass_context=True,alias="badboi")#,brief="Tells me I'm a bad boy")
async def Badboi(ctx):
    mod = discord.utils.get(ctx.guild.roles, name="Mods")  # Gets the role "Mod" from the server
    admin = discord.utils.get(ctx.guild.roles, name=":)")  # Gets the role ":)" from the server
    if mod or admin in ctx.author.roles:  # Checks if the user that sent the command has the correct role
        await ctx.send("<:FeelsSadFrogoman:834217399662149662>")
    else:
        await ctx.send("You're not my owner!")


@client.command(pass_context=True,alias="goodboi",brief="Tells me I'm a good boy")
async def Goodboi(ctx):
    mod = discord.utils.get(ctx.guild.roles, name="Mod")  # Gets the role "Mod" from the server
    admin = discord.utils.get(ctx.guild.roles, name=":)")  # Gets the role ":)" from the server
    if mod or admin in ctx.author.roles:  # Checks if the user that sent the command has the correct role
        await ctx.send("<:FeelsHappyFrogoman:834217354560274482>")
    else:
        await ctx.send("I am a good boi but you're clearly not ")


client.load_extension("cogs.welcome")
client.load_extension("cogs.Private_Messages")  # Loads the Private_messages.py as a "cog"
print("Debug? ", debug)
print("Starting Bot now!")
try:
    client.run(dotenv.get_key(".env", "APIKEY"))  ##Starts the bot
except discord.errors.LoginFailure:
    print("Please add a token to the .env")
