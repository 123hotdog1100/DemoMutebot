import asyncio
import cogs.SQLite as S
import discord

from discord.ext import commands
from discord.ext.commands import Cog


# This file is to deal with all of the private message issues
class User_Management(commands.Cog):
    def __init__(self, client):
        self.client = client
        guild = self.client.get_guild(833822533136416808)


    def get_id(self, member):
        id = member.mention
        id = id.strip("<")
        id = id.strip("@")
        id = id.strip(">")
        return id

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

    @commands.command(alias="tempban", brief="tempbans a user", description="This command tempbans a user")
    @commands.has_permissions(ban_members=True)
    async def Tempban(self, ctx, member: discord.Member, time, *, reason=None):
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        tempban = int(time[0]) * time_convert[time[-1]]
        if reason is None:
            reason = "No reason given"
        output = f"The moderator {ctx.author.mention} has Temp banned {member} for the duration of {time} and for the reason: {reason}"
        timeout = f"The ban for {member} has timed out and there for they have been unbanned"
        embedvar = discord.Embed(title="Tempban output")
        embedvar.add_field(name="Issue", value=output)
        response = await ctx.send(embed=embedvar)
        embedvar2 = discord.Embed(title="tempban timeout")
        embedvar2.add_field(name="repsonse", value=timeout)
        await member.ban(reason=reason)
        await asyncio.sleep(2)
        await response.delete()
        await ctx.message.delete()
        await self.client.get_channel(834074140284813333).send(embed=embedvar)
        await asyncio.sleep(tempban)
        await ctx.guild.unban(member)
        await self.client.get_channel(834074140284813333).send(embed=embedvar2)

    @commands.command(alias="tempmute", brief="tempmutes a user", description="This command tempmutes a user")
    @commands.has_permissions(ban_members=True)
    async def Tempmute(self, ctx, member: discord.Member, time, *, reason=None):
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        tempban = int(time[0]) * time_convert[time[-1]]
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if reason is None:
            reason = "No reason given"
        output = f"The moderator {ctx.author.mention} has Temp muted {member} for the duration of {time} and for the reason: {reason}"
        timeout = f"The mute for {member} has timed out and there for they have been unmuted"
        embedvar = discord.Embed(title="Tempmute output")
        embedvar.add_field(name="Issue", value=output)
        response = await ctx.send(embed=embedvar)
        embedvar2 = discord.Embed(title="Tempmute timeout")
        embedvar2.add_field(name="repsonse", value=timeout)
        dm = member.mention.strip("<")
        dm = dm.strip("@")
        dm = dm.strip(">")
        print(dm)
        print(member.mention)
        channel = await member.create_dm()
        server = "Demomute"
        await channel.send(f"You was Temp muted on {server} for {time} by {ctx.author.mention}")
        await member.add_roles(role)
        await asyncio.sleep(2)
        await response.delete()
        await ctx.message.delete()
        await self.client.get_channel(834074140284813333).send(embed=embedvar)
        await asyncio.sleep(tempban)
        await member.remove_roles(role)
        await self.client.get_channel(834074140284813333).send(embed=embedvar2)
        await channel.send(f"You are no longer temp muted on {server}")

    @Ban.error
    async def Ban_error(self, ctx, error):
        print(error)
        if isinstance(error, discord.ext.commands.errors.MissingPermissions):
            response = await ctx.send("You do not have the required permissions for this command")
            await asyncio.sleep(2)
            await response.delete()
            print(f"{ctx.author} Tried to use a elevated command in User_Management.py")
            await self.client.get_channel(834074140284813333).send(
                f"{ctx.author} Tried to use a elevated command in User Management Cog")
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            response = await ctx.send("This command requires a member and time arguments")
            await asyncio.sleep(4)
            await response.delete()

    @Kick.error
    async def Kick_error(self, ctx, error):
        print(error)
        if isinstance(error, discord.ext.commands.errors.MissingPermissions):
            response = await ctx.send("You do not have the required permissions for this command")
            await asyncio.sleep(2)
            await response.delete()
            print(f"{ctx.author} Tried to use a elevated command in User_Management.py")
            await self.client.get_channel(834074140284813333).send(
                f"{ctx.author} Tried to use a elevated command in User Management Cog")
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            response = await ctx.send("This command requires a member and time arguments")
            await asyncio.sleep(4)
            await response.delete()

    @Tempban.error
    async def Tempban_error(self, ctx, error):
        print(error)
        if isinstance(error, discord.ext.commands.errors.MissingPermissions):
            response = await ctx.send("You do not have the required permissions for this command")
            await asyncio.sleep(2)
            await response.delete()
            print(f"{ctx.author} Tried to use a elevated command in User_Management.py")
            await self.client.get_channel(834074140284813333).send(
                f"{ctx.author} Tried to use a elevated command in User Management Cog")
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            response = await ctx.send("This command requires a member and time arguments")
            await asyncio.sleep(4)
            await response.delete()

    @Tempmute.error
    async def Tempmute_error(self, ctx, error):
        print(error)
        if isinstance(error, discord.ext.commands.errors.MissingPermissions):
            response = await ctx.send("You do not have the required permissions for this command")
            await asyncio.sleep(2)
            await response.delete()
            print(f"{ctx.author} Tried to use a elevated command in User_Management.py")
            await self.client.get_channel(834074140284813333).send(
                f"{ctx.author} Tried to use a elevated command in User Management Cog")
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            response = await ctx.send("This command requires a member and time arguments")
            await asyncio.sleep(4)
            await response.delete()

    @commands.command()
    @commands.has_role(833822769048977409)
    async def Warn(self, ctx, member: discord.Member, *, reason=None):
        id = member.mention
        id = id.strip("<")
        id = id.strip("@")
        id = id.strip(">")
        current = S.read_using_id(id)
        username = member.display_name
        if current is None:
            S.data_entry(id, username, 1)
        elif current is not None:
            S.update(id)
        response = await ctx.send(
            f"I have warned {member.display_name} for {reason} they are now on {S.read_using_id(id)} warnings")
        dm = await member.create_dm()
        if reason == None:
            reason = "No reason given"
        S.data_entry_reasons(id, username, reason)
        embedvar = discord.Embed(title="Demomute Warning System")
        embedvar.add_field(name="You have been warned", value=f"You was warned for {reason} by {ctx.author.mention}")
        await dm.send(embed=embedvar)
        await asyncio.sleep(2)
        await response.delete()
        if S.read_using_id(id) >= 3:
            S.update_history(id)
            S.clear(id)
            tmute = self.client.get_command("Tempmute")
            await ctx.invoke(tmute, member, "1h", reason="Too many warnings")
            response2 = await ctx.send(f"{member.mention} Had more than three warnings they have been muted for 1h")
            await asyncio.sleep(2)
            await response2.delete

    @Warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingPermissions):
            response = await ctx.send("You do not have the required permissions for this command")
            await asyncio.sleep(2)
            await response.delete()
            print(f"{ctx.author} Tried to use a elevated command in User_Management.py")
            await self.client.get_channel(834074140284813333).send(
                f"{ctx.author} Tried to use a elevated command in User Management Cog")
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            response = await ctx.send("This command requires a member argument")
            await asyncio.sleep(4)
            await response.delete()

    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def Warns(self, ctx, member: discord.Member):
        id = member.mention
        id = id.strip("<")
        id = id.strip("@")
        id = id.strip(">")
        current = S.read_using_id(id)
        if current == None:
            current = 0
        history = S.read_Histroy_ID(id)
        if history == None:
            history = 0
        embedvar = discord.Embed(title="Demomute Warning System")
        embedvar.add_field(name="Current warnings", value=f"The user {member.mention} has {current} warnings")
        embedvar.add_field(name="Historical warnings", value=f"The user {member.mention} has {history} warnings")
        length = S.reasons_read_amount(id)
        number = 1
        if length == 0:
            pass
        else:
            r = S.reasons_read_using_id(id)
            try:
                for value in r:
                    reason = value
                    embedvar.add_field(name=f'Warning {number}', value=reason, inline=False)
                    number = 1 + number
            except StopIteration:
                pass

        response = await ctx.send(embed=embedvar)
        await asyncio.sleep(5)
        # await response.delete()
        await ctx.message.delete()
    @commands.command()
    @commands.has_role(833822769048977409)
    async def clearwarns(self,ctx, member: discord.Member):
        id = self.get_id(member)
        S.delete(id)
        S.clear(id)
        S.clear_history(id)
        response = await ctx.send("I have cleared the users warnings")
        await asyncio.sleep(2)
        await response.delete()

def setup(client):
    client.add_cog(User_Management(client))
