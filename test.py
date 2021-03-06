import requests
import json

URL = "http://127.0.0.1:8000/stu/"

def getdata(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)
# getdata()


def postdata():
    data = {'name': 'Raju', 'roll': 32, 'city': 'Ludhiana'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
# postdata()


def updatedata():
    data = {'id':3,'name': 'Raj', 'roll': 54, 'city': 'Ludhiana'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
# updatedata()

def deletedata():
    data = {'id':3}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
deletedata()