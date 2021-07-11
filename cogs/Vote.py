import asyncio
import discord
from discord.ext import commands


class Vote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Vote(self, ctx, duration: int, *, vote):
        global message, yes, no
        mod = discord.utils.get(ctx.guild.roles, name="Mods")  # Gets the role "Mod" from the server
        admin = discord.utils.get(ctx.guild.roles, name=":)")  # Gets the role ":)" from the server
        await ctx.message.delete()
        if mod in ctx.author.roles or admin in ctx.author.roles:
            output = False
            embed = discord.Embed(title="Voting")
            embed.add_field(name="Please vote on", value=vote)
            message = await ctx.send(embed=embed)
            await message.add_reaction('✅')
            await message.add_reaction("❌")
            await asyncio.sleep(duration)
            yenlen = len(yes)
            nolen = len(no)
            if yenlen > nolen:
                output = True
            if yenlen == nolen:
                output2 = True
            print("test", output)
            embed2 = discord.Embed(title="Voting resaults")
            if output:
                embed2.add_field(name=vote, value="Successful")
                print(vote, " Was successfull")
            if not output and not output2:
                embed2.add_field(name=vote, value="Unsuccessful")
                print(vote, " was unsuccessful")
            if output2:
                embed2.add_field(name=vote, value="Tie or noone voted")
                print(vote, " Tied")
            await message.delete()
            await ctx.send(embed=embed2)
        else:
            response = await ctx.send("You do not have permissions to do this")
            await asyncio.sleep(4)
            await response.delete()

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user: discord.member):
        global message, yes, no
        yes = []
        no = []
        print(user)
        if user != self.client.user:
            if reaction.message == message:
                if reaction.emoji == '✅':
                    yes.append(user.mention)
                elif reaction.emoji == "❌":
                    no.append(user.mention)


def setup(client):
    client.add_cog(Vote(client))
