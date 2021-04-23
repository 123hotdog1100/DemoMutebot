import requests, json, sys
from time import sleep
import dotenv

BASE_URL = 'https://api.twitch.tv/helix/'
CLIENT_ID = dotenv.get_key(".env", "TWITCHAPI")
CLIENT_SECRET = dotenv.get_key(".env", 'TWITCHAPISECRET')
OAUTHHEADERS = {'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'grant_type': 'client_credentials'}
OAUTHURL = "https://id.twitch.tv/oauth2/token"


def getOauth():##This function gets the oauth2 token which is required for interacting with the twitchAPI
    try:
        req = requests.post(OAUTHURL, OAUTHHEADERS)
        jsondata = req.json()
        if 'access_token' in jsondata:
            OAUTH = jsondata['access_token']
            return OAUTH
    except Exception as e:
        print(e)


def checkUser(userID, OAUTH):##Checks to see if someone is live
    HEADERS = {'client-id': CLIENT_ID, 'Authorization': 'Bearer ' + OAUTH}
    URL = BASE_URL + 'streams?user_login=hotdog1100'
    try:
        req = requests.get(URL, headers=HEADERS)
        jsondata = req.json()
        print(jsondata)
        if len(jsondata['data']) == 1:
            print('hotdog1100' + ' is live: ' + jsondata['data'][0]['title'] + ' playing ' + jsondata['data'][0]['game_name'])
        else:
            return False
    except Exception as e:
        print("Error checking user: ", e)
        return False


def getUserID(Username, OAUTH):##Gets the USERSID based on the Username they are given and also uses the OAUTH token generated above
    HEADERS = {'client-id': CLIENT_ID, 'Authorization': 'Bearer ' + OAUTH}
    URL = BASE_URL + "users?login=" + Username
    try:
        req = requests.get(URL, headers=HEADERS)
        jsondata = req.json()
        print(jsondata)
        if len(jsondata['data']) == 1:
            ID = jsondata['id']
            return ID

    except Exception as e:
        print(e)

    #except Exception as e:
     #   print("Error getting ID for: ", Username, "Caused by: ", e)


AUTH = getOauth()

#print(getUserID("hotdog1100", AUTH))
print(checkUser(75334882, AUTH))