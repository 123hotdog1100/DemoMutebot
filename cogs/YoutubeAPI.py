from googleapiclient.discovery import build
import dotenv

api_key = dotenv.get_key(".env", "GOOGLEAPI")

youtube = build('youtube', 'v3', developerKey=api_key)

id = 0


def check(Username):
    request = youtube.channels().list(
        part='statistics',
        forUsername=Username
    )
    response = request.execute()
    for item in response['items']:
        id = item['id']

    for item in response['items']:
        num = item['statistics']['videoCount']
        current = int(num)
        return (current)


def getid(Username):
    request = youtube.channels().list(
        part='statistics',
        id=Username
    )
    response = request.execute()
    for item in response['items']:
        id = item['id']
        return id


def latestvid(id):
    request = youtube.search().list(
        part='snippet',
        channelId=id,
        type='video'
    )
    response = request.execute()
    for item in response['items']:
        vid = item['id']['videoId']
        return vid

def conversion(Username):
    BASE_URL = "https://www.youtube.com/watch?v="
    VIDID = latestvid("UCQawg27ajRWDNuN-0ieeOrw")
    VIDURL = BASE_URL, VIDID
    str = ''.join(VIDURL)
    return str
