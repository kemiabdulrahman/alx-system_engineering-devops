#!/usr/bin/python3
'''
data in the JSON format
'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    userid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(userid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(userid)
    todo = requests.get(url, verify=False).json()
    name = user.get('username')
    t = [{"task": t.get("title"),
          "username": name,
          "completed": t.get("completed")} for t in todo]
    b = {}
    b[userid] = t
    with open("{}.json".format(userid), 'w') as filejs:
        json.dump(b, filejs)
