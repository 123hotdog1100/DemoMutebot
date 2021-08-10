import discord
from discord.ext import commands
import random
import asyncio
from .DemoAPI import getlatestclip

# This file is to deal with all of the private message issues
class fun_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball', 'eightball', 'ball'])
    @commands.has_role(833822769048977409)
    async def _8ball(self, ctx, *, Question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]
        await ctx.send(f'Question : {Question}\nAnswer :{random.choice(responses)}')

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRole):
            response = await ctx.send("You do not have the Server boost role")
            await asyncio.sleep(2)
            await ctx.message.delete()
            await response.delete()
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            response = await ctx.send("Please give me a question!")
            await asyncio.sleep(4)
            await response.delete()

    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def maths(self, ctx, *, args):
        print(args)
        await ctx.message.delete()
        if "+" in args:
            list = args.split("+")
            output = int(list[0]) + int(list[1])
            output = str(output)
            await ctx.send(f"The answer is {output}")
        elif "*" in args:
            list = args.split("*")
            output = int(list[0]) * int(list[1])
            await ctx.send(f"The answer is {output}")
        elif "/" in args:
            list = args.split("/")
            output = int(list[0]) / int(list[1])
            await ctx.send(f"The answer is {output}")
        elif "-" in args:
            list = args.split("-")
            output = int(list[0]) - int(list[1])
            await ctx.send(f"The answer is {output}")

    @maths.error
    async def maths(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandOnCooldown):
            response = await ctx.send("This command is on cooldown")
            await asyncio.sleep(2)
            await response.delete()
        else:
            print(error)
            pass

    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def latestclip(self, ctx):
        await ctx.message.delete()
        latestURL = getlatestclip(1, "demomute")
        response = await ctx.send(f"The latest clip is {latestURL}")
        await asyncio.sleep(10)
        await response.delete()



def setup(client):
    client.add_cog(fun_commands(client))
