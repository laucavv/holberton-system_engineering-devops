#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import json
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

    json_file = '{}.json'.format(argv[1])
    list_task = []
    for task in tasks_user:
        dics_tasks = {}
        dics_tasks['task'] = task['title']
        dics_tasks['completed'] = task['completed']
        dics_tasks['username'] = name_user
        list_task.append(dics_tasks)

    dict_user = {}
    dict_user[argv[1]] = list_task
    with open(json_file, mode='w') as file:
        file_w = json.dumps(dict_user)
        file.write(file_w)
