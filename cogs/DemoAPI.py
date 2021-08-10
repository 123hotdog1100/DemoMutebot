import requests
import dotenv

BASE = "http://" +  dotenv.get_key(".env", "BASEAPIURL")
BASE = BASE + "/"
def get_stream(ID,Username):##Gets stream name

    r= requests.get(BASE + "sync/1", {'Command': 'getstream','ID': ID, 'Username': Username})
    return r.json()

def check_user(ID,Username):##Checks if user is live
    r = requests.get(BASE + "sync/1", {'Command': 'checkuser', 'ID': ID, 'Username': Username})
    return r.json()


def done(ID):
    r = requests.put(BASE + "sync/1")
    if r.json() == 201:
        return True

def check(ID):
    r = requests.get(BASE + "sync/1", {'Command': 'getchecked', 'ID': ID})
    if r.json() == 201:
        return True
def update(ID):
    r = requests.patch(BASE + "sync/1")
    if r.status_code == 404:
        return False
    if r.json() == 200:
        return True

def getlatestclip(ID, Username):
    r = requests.get(BASE + "sync/1", {'Command': 'getlatestclip', 'Username': Username, 'ID': ID})
    return r.json()
