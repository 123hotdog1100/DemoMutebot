from pydactyl import PterodactylClient
import dotenv

Key = dotenv.get_key(".env", "PTEROKEY")

client = PterodactylClient('http://ptero.rpelliott.tk/', Key)
def whitelist(Player):
    client.client.send_console_command("0137f295", f"whitelist add {Player}")


