#!/usr/bin/python3
'''
export data in the CSV format
'''

import csv
import requests
from sys import argv

if __name__ == '__main__':
    userid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(userid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        userid)
    todo = requests.get(url, verify=False).json()
    with open("{}.csv".format(userid), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in todo:
            taskwriter.writerow([int(userid), user.get('username'),
                                 i.get('completed'),
                                 i.get('title')])
