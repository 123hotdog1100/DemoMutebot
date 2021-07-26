import requests

BASE = "http://127.0.0.1:5000/"

def get_stream(ID,Username):

    r= requests.get(BASE + "sync/1", {'ID': ID, 'Username': Username})
    return r.json()

print(get_stream(1,"demomute"))