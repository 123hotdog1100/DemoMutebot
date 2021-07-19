from pydactyly import PterodactylClient
import dotenv

Key = dotenv.get_key(".env", "PTEROKEY")

client = PterodactylClient('', Key)