import asyncio
import discord
from discord.ext import commands
import datetime


class Vote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Vote(self, ctx, duration, *, vote):
        global message, yes, no
        mod = discord.utils.get(ctx.guild.roles, name="Mods")  # Gets the role "Mod" from the server
        admin = discord.utils.get(ctx.guild.roles, name=":)")  # Gets the role ":)" from the server
        if mod in ctx.author.roles or admin in ctx.author.roles and time == True:
            converted = str(datetime.timedelta(seconds=int(duration)))
            await ctx.message.delete()
            print("Done")
            output = False
            embed = discord.Embed(title=f"Voting. (Duration {converted})")
            # embed.set_author(name=ctx.message.display_name, url=discord.Embed.Empty, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Please vote on", value=vote)
            message = await ctx.send("<@&865011222898016287>", embed=embed)
            await message.add_reaction('✅')
            await message.add_reaction("❌")
            await asyncio.sleep(int(duration))
            yenlen = len(yes)
            nolen = len(no)
            if yenlen > nolen:
                output = True
            if yenlen == nolen:
                output2 = True
            print("test", output)
            embed2 = discord.Embed(title="Voting resaults")
            # embed2.set_author(name=ctx.message.display_name, icon_url=ctx.author.avatar_url)
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
            await ctx.message.delete()
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
