#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = '{}users/{}'.format(url, argv[1])
    request_user = requests.get(user_id).json()
    name_user = request_user['name']
    tasks_user = requests.get('{}todos?userId={}'.format(url, argv[1])).json()
    len_tasks = len(tasks_user)
    tasks_done = requests.get('{}todos?userId={}&&completed=true'
                              .format(url, argv[1])).json()
    len_tasks_done = len(tasks_done)

    print('Employee {} is done with tasks({}/{}):'
          .format(name_user, len_tasks_done, len_tasks))
    for task in tasks_done:
        print('\t {}'.format(task['title']))
