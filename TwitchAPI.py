import requests, json, sys
from time import sleep

BASE_URL = 'https://api.twitch/helix/'
CLIENT_ID = 'nko3em2c413ryes2p2ntgz7an4m7i0'
HEADERS = {'Client-ID': CLIENT_ID}
INDENT = 2


def get_response(querry):
    url = BASE_URL + querry
    sleep(2)
    response = requests.get(url, headers=HEADERS)
    return response


def print_response(response):
    response_json = response.json()
    print_response = json.dumps(response_json, indent=INDENT)
    print(print_response)


def get_user_streams_querry(user_login):
    try:
        return 'streams?user_login={0}'.format(user_login)
    except requests.exceptions.ConnectionError:
        return "Connection refused"


def get_user_query(user_login):
    try:
        return 'users?login={0}'.format(user_login)
    except requests.exceptions.ConnectionError:
        return "Connection refused"
