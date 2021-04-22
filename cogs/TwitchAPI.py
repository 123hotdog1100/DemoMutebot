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


def checkUser(userID):##Checks to see if someone is live

    try:
        req = requests.get(BASE_URL, HEADERS)
        jsondata = req.json()
        if 'stream' in jsondata:
            if jsondata['stream'] is not None:
                return True
            else:
                return False
    except Exception as e:
        print("Error checking user: ", e)
        return False


def getUserID(Username, OAUTH):##Gets the USERSID based on the Username they are given and also uses the OAUTH token generated above
    HEADERS = {'client-id': CLIENT_ID, 'Authorization': 'Bearer ' + OAUTH}
    print(HEADERS)
    URL = BASE_URL + "users?login="
    try:
        req = requests.get(URL, HEADERS)
        print(req)
        jsondata = req.json()
        print(jsondata)

    except Exception as e:
        print("Error getting ID for: ", Username, "Caused by: ", e)


#AUTH = getOauth()

#getUserID("demomute", AUTH)
