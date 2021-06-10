import asyncio

import discord

from discord.ext import commands
from discord.ext.commands import Cog


# This file is to deal with all of the private message issues
class User_Management(commands.Cog):
    def __init__(self, client):
        self.client = client
        guild = self.client.get_guild(833822533136416808)


    @commands.command(alias="kick", brief="kick a user", pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def Kick(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            reason = "No reason given"
        output = f"The moderator {ctx.author.mention} has kicked {member} for {reason}"
        await member.kick(reason=reason)
        embedvar = discord.Embed(title="Kick output")
        embedvar.add_field(name="Issue", value=output)
        response = await ctx.send(embed=embedvar)
        await asyncio.sleep(1)
        await response.delete()
        await ctx.message.delete()
        await self.client.get_channel(834074140284813333).send(embed=embedvar)


    @commands.command(alias="ban", brief="ban a user")
    @commands.has_permissions(ban_members=True)
    async def Ban(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            reason = "No reason given"
        output = f"The moderator {ctx.author.mention} has kicked {member} for {reason}"
        embedvar = discord.Embed(title="Kick output")
        embedvar.add_field(name="Issue", value=output)
        response = await ctx.send(embed=embedvar)
        await member.ban(reason=reason)
        await asyncio.sleep(2)
        await response.delete()
        await ctx.message.delete()
        await self.client.get_channel(834074140284813333).send(embed=embedvar)


    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingPermissions):
            response = await ctx.send("You do not have the required permissions for this command")
            await asyncio.sleep(2)
            await response.delete()
            print(f"{ctx.author} Tried to use a elevated command in User_Management.py")
            await self.client.get_channel(834074140284813333).send(
                f"{ctx.author} Tried to use a elevated command in User Management Cog")


def setup(client):
    client.add_cog(User_Management(client))
