import asyncio
import discord
from discord.ext import commands, tasks
import dotenv
import os

intents = discord.Intents.default()
intents.members = True
global store, done
done = 0
store = 0

import logging

logging.basicConfig(level=logging.DEBUG, filename="Discord.log")

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
if os.path.isfile("Whitelist.txt"):
    pass
else:
    with open("Whitelist.txt", "w") as f:
        pass

prefix = dotenv.get_key(".env", "PREFIX")  # Sets the prefix that the bot will use
print("Prefix set to", prefix)
client = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True)
client.remove_command('help')

debug = dotenv.get_key(".env", "DEBUG")

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
    if debug == "True":
        await send("I am in debug mode i will not check for twitch streams", 834074140284813333)
    else:
        await send("I have started successfully", 834074140284813333)


@client.command(alias="Shutdown", brief="Turns the bot off",
                description="Turns the bot off but requires bot admin role")
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
async def Twitch():  ##Runs the twitch check using custom coded twitch api interface
    global done
    if done == 1:
        check = TwitchAPI.checkUser("demomute", AUTH)
        print("Is there still a live stream?", check)
        if not check:
            done = 0
            chan = client.get_channel(834094513944920124)
            await chan.edit(name="Stream-Offline")
            print("Recieved no live stream starting to check for one again")
            status.stop()

    elif TW == "True":
        print("Checking for twtich livestream")
        username = 'demomute'
        if TwitchAPI.checkUser(username, AUTH) == True:
            try:
                done = 1
                name = TwitchAPI.getstream(username, AUTH) + ' <@&834095415707041805>'
                chan = client.get_channel(834094513944920124)
                await send(name, 834094513944920124)
                await chan.edit(name="Now-Live!")
                status.start()
                print(name)
            except TypeError as e:
                Twitch.restart()
                print("Twitch whoopsie ", e)
                return

        else:
            print("No Stream detected")
    else:
        pass


@tasks.loop()
async def status():
    username = 'demomute'
    await client.change_presence(activity=discord.Streaming(name=TwitchAPI.getstream(username, AUTH),
                                                                url="https://www.twitch.tv/demomute"))
    await asyncio.sleep(20)
    await client.change_presence(activity=discord.Game("Message me for help"))


@status.after_loop
async def status_after_loop():
    await client.change_presence(activity=discord.Game("Message me for help"))

@client.command(pass_context=True, alias="badboi")
@commands.cooldown(1, 30, commands.BucketType.user)
async def Badboi(ctx):
    mod = discord.utils.get(ctx.guild.roles, name="Mods")  # Gets the role "Mod" from the server
    admin = discord.utils.get(ctx.guild.roles, name=":)")  # Gets the role ":)" from the server
    if mod in ctx.author.roles or admin in ctx.author.roles:  # Checks if the user that sent the command has the correct role
        await ctx.send("<:FeelsSadFrogoman:834217399662149662>")
    else:
        await ctx.send("You're not my owner!")


@client.command(pass_context=True, alias="goodboi", brief="Tells me I'm a good boy")
@commands.cooldown(1, 30, commands.BucketType.user)
async def Goodboi(ctx):
    mod = discord.utils.get(ctx.guild.roles, name="Mods")  # Gets the role "Mod" from the server
    admin = discord.utils.get(ctx.guild.roles, name=":)")  # Gets the role ":)" from the server
    vip = discord.utils.get(ctx.guild.roles, name="VIP")
    if mod in ctx.author.roles or admin in ctx.author.roles or vip in ctx.author.roles:  # Checks if the user that sent the command has the correct role
        await ctx.send("<:FeelsHappyFrogoman:834217354560274482>")
    else:
        await ctx.send("I am a good boi but you're clearly not ")


@client.command(pass_context=True, alias="c", brief="Delete amount of messages stated")
@commands.has_permissions(manage_channels=True)
async def clear(ctx, amount: int):
    if amount > 100:
        error = await ctx.send(f"{amount} is more messages then discord can handle me removing sorry.")
        help = await ctx.send("please specify an amount below 100")
        await asyncio.sleep(5)
        await help.delete()
        await error.delete()
    await ctx.channel.purge(limit=amount)
    response = await ctx.send(f"I have cleared {amount} messages")
    await asyncio.sleep(3)
    await response.delete()


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        response = await ctx.send("Please specify an amount")
        await asyncio.sleep(2)
        await ctx.message.delete()
        await response.delete()
    else:
        print(error)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        response = await ctx.send("Sorry i don't know that one.")
        await asyncio.sleep(3)
        await response.delete()
        await ctx.message.delete()
    else:
        await ctx.message.delete()
        print(error)


@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.light_grey()
    )
    await ctx.message.delete()
    embed.set_author(name='Help')
    embed.add_field(name=f"{prefix}help", value="Shows this", inline=False)
    embed.add_field(name=f"{prefix}warns", value="Shows the amount of warnings a user has had", inline=False)
    mod = discord.utils.get(ctx.guild.roles, name="Mods")
    admin = discord.utils.get(ctx.message.guild.roles, name=":)")
    vip = discord.utils.get(ctx.guild.roles, name="VIP")
    if mod in ctx.author.roles or admin in ctx.author.roles:
        embed.add_field(name=f"{mod}'s Role permissions", value=f"You get the following commands from the {mod} role")
        embed.add_field(name=f"{prefix}close", value="Closes the support channel it is used in", inline=False)
        embed.add_field(name=f"{prefix}Tempban", value="Tempbans the user for the time set", inline=False)
        embed.add_field(name=f"{prefix}Ban", value="Permanently bans the user", inline=False)
        embed.add_field(name=f"{prefix}kick", value="Kicks the user", inline=False)
        embed.add_field(name=f"{prefix}Tempmute", value="Tempmutes the user for the time set", inline=False)
        embed.add_field(name=f"{prefix}clear", value="Deleted the amount of messages stated", inline=False)
        embed.add_field(name=f"{prefix}warn", value="Warns a user and pms them the reason", inline=False)
        embed.add_field(name=f"{prefix}vote", value="Creates a vote in the Channel where the command was used",
                        inline=False)
    if vip in ctx.author.roles:
        embed.add_field(name=f"{vip}'s Role permissions", value=f"You get the following commands from the {vip} role",
                        inline=True)
        embed.add_field(name=f"{prefix}Goodboi", value="Tells me i'm a good boi", inline=False)
    await author.send(author, embed=embed)


@help.error
async def help_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandOnCooldown):
        response = await ctx.send("This command is on cooldown")
        await asyncio.sleep(2)
        await response.delete()


client.load_extension("cogs.welcome")
client.load_extension("cogs.User_Management")
client.load_extension("cogs.fun_commands")
client.load_extension("cogs.Vote")
if dotenv.get_key(".env", "GameINT") == "True":
    print("loading Game server Management")
    client.load_extension("cogs.Game Servers")
client.load_extension("cogs.Private_Messages")  # Loads the Private_messages.py as a "cog"
print("Debug? ", debug)
print("Starting Bot now")
try:
    client.run(dotenv.get_key(".env", "APIKEY"))  ##Starts the bot
except discord.errors.LoginFailure:
    print("Please add a token to the .env")
