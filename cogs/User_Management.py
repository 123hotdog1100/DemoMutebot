import discord

from discord.ext import commands


# This file is to deal with all of the private message issues
class User_Management(commands.Cog):
    def __init__(self, client):
        self.client = client
        guild = self.client.get_guild(833822533136416808)

    @commands.command(alias="kick", brief="kick a user")
    async def Kick(self, ctx, member: discord.Member, *, reason=None):
        admin = discord.utils.get(ctx.guild.roles, name=":)")  # Gets the role ":)" from the server
        mods = discord.utils.get(ctx.guild.roles, name="Mods")  # Gets the role ":)" from the server
        output = f"The user{ctx.author.mention} has kicked {member} for {reason}"
        if admin or mods in ctx.author.roles:
            await member.kick(reason=reason)
            embedvar = discord.Embed(title="Kick output")
            embedvar.add_field(name="Issue", value=output)
            await ctx.send(embed=embedvar)
        else:
            ctx.send("You do not have permission to use this command")
            pass



    @commands.command(alias="ban", brief="ban a user")
    async def Ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)


def setup(client):
    client.add_cog(User_Management(client))
