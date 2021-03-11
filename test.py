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


def postdata(name,rollno,city):
    data = {'name': name, 'roll': rollno, 'city': city}
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
# postdata()


def updatedata(id,name,rollno,city):
    data = {'id':id,'name': name, 'roll': rollno, 'city':city}
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
# updatedata()

def deletedata(id):
    data = {'id':id}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
# deletedata()

print("1 - Send Data")
print("2 - GET Data")
print("3 - Update Data")
print("4 - Delete Data")
print("0 - Exit")
n=6
while(n!=0):
    n = int(input("Enter Option "))
    if(n==1):
        name=input("Enter Name ")
        rollno=int(input("Enter roll no "))
        city=input("Enter City ")
        postdata(name,rollno,city)
    elif(n==2):
        try:
            id=int(input("Enter ID "))
        except:
            id=None
        getdata(id)
    elif(n==3):
        id=int(input("Enter ID "))
        name = input("Enter Name ")
        rollno = int(input("Enter roll no "))
        city = input("Enter City ")
        updatedata(id,name,rollno,city)
    elif(n==4):
        id = int(input("Enter ID "))
        deletedata(id)
    else:
        exit()
