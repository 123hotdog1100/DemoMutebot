from discord.ext import tasks, commands
import discord
import cogs.TwitchAPI as TwitchAPI
import cogs.YoutubeAPI as YoutubeAPI

user_login = 'demomute'
query = TwitchAPI.get_user_query(user_login)


class loop(commands.Cog):
    global store
    store = 0

    def __init__(self, client):
        self.client = client
        #  self.printer.start()
        self.Youtube.start(client)



    def cog_unload(self):
        print("Looping stopping")
        self.Youtube.stop()

    # @tasks.loop(seconds=10.0, reconnect=True)
    # async def printer(self):
    # print("Looping")
    # print(query)
    #  response = TwitchAPI.get_response(query)
    #   TwitchAPI.print_response(response)

    # @printer.before_loop
    # async def before_printer(self):
    # print("Waiting")
    # await self.client.wait_until_ready()

def setup(client):
    client.add_cog(loop(client))
