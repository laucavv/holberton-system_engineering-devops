#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = '{}users/{}'.format(url, argv[1])
    request_user = requests.get(user_id).json()
    name_user = request_user['username']
    tasks_user = requests.get('{}todos?userId={}'.format(url, argv[1])).json()
    tasks_done = requests.get('{}todos?userId={}&&completed=true'
                              .format(url, argv[1])).json()

    csvfile = '{}.csv'.format(argv[1])
    with open(csvfile, mode='w') as file:
        file_write = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in tasks_user:
            file_write.writerow([argv[1], name_user,
                                 task['completed'], task['title']])
