import discord as d
import twitch

helix = twitch.Helix('nko3em2c413ryes2p2ntgz7an4m7i0','lcexkl5x47e3oqqxt57va40y1jc03u')

class MyClient(d.Client):
    async def on_ready(self):
        print('Successfully Connected')
        await client.change_presence(activity=d.Game("Message me for help"))


client = MyClient()
client.run('')
