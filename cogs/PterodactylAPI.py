from pydactyl import PterodactylClient
import dotenv

Key = dotenv.get_key(".env", "PTEROKEY")
Server_ID = dotenv.get_key(".env", "ServerID")


client = PterodactylClient('http://ptero.rpelliott.tk/', Key)
def whitelist(Player):
    client.client.send_console_command(Server_ID, f"whitelist add {Player}")

def removewhitelist(Player):
    client.client.send_console_command(Server_ID, f"whitelist remove {Player}")
