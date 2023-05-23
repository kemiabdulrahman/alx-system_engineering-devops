#!/usr/bin/python3
'''
data in the JSON format
'''
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    us = requests.get(url, verify=False).json()
    undoc = {}
    udoc = {}
    for user in us:
        uid = user.get("id")
        udoc[uid] = []
        undoc[uid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(url, verify=False).json()
    [udoc.get(i.get("userId")).append({"task": i.get("title"),
                                       "completed": i.get("completed"),
                                       "username": undoc.get(
                                               i.get("userId"))})
     for i in todo]
    with open("todo_all_employees.json", 'w') as jsf:
        json.dump(udoc, jsf)
