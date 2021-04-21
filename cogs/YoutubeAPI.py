from googleapiclient.discovery import build

api_key = 'AIzaSyDtwKl2tY4NXdKRrJ139yLvUKk7qQD2vww'

youtube = build('youtube', 'v3', developerKey=api_key)



def check(Username):
    request = youtube.channels().list(
        part='statistics',
        forUsername=Username
    )
    response = request.execute()

    for item in response['items']:
        num = item['statistics']['videoCount']
        current = int(num)
        return(current)
